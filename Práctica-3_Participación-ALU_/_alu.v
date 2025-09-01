module Pre_ALU(input[3:0] A, input[3:0] B, input Sel, output reg[3:0] C);

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

`timescale 1ns/1ns

module _PRE_ALU_TB();

reg [3:0] A_tb, B_tb;
reg Sel_tb;
wire [3:0] C_tb;

Pre_ALU DUV (.A(A_tb), .B(B_tb), .Sel(Sel_tb), .C(C_tb));

initial
begin
A_tb = 4'b0010;
B_tb = 4'b1000;
Sel_tb = 1'b0;
#100;
A_tb = 4'b0010;
B_tb = 4'b1000;
Sel_tb = 1'b1;
#100;
A_tb = 4'b1110;
B_tb = 4'b0001;
Sel_tb = 1'b0;
#100;
A_tb = 4'b1110;
B_tb = 4'b0001;
Sel_tb = 1'b1;
#100;
A_tb = 4'b1111;
B_tb = 4'b0101;
Sel_tb = 1'b0; // Overflow
#100;
$stop;
end

endmodule
