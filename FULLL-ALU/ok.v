module Pre_ALU(input[3:0] A, input[3:0] B, input Sel[1:0], output reg[3:0] C);

// 2.- Internal components -> N/A

// 3.- Assignments, Sequential Blocks, and Module Instances:

always @*
begin 
 case (Sel) // Doesn't use begin
   1'b0 : C = A + B;
   1'b1 : C = A & B;
   default : C = 4'b0000; // Best Practices?
 endcase
end
  
endmodule 
