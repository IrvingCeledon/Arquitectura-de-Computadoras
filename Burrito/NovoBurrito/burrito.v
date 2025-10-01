// Dn: Direccion n
// RD: Register direction
module Burrito(WEnable, Op, D1, D2, RD);
  input WEnable;  
  input [3:0] Op;
  input [4:0] D1, D2, RD;

wire [31:0] S1, S2, aluOut;

br BANCO (.WriteOn(WEnable), .RR1(D1), .RR2(D2), .AW(RD),
	  .DataIn(aluOut), .RD1(S1), .RD2(S2)
	  );

_ALU alu(.A(S1), .B(S2), .Sel(Op), .C(aluOut)
	 );

endmodule

// Dn: Direccion n
// RD: Register direction
module Burrito(WEnable, Op, D1, D2, RD);
  input WEnable;  
  input [3:0] Op;
  input [4:0] D1, D2, RD;

wire [31:0] S1, S2, aluOut;

br BANCO (.WriteOn(WEnable), .RR1(D1), .RR2(D2), .AW(RD),
	  .DataIn(aluOut), .RD1(S1), .RD2(S2)
	  );

_ALU alu(.A(S1), .B(S2), .Sel(Op), .C(aluOut)
	 );

endmodule
