
`timescale 1ns/1ns

module Burrito_TB();
  reg [19:0] Instructions_TB;

  Burrito DUV (.Instructions(Instructions_TB));

reg we_tb;
reg [2:0] addr_tb;
reg [19:0] din_tb;
wire [19:0] dout_tb;

ram_async RAM_tb (
    .writeOn(we_tb),
    .address(addr_tb),
    .data_in(din_tb),
    .data_out(dout_tb)
);

integer i;

initial begin
  #100
  for (i = 0; i <= 5; i = i + 1) begin
    addr_tb = i;
    we_tb = 0;

    WEnable_tb = Instructions_TB[19]; 
    Op_tb = Instructions_TB[18:15];
    D1_tb = Instructions_TB[14:10];
    D2_tb = Instructions_TB[9:5]; 
    RD_tb = Instructions_TB[4:0]; 
    #100;
  end

  $stop;
end

endmodule
