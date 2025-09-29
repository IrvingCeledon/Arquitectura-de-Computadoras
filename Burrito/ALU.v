module _ALU(
  input[31:0] A, 
  input[31:0] B, 
  input [3:0] Sel, 
  output reg[31:0] C); 

// 2.- Internal components -> N/A

// 3.- Assignments, Sequential Blocks, and Module Instances:

always @*
begin 
 case (Sel) // The syntax {4'b000,. . .} is not required, Verilog automatically zero-extends to match the destination size.
  4'b0000 : C = {4'b0000, (A + B)}; // SUM
  4'b1111 : C = $signed({4'b0000, A}) - $signed({4'b0000, B}); // SUB
  4'b0001 : C = {4'b0000, (A & B)}; // AND
  4'b0010 : C = {4'b0000, (A | B)}; // OR
  4'b0100 : C = {4'b0000, (A ^ B)}; // XOR
  
  // 8'hFF -> Hexadecimal representation of 255 (all bits = 1)
  // 8'h00 -> Hexadecimal representation of 0   (all bits = 0)
  4'b1000 : C = (A == B) ? 8'hFF : 8'h00; // ==
  4'b0011 : C = (A > B) ? 8'hFF : 8'h00; // GREATER THAN
  
  // Using B[1:0] limits the shift amount, preventing shifts larger than the operand width.
  4'b0110 : C = A << B[2:0]; // SHIFT LEFT 
  4'b1100 : C = A >> B[2:0]; // SHIFT RIGHT 
  4'b0101 : C = A * B; // MULTIPLICATION
  default : C = 8'h00; // DEFAULT
 endcase
end

endmodule
