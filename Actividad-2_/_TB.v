`timescale 1ns/1ns

module _LG_TB;

reg A_tb, B_tb;
wire _AND_tb, _NAND_tb, _OR_tb, _NOR_tb, _NOT_tb,  _XOR_tb, _XNOR_tb;

  _LOGIC_GATES DUV (.A(A_tb), .B(B_tb), ._AND(_AND_tb), ._NAND(_NAND_tb), ._OR(_OR_tb), ._NOR(_NOR_tb), ._NOT(_NOT_tb), ._XOR(_XOR_tb), ._XNOR(_XNOR_tb);

initial 
begin
A_tb = 0;
B_tb = 0;
#100;
A_tb = 1;
B_tb = 0;
#100;
A_tb = 0;
B_tb = 1;
#100;
A_tb = 1;
B_tb = 1;
#100;
$stop;
end

endmodule

module _ALU_TB();

reg [3:0] A_tb, B_tb, Sel_tb;
wire [7:0] C_tb;

_ALU DUV (.A(A_tb), .B(B_tb), .Sel(Sel_tb), .C(C_tb));

initial
begin
// TEST SUM
A_tb = 4'b0010;
B_tb = 4'b1000;
Sel_tb = 4'b0000;
#100;

// TEST SUB
A_tb = 4'b0010;
B_tb = 4'b1000;
Sel_tb = 4'b1111;
#100;

// TEST AND
A_tb = 4'b1110;
B_tb = 4'b0001;
Sel_tb = 4'b0001;
#100;

// TEST OR
A_tb = 4'b1110;
B_tb = 4'b0001;
Sel_tb = 4'b0010;
#100;

// TEST XOR
A_tb = 4'b1111;
B_tb = 4'b0101;
Sel_tb = 4'b0100; // Overflow
#100;

// TEST == (TRUE)
A_tb = 4'b1001;
B_tb = 4'b1001;
Sel_tb = 4'b1000; // Overflow
#100;

// TEST == (FALSE)
A_tb = 4'b1001;
B_tb = 4'b0101;
Sel_tb = 4'b1000; // Overflow
#100;

// TEST > (TRUE)
A_tb = 4'b1111;
B_tb = 4'b0111;
Sel_tb = 4'b0011; 
#100;

// TEST > (FALSE)
A_tb = 4'b0111;
B_tb = 4'b1111;
Sel_tb = 4'b0011; 
#100;

// TEST <<
A_tb = 4'b1000;
B_tb = 4'b0111;
Sel_tb = 4'b0110; 
#100;

// TEST >>
A_tb = 4'b0010;
B_tb = 4'b0001;
Sel_tb = 4'b1100; 
#100;

// TEST MULTIPLICATION
A_tb = 4'b1011;
B_tb = 4'b0111;
Sel_tb = 4'b0101; 
#100;
$stop;
end

endmodule
