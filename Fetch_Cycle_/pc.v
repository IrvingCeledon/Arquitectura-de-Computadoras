`timescale 1ns/1ns

module pc(pc_clk, next, current);
  input pc_clk;
  input [31:0] next;
  output reg [31:0] current;
// It will be nice an if that resets.
  initial begin
    current = 32'b0;
    #5;
  end

  always @(posedge pc_clk) begin
    current = next;
  end

endmodule
