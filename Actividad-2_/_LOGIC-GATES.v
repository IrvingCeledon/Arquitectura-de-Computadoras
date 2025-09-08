module _LOGIC_GATES(
  input A,
  input B,
  output _AND,
  output _NAND,
  output _OR,
  output _NOR,
  output _NOT, 
  output _XOR,
  output _XNOR);

// 2.- Internal components -> N/A

// 3.- Assignments, Sequential Blocks, and Module Instances:

assign _AND = A&B; 
assign _NAND = ~(A&B); 
assign _OR = A|B; 
assign _NOR = ~(A|B); 
assign _NOT = ~A; 
assign _XOR = A^B; 
assign _XNOR = ~(A^B); 

endmodule
