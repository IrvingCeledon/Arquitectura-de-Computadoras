// 1. Definicion del modulo
// RR: Read Register
// AW: Address Write
// RD: Read Data
module br (WriteOn, RR1, RR2, AW, DataIn, RD1, RD2);
  input WriteOn;
  input [4:0] RR1, RR2, AW;
  input [31:0] DataIn;
  output reg [31:0] RD1, RD2;

// 2. Internal Components 
  reg [31:0] BR [0:31]; 

// 3.- Assignments, Sequential Blocks, and Module Instances:
initial begin
  $readmemb("BR_DATA.txt", BR);
end

always @*
begin
  if ( WriteOn )
    BR[AW] = DataIn;

  RD1 = BR[RR1];
  RD2 = BR[RR2];
end

endmodule
// Asignacion por bloqueo
