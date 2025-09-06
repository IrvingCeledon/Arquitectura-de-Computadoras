module Pre_ALU(input[3:0] A, input[3:0] B, input Sel[3:0], output reg[3:0] C); //output reg[7:0] C

// 2.- Internal components -> N/A

// 3.- Assignments, Sequential Blocks, and Module Instances:

always @*
begin 
 case (Sel) // Doesn't use begin
   4'b0000 : C = A + B; // SUM
   4'b1111 : C = A - B; // REST
   4'b0001 : C = A & B; // AND
   4'b0010 : C = A | B; // OR
   4'b0100 : C = A ^ B; // XOR
   4'b1000 : 
    begin 
     if (A == B)
      C = 4'b1111;
     else
      C = 4'b0000;
    end
   4'b0011 : C = A > B; // HIGHER THAN
    begin 
     if (A > B)
      C = 4'b1111;
     else
      C = 4'b0000;
    end
   4'b0110 : C = A << B; // LEFT LOGICAL DISPLACEMENT      
   4'b1100 : C = A >> B; // RIGHT LOGICAL DISPLACEMENT 
   4'b0101 : C = A * B; // MULTIPLICATION
   default : C = 4'b0000; // Best Practices?
 endcase
end
 C = (A > B) ? 4'b1111 : 4'b0000;
 C = (A * B)[3:0];
