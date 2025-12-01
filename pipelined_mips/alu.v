`timescale 1ns/1ns

module alu(
    op1,
    op2,
    alu_conf,
    alu_result,
    zero
);
    input wire [31:0] op1;
    input wire [31:0] op2;
    input wire [3:0]  alu_conf; // Comes from alu_control

    output reg [31:0] alu_result;
    output wire       zero;     // Flag for jumps (BEQ)

	// Zero is always true if result is 0
    assign zero = (alu_result == 32'b0);

    always @(*) begin
        case(alu_conf)
            // Logical
            4'b0000: alu_result = op1 & op2;       // AND
            4'b0001: alu_result = op1 | op2;       // OR
            4'b0011: alu_result = op1 ^ op2;       // XOR (XORI)
            4'b1100: alu_result = ~(op1 | op2);    // NOR (MIPS standar)

            // Arithmetics
            4'b0010: alu_result = op1 + op2;       // ADD
            4'b0110: alu_result = op1 - op2;       // SUB

            // Set Less Than
            4'b0111: begin                         // SLT
                // Use %signed to make a signed comparation (two's complement)
                if ($signed(op1) < $signed(op2))
                    alu_result = 32'd1;
                else
                    alu_result = 32'd0;
            end

            default: alu_result = 32'b0;
        endcase
    end

endmodule