ˋtimescale 1ns/1ns

module ram_sync_tb();
  reg clk_tb, writeOn_tb;
  reg [4:5] address_tb;
  reg [31:0] data_in_tb;
  wire [31:0] data_out_tb;
