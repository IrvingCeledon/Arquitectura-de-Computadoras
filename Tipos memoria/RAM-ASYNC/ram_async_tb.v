`timescale 1ns/1ns

module _ram_tb();
	reg [4:0] address_tb;
	reg writeOn_tb;
	reg [31:0] data_in_tb;
	wire [31:0] data_out;

ram DUV (.address(address_tb), 
		 .writeOn(writeOn_tb), 
		 .data_in(data_in_tb), 
		 .data_out(data_out));

	reg [38:0] instructions [0:4]; 

initial

begin
	$readmemb("instructions.txt", instructions);

	for (int i = 0; i < 5; i++) begin
		address_tb = instructions[i][38:33];
		writeOn_tb = instructions[i][32];
		data_in_tb = instructions[i][31:0];
		#100
	end

	$stop;
end
	
endmodule
