`timescale 1ns/1ns

module _LG_TB;

reg A_tb, B_tb;
wire _AND_tb, _NAND_tb, _OR_tb, _NOR_tb, _NOT_tb,  _XOR_tb, _XNOR_tb;

_LOGIC_GATES DUV (.A(A_tb), .B(B_tb), ._AND(_AND_tb), 
		  ._NAND(_NAND_tb), ._OR(_OR_tb), ._NOR(_NOR_tb), 
		  ._NOT(_NOT_tb), ._XOR(_XOR_tb), ._XNOR(_XNOR_tb));

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
