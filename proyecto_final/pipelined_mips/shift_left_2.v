`timescale 1ns/1ns

module shift_left_2(
    input  wire [31:0] in,
    output wire [31:0] out
);
    assign out = {in[29:0], 2'b00}; 
    // ? assign out = in << 2;

endmodule