`timescale 1ns/1ns

module mux #(parameter WIDTH = 32) (
    input  wire [WIDTH-1:0] d0, // Select 0
    input  wire [WIDTH-1:0] d1, // Select 1
    input  wire s,              // Selector
    output wire [WIDTH-1:0] y   // output
);
    assign y = (s) ? d1 : d0;

endmodule