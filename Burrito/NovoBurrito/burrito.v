// Dn: Direccion n
// RD: Register direction
// AW: Address Write
module Burrito(Instructions);
	input [19:0] Instructions;
	wire [31:0] S1, S2, aluOut;

	br BANCO (.WriteOn(Instructions[19]), .RR1(Instructions[14:10]), .RR2(Instructions[9:5]), 
			      .AW(Instructions[4:0]), .DataIn(aluOut), .RD1(S1), .RD2(S2)
	         );

	_ALU alu(.A(S1), .B(S2), .Sel(Instructions[18:15]), .C(aluOut));

endmodule
