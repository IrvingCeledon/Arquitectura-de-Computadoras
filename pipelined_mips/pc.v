`timescale 1ns/1ns

module pc(
    input wire pc_clk,
    input wire reset,     
    input wire enable,      
    input wire [31:0] next,
    output reg [31:0] current
);

    always @(posedge pc_clk) begin
        if (reset) begin
            current <= 32'b0;
        end
        else if (enable) begin
            current <= next;  // Updates if not Stall
        end
    end

endmodule