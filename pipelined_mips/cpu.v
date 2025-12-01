`timescale 1ns/1ns

module cpu(
    input wire clk,
    input wire reset
);
    // --- IF Stage (Instruction Fetch) ---
    wire [31:0] pc_current;
    wire [31:0] pc_next, pc_next_branch, pc_plus_4_if;
    wire [31:0] instruction_if;
    
    // --- ID Stage (Instruction Decode) ---
    wire [31:0] pc_plus_4_id;
    wire [31:0] instruction_id;
    wire [31:0] read_data1_id, read_data2_id;
    wire [31:0] sign_ext_imm_id;
    wire [31:0] jump_address;
    
    // Control Signals ID
    wire reg_dst_id, branch_id, mem_read_id, mem_to_reg_id;
    wire [2:0] alu_op_id;
    wire mem_write_id, alu_src_id, reg_write_id, jump_id;

    // --- EX Stage (Execute) ---
    wire reg_write_ex, mem_to_reg_ex;
    wire branch_ex, mem_read_ex, mem_write_ex;
    wire reg_dst_ex, alu_src_ex;
    wire [2:0] alu_op_ex;
    
    wire [31:0] pc_plus_4_ex;
    wire [31:0] read_data1_ex, read_data2_ex;
    wire [31:0] sign_ext_imm_ex;
    wire [4:0]  rt_ex, rd_ex, write_reg_ex;
    
    wire [31:0] alu_input_b;
    wire [31:0] alu_result_ex;
    wire zero_ex;
    wire [3:0] alu_conf;
    wire [31:0] branch_offset_shifted;
    wire [31:0] branch_target_ex;

    // --- MEM Stage (Memory) ---
    wire reg_write_mem, mem_to_reg_mem;
    wire branch_mem, mem_read_mem, mem_write_mem;
    wire zero_mem;
    wire [31:0] alu_result_mem, read_data2_mem;
    wire [4:0]  write_reg_mem;
    wire [31:0] branch_target_mem;
    wire [31:0] memory_read_data_mem;
    
    wire pc_src; 

    // --- WB Stage (Write Back) ---
    wire reg_write_wb, mem_to_reg_wb;
    wire [31:0] read_data_wb, alu_result_wb;
    wire [4:0]  write_reg_wb;
    wire [31:0] result_wb;

    // ==============
    // (HAZARD UNIT)
    // ==============
    
    wire hazard_detected;
    
    wire hazard_ex = reg_write_ex && (write_reg_ex != 0) && 
                     (write_reg_ex == instruction_id[25:21] || write_reg_ex == instruction_id[20:16]);
                     
    wire hazard_mem = reg_write_mem && (write_reg_mem != 0) && 
                      (write_reg_mem == instruction_id[25:21] || write_reg_mem == instruction_id[20:16]);

    wire hazard_wb = reg_write_wb && (write_reg_wb != 0) && 
                     (write_reg_wb == instruction_id[25:21] || write_reg_wb == instruction_id[20:16]);

    assign hazard_detected = hazard_ex | hazard_mem | hazard_wb;

    // =====================================
    // First Stage: IF - INSTRUCTION FETCH
    // =====================================

    assign pc_next_branch = (pc_src) ? branch_target_mem : pc_plus_4_if;
    assign pc_next = (jump_id) ? jump_address : pc_next_branch;

    pc PC_MODULE (
        .pc_clk(clk),
        .reset(reset),
        .enable(~hazard_detected), 
        .next(pc_next),
        .current(pc_current)
    );

    adder PC_ADDER (
        .op1(pc_current),
        .op2(32'd4),
        .result(pc_plus_4_if)
    );

    instruction_memory INST_MEM (
        .address(pc_current),
        .instruction(instruction_if)
    );

    // BUFFER IF/ID
    if_id PIPE_IF_ID (
        .clk(clk),
        .reset(reset),
        .enable(~hazard_detected), 
        .flush(pc_src | jump_id), 
        .pc_in(pc_plus_4_if),
        .instruction_in(instruction_if),
        .pc_out(pc_plus_4_id),
        .instruction_out(instruction_id)
    );

    // ======================================
    // SECOND STAGE: ID - INSTRUCTION DECODE
    // ======================================

    control_unit CONTROL (
        .opcode(instruction_id[31:26]),
        .reg_dst(reg_dst_id),
        .branch(branch_id),
        .mem_read(mem_read_id),
        .mem_to_reg(mem_to_reg_id),
        .alu_op(alu_op_id),
        .mem_write(mem_write_id),
        .alu_src(alu_src_id),
        .reg_write(reg_write_id),
        .jump(jump_id)
    );

    register_bank REG_FILE (
        .clk(clk),
        .reset(reset),
        .reg_write(reg_write_wb),     
        .read_reg1(instruction_id[25:21]), 
        .read_reg2(instruction_id[20:16]), 
        .write_reg(write_reg_wb),     
        .write_data(result_wb),       
        .read_data1(read_data1_id),
        .read_data2(read_data2_id)
    );

    sign_extend SIGN_EXT (
        .in(instruction_id[15:0]),
        .out(sign_ext_imm_id)
    );

    assign jump_address = {pc_plus_4_id[31:28], instruction_id[25:0], 2'b00};

    // BUFFER ID/EX
    id_ex PIPE_ID_EX (
        .clk(clk), .reset(reset), .enable(1'b1), 
        .flush(pc_src | hazard_detected), 
        
        // Control Inputs
        .reg_write_in(reg_write_id), .mem_to_reg_in(mem_to_reg_id),
        .branch_in(branch_id), .mem_read_in(mem_read_id), .mem_write_in(mem_write_id),
        .reg_dst_in(reg_dst_id), .alu_op_in(alu_op_id), .alu_src_in(alu_src_id),
        // Data Inputs
        .pc_in(pc_plus_4_id),
        .read_data1_in(read_data1_id), .read_data2_in(read_data2_id),
        .sign_ext_in(sign_ext_imm_id),
        .rt_in(instruction_id[20:16]), .rd_in(instruction_id[15:11]),
        
        // Outputs
        .reg_write_out(reg_write_ex), .mem_to_reg_out(mem_to_reg_ex),
        .branch_out(branch_ex), .mem_read_out(mem_read_ex), .mem_write_out(mem_write_ex),
        .reg_dst_out(reg_dst_ex), .alu_op_out(alu_op_ex), .alu_src_out(alu_src_ex),
        .pc_out(pc_plus_4_ex),
        .read_data1_out(read_data1_ex), .read_data2_out(read_data2_ex),
        .sign_ext_out(sign_ext_imm_ex),
        .rt_out(rt_ex), .rd_out(rd_ex)
    );

    // ======================
    // Third Stage: EX - EXECUTE
    // ======================

    shift_left_2 SHIFT_BRANCH (
        .in(sign_ext_imm_ex),
        .out(branch_offset_shifted)
    );

    adder BRANCH_ADDER (
        .op1(pc_plus_4_ex),
        .op2(branch_offset_shifted),
        .result(branch_target_ex)
    );

    mux #(.WIDTH(32)) MUX_ALU_SRC (
        .d0(read_data2_ex),
        .d1(sign_ext_imm_ex),
        .s(alu_src_ex),
        .y(alu_input_b)
    );

    alu_control ALU_CTRL (
        .alu_op(alu_op_ex),
        .funct(sign_ext_imm_ex[5:0]), 
        .alu_conf(alu_conf)
    );

    alu ALU_MAIN (
        .op1(read_data1_ex),
        .op2(alu_input_b),
        .alu_conf(alu_conf),
        .alu_result(alu_result_ex),
        .zero(zero_ex)
    );

    mux #(.WIDTH(5)) MUX_REG_DST (
        .d0(rt_ex),
        .d1(rd_ex),
        .s(reg_dst_ex),
        .y(write_reg_ex)
    );

    // BUFFER EX/MEM
    ex_mem PIPE_EX_MEM (
        .clk(clk), .reset(reset), .enable(1'b1), 
        .flush(pc_src),
        
        // Control
        .reg_write_in(reg_write_ex), .mem_to_reg_in(mem_to_reg_ex),
        .branch_in(branch_ex), .mem_read_in(mem_read_ex), .mem_write_in(mem_write_ex),
        // Data
        .zero_in(zero_ex),
        .alu_result_in(alu_result_ex),
        .read_data2_in(read_data2_ex),
        .write_reg_in(write_reg_ex),
        .branch_target_in(branch_target_ex),
        
        // Outputs
        .reg_write_out(reg_write_mem), .mem_to_reg_out(mem_to_reg_mem),
        .branch_out(branch_mem), .mem_read_out(mem_read_mem), .mem_write_out(mem_write_mem),
        .zero_out(zero_mem),
        .alu_result_out(alu_result_mem),
        .read_data2_out(read_data2_mem),
        .write_reg_out(write_reg_mem),
        .branch_target_out(branch_target_mem)
    );

    // ==================================
    // Fourth Stage: MEM - MEMORY ACCESS
    // ==================================

    assign pc_src = branch_mem & zero_mem;

    data_memory DATA_MEM (
        .clk(clk),
        .mem_write(mem_write_mem),
        .mem_read(mem_read_mem),
        .address(alu_result_mem),
        .write_data(read_data2_mem),
        .read_data(memory_read_data_mem)
    );

    // BUFFER MEM/WB
    mem_wb PIPE_MEM_WB (
        .clk(clk), .reset(reset), .enable(1'b1), .flush(1'b0),
        // Control
        .reg_write_in(reg_write_mem), .mem_to_reg_in(mem_to_reg_mem),
        // Data
        .read_data_in(memory_read_data_mem),
        .alu_result_in(alu_result_mem),
        .write_reg_in(write_reg_mem),
        
        // Outputs
        .reg_write_out(reg_write_wb), .mem_to_reg_out(mem_to_reg_wb),
        .read_data_out(read_data_wb),
        .alu_result_out(alu_result_wb),
        .write_reg_out(write_reg_wb)
    );

    // =============================
    // Fifth Stage: WB - WRITE BACK
    // =============================

    mux #(.WIDTH(32)) MUX_MEM_TO_REG (
        .d0(alu_result_wb),
        .d1(read_data_wb), 
        .s(mem_to_reg_wb),
        .y(result_wb)
    );

endmodule