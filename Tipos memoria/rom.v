//1.Definicion del modulo
module rom (direccion, dato_s);
	input [7:0] direccion;
	output reg [7:0] dato_s;
//2.Componentes internos
//Creacion de la ROM

reg [7:0] ROM [0:10]; 

//3.Cuerpo del modulo
initial
	begin
		ROM [0] =8'd90;
		ROM [1] =8'd80;
		ROM [2] =8'd70;
		ROM [3] =8'd60;
		ROM [4] =8'd50;
		ROM [5] =8'd40;
		ROM [6] =8'd30;
		ROM [7] =8'd20;
		ROM [8] =8'd10;
		ROM [9] =8'd100;
		ROM [10] =8'd101;
	end 


always @*
begin
	dato_s = ROM[direccion];
end


endmodule