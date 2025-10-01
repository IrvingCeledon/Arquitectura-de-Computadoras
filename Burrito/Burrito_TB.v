`timescale 1ns/1ns

module Burrito_TB();
  reg WEnable_tb;
  reg [3:0] Op_tb;
  reg [4:0] D1_tb, D2_tb, RD_tb;

Burrito DUV (.WEnable(WEnable_tb), .Op(Op_tb),
	     .D1(D1_tb), .D2(D2_tb), .RD(RD_tb));

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
  for (i = 0; i <= 5; i = i + 1) begin
    addr_tb = i;
    we_tb = 0;

    WEnable_tb = dout_tb[19]; 
    Op_tb = dout_tb[18:15];
    D1_tb = dout_tb[14:10];
    D2_tb = dout_tb[9:5]; 
    RD_tb = dout_tb[4:0]; 
    #100;
  end

  $stop;
end

endmodule