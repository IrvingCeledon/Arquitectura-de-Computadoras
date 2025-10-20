`timescale 1ns/1ns

module cpu_tb();
  reg clk_tb;
  wire [31:0] cpuInst_tb;

  cpu DUV (.clk(clk_tb), .cpuInst(cpuInst_tb));

  always #50 clk_tb = ~clk_tb;

  initial begin
    clk_tb = 1'b0;
    #250;
  end

endmodule

