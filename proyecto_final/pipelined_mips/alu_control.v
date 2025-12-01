`timescale 1ns/1ns

module alu_control(
    alu_op,
    funct,
    alu_conf
);
    input wire [2:0] alu_op;
    input wire [5:0] funct;
    
    output reg [3:0] alu_conf; 

    always @(*) begin
        alu_conf = 4'b0000;

        case (alu_op)
            // CASE 0: + (LW, SW, ADDI)
            3'b000: begin
                alu_conf = 4'b0010; // ALU hace ADD
            end

            // CASE 1: - (BEQ)
            3'b001: begin
                alu_conf = 4'b0110; // ALU hace SUB
            end

            // CASE 2: TYPE R (get funct)
            3'b010: begin
                case (funct)
                    6'b100000: alu_conf = 4'b0010; // ADD 
                    6'b100010: alu_conf = 4'b0110; // SUB 
                    6'b100100: alu_conf = 4'b0000; // AND 
                    6'b100101: alu_conf = 4'b0001; // OR 
                    6'b101010: alu_conf = 4'b0111; // SLT 
                    default:   alu_conf = 4'b0000;
                endcase
            end

            // CASE 3-6: Other type I
            3'b011: alu_conf = 4'b0000; // ANDI 
            3'b100: alu_conf = 4'b0001; // ORI  
            3'b101: alu_conf = 4'b0011; // XORI 
            3'b110: alu_conf = 4'b0111; // SLTI 

            default: alu_conf = 4'b0000;
        endcase
    end

endmodule