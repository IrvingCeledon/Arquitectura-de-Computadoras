`timescale 1ns/1ns

module adder(
    input  wire [31:0] op1,
    input  wire [31:0] op2,
    output wire [31:0] result
);
    assign result = op1 + op2;

endmodule