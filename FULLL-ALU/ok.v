module Pre_ALU(
 input[3:0] A, 
 input[3:0] B, 
 input [3:0] Sel, 
 output reg[7:0] C); 

// 2.- Internal components -> N/A

// 3.- Assignments, Sequential Blocks, and Module Instances:

always @*
begin 
 case (Sel) 
  4'b0000 : C = {4'b0000, (A + B)}; // SUM
  4'b1111 : C = {4'b0000, (A - B)}; // REST
  4'b0001 : C = {4'b0000, (A & B)}; // AND
  4'b0010 : C = {4'b0000, (A | B)}; // OR
  4'b0100 : C = {4'b0000, (A ^ B)}; // XOR
  4'b1000 : C = (A == B) ? 8'hFF : 8'h00; // ==
  4'b0011 : C = (A > B) ? 8'hFF : 8'h00; // HIGHER THAN
  4'b0110 : C = A << B[2:0]; // LEFT LOGICAL DISPLACEMENT      
  4'b1100 : C = A >> B[2:0]; // RIGHT LOGICAL DISPLACEMENT 
  4'b0101 : C = A * B; // MULTIPLICATION
  default : C = 8'h00; // DEFAULT
 endcase
end
