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
$readmemb("Data.txt", DUV.BR);

// TEST 1 WriteReg = 1'b0
RegWrite_tb = 1'b0;
RR1_tb = 5'b11111;
RR2_tb = 5'b00001;
#100;

// TEST 2 WriteReg = 1'b1
RegWrite_tb = 1'b1;
WriteReg_tb = 5'b11111;
WriteData_tb = 32'hFFFFFFFF;
RR1_tb = 5'b11111;
RR2_tb = 5'b00001;
#100;

// TEST 3 WriteReg = 1'b1
RegWrite_tb = 1'b1;
WriteReg_tb = 5'b11111;
WriteData_tb = 32'd23;
RR1_tb = 5'b11111;
RR2_tb = 5'b00001;
#100;

// TEST 4 WriteReg = 1'b0
RegWrite_tb = 1'b0;
RR1_tb = 5'b01011;
RR2_tb = 5'b10001;
#100;

// TEST 5 WriteReg = 1'b1
RegWrite_tb = 1'b1;
WriteReg_tb = 5'b10001;
WriteData_tb = 32'd47;
RR1_tb = 5'b11111;
RR2_tb = 5'b10001;
#100;
$stop;
end

endmodule
