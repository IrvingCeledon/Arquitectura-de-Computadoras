`timescale 1ns/1ns

module cpu(clk, cpuInst);
  input clk;
  output [31:0] cpuInst;

  wire [31:0] W1, W2;

  pc PC(.pc_clk(clk), .next(W1), .current(W2));
  register_bank memory(.address(W1), .inst_out(cpuInst));
  adder add(.op1(4), .op2(W1), .result(W2));
  

endmodule
