`timescale 1ns/1ns

module ex_mem(
    clk, reset, enable, flush,
	
    // --- Control inputs ---
    reg_write_in, mem_to_reg_in,   // WB 
    branch_in, mem_read_in, mem_write_in, // MEM 
    
    // --- Data inputs ---
    zero_in, alu_result_in, read_data2_in, write_reg_in, branch_target_in,
    
    // --- Control outputs ---
    reg_write_out, mem_to_reg_out,
    branch_out, mem_read_out, mem_write_out,
    
	// Data outputs
    zero_out, alu_result_out, read_data2_out, write_reg_out, branch_target_out
);
    input wire clk;
    input wire reset;
    input wire enable;
    input wire flush;

    // Control 
    input wire reg_write_in;
    input wire mem_to_reg_in;
    input wire branch_in;
    input wire mem_read_in;
    input wire mem_write_in;

    // Data 
    input wire zero_in;
    input wire [31:0] alu_result_in;
    input wire [31:0] read_data2_in; 
    input wire [4:0]  write_reg_in;  
    input wire [31:0] branch_target_in;

    // Outputs
    output reg reg_write_out;
    output reg mem_to_reg_out;
    output reg branch_out;
    output reg mem_read_out;
    output reg mem_write_out;

    output reg zero_out;
    output reg [31:0] alu_result_out;
    output reg [31:0] read_data2_out;
    output reg [4:0]  write_reg_out;
    output reg [31:0] branch_target_out;

    always @(posedge clk) 
    begin
        if (reset | flush) begin
            reg_write_out     <= 1'b0;
            mem_to_reg_out    <= 1'b0;
            branch_out        <= 1'b0;
            mem_read_out      <= 1'b0;
            mem_write_out     <= 1'b0;
            
            zero_out          <= 1'b0;
            alu_result_out    <= 32'b0;
            read_data2_out    <= 32'b0;
            write_reg_out     <= 5'b0;
            branch_target_out <= 32'b0;
        end 
        else if (enable) begin
            reg_write_out     <= reg_write_in;
            mem_to_reg_out    <= mem_to_reg_in;
            branch_out        <= branch_in;
            mem_read_out      <= mem_read_in;
            mem_write_out     <= mem_write_in;
            
            zero_out          <= zero_in;
            alu_result_out    <= alu_result_in;
            read_data2_out    <= read_data2_in;
            write_reg_out     <= write_reg_in;
            branch_target_out <= branch_target_in;
        end
    end

endmodule