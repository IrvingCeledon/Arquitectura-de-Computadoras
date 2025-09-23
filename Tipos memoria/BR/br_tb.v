`timescale 1ns/1ns

module _br_tb();

reg [4:0] RR1_tb, RR2_tb, WriteReg_tb;
reg [31:0] WriteData_tb;
reg RegWrite_tb;
wire [31:0] RD1_tb, RD2_tb;

br DUV (.RR1(RR1_tb), .RR2(RR2_tb), .WriteReg(WriteReg_tb), 
	.WriteData(WriteData_tb), 
	.RegWrite(RegWrite_tb),
	.RD1(RD1_tb), .RD2(RD2_tb));

initial
begin
// TEST WriteReg = 1'b1
RR1_tb = 5'hFF;
RR2_tb = 5'hFF;
RegWrite_tb = 1'b0;
#100;

// TEST WriteReg = 1'b0
// RR1_tb = 5'b10110;
// RR2_tb = 5'h00;
RegWrite_tb = 1'b1;
WriteReg_tb = 1'h00;
#100;
$stop;
end

endmodule

// initial
// begin
// $readmemb("Data.txt", Banco);
// end
