`timescale 1ns/1ns

module id_ex(
    clk, reset, enable, flush,
	
    // control inputs
    reg_write_in, mem_to_reg_in,   // WB
    branch_in, mem_read_in, mem_write_in, // MEM
    reg_dst_in, alu_op_in, alu_src_in,    // EX
    // data inputs
    pc_in, read_data1_in, read_data2_in, sign_ext_in, rt_in, rd_in,
	
    // control outputs
    reg_write_out, mem_to_reg_out,
    branch_out, mem_read_out, mem_write_out,
    reg_dst_out, alu_op_out, alu_src_out,
    // data ouputs
    pc_out, read_data1_out, read_data2_out, sign_ext_out, rt_out, rd_out
);
    input wire clk;
    input wire reset;
    input wire enable;
    input wire flush;

    // --- (WB Stage) ---
    input wire reg_write_in;
    input wire mem_to_reg_in;
    
    // --- (MEM Stage) ---
    input wire branch_in;
    input wire mem_read_in;
    input wire mem_write_in;
    
    // --- (EX Stage) ---
    input wire reg_dst_in;
    input wire [2:0] alu_op_in; 
    input wire alu_src_in;

    // --- Data Signals ---
    input wire [31:0] pc_in;
    input wire [31:0] read_data1_in; // Rs value
    input wire [31:0] read_data2_in; // Rt value
    input wire [31:0] sign_ext_in;   // Inmediato extendido
    input wire [4:0] rt_in;          // Instruction[20:16]
    input wire [4:0] rd_in;          // Instruction[15:11]

    // --- Outputs ---
    output reg reg_write_out;
    output reg mem_to_reg_out;
    output reg branch_out;
    output reg mem_read_out;
    output reg mem_write_out;
    output reg reg_dst_out;
    output reg [2:0] alu_op_out;
    output reg alu_src_out;

    output reg [31:0] pc_out;
    output reg [31:0] read_data1_out;
    output reg [31:0] read_data2_out;
    output reg [31:0] sign_ext_out;
    output reg [4:0] rt_out;
    output reg [4:0] rd_out;

    always @(posedge clk) 
    begin
        if (reset | flush) begin
            reg_write_out  <= 1'b0;
            mem_to_reg_out <= 1'b0;
            branch_out     <= 1'b0;
            mem_read_out   <= 1'b0;
            mem_write_out  <= 1'b0;
            reg_dst_out    <= 1'b0;
            alu_op_out     <= 2'b0;
            alu_src_out    <= 1'b0;
            
            pc_out         <= 32'b0;
            read_data1_out <= 32'b0;
            read_data2_out <= 32'b0;
            sign_ext_out   <= 32'b0;
            rt_out         <= 5'b0;
            rd_out         <= 5'b0;
        end 
        else if (enable) begin
            reg_write_out  <= reg_write_in;
            mem_to_reg_out <= mem_to_reg_in;
            branch_out     <= branch_in;
            mem_read_out   <= mem_read_in;
            mem_write_out  <= mem_write_in;
            reg_dst_out    <= reg_dst_in;
            alu_op_out     <= alu_op_in;
            alu_src_out    <= alu_src_in;
            
            pc_out         <= pc_in;
            read_data1_out <= read_data1_in;
            read_data2_out <= read_data2_in;
            sign_ext_out   <= sign_ext_in;
            rt_out         <= rt_in;
            rd_out         <= rd_in;
        end
    end

endmodule