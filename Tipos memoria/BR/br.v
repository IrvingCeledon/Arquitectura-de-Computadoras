// 1. Definicion del modulo
// RR: Read Register
// RD: Read Data
module br (RR1, RR2, WriteReg, WriteData, RegWrite, RD1, RD2);
  input [4:0] RR1, RR2, WriteReg;
  input [31:0] WriteData;
  input RegWrite;
  output reg [31:0] RD1, RD2;

// 2. Internal Components 
  reg [31:0] BR [0:31]; 

// 3.- Assignments, Sequential Blocks, and Module Instances:
always @*
begin
  if ( RegWrite )
    BR[WriteReg] = WriteData;

  RD1 = BR[RR1];
  RD2 = BR[RR2];
end

endmodule
// Asignacion por bloqueo
