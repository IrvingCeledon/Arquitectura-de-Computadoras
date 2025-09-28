`timescale 1ns/1ns

module _ram_tb();

reg [4:0] address_tb, RR2_tb, WriteReg_tb;
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
  
//1. Module definition
module ram (address, data_in, data_out, writeOn);
  input [5:0] address;
  input [31:0] data_in;
  output reg [31:0] data_out;
  input writeOn;
	
//2. Internal components

// RAM creation
  reg [31:0] RAM [0:31]; 

//3. Assignments, Sequential Blocks, and Module Instances:
  initial begin
	  $readmemb("Data.txt", RAM);  // Load of data  
  end
  
  always @* begin    
	if (writeOn) begin  // if flag rises
	  RAM[address] = data_in;  // Asynchronous writing
    end

	data_out = RAM[address];  // Asynchronous reading is always on
  end
  
endmodule
