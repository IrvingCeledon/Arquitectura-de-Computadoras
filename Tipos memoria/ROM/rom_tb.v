`timescale 1ns/1ns

module rom_tb();
  reg [5:0] address_tb;
  wire [31:0] data_out_tb;

  rom DUV (.address(address_tb), .data_out(data_out_tb));
  integer i;
  reg [5:0] instructions [0:4];

initial begin 
  // This file only have addresses.
  $readmemb("instructions.txt", instructions); 
  #10 // A slight delay in loading data.

  for (i = 0; i < 5; i = i + 1) begin
    address_tb = instructions[i][5:0];
    #100;
  end

  $stop;
end

endmodule
