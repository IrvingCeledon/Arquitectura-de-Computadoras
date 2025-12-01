`timescale 1ns/1ns

module if_id(clk, reset, enable, flush, pc_in, instruction_in, pc_out, instruction_out);
	input wire clk;
	input wire reset;
	input wire enable;
	input wire flush;
	
	input wire [31:0] pc_in;
	input wire [31:0] instruction_in;
	
	output reg [31:0] pc_out;
	output reg [31:0] instruction_out;

    always @(posedge clk) 
	begin
        if (reset | flush) begin
            pc_out   		<= 32'b0;
            instruction_out <= 32'b0;
        end 
        else if (enable) begin
            pc_out   <= pc_in;
            instruction_out <= instruction_in;
        end
    end

endmodule