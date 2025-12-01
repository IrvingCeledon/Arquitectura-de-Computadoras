`timescale 1ns/1ns

module control_unit(
    opcode,
    reg_dst,
    branch,
    mem_read,
    mem_to_reg,
    alu_op,
    mem_write,
    alu_src,
    reg_write,
    jump
);
    input wire [5:0] opcode;

    output reg reg_dst;
    output reg branch;
    output reg mem_read;
    output reg mem_to_reg;
    output reg [2:0] alu_op; 
    output reg mem_write;
    output reg alu_src;
    output reg reg_write;
    output reg jump;         

    always @(*) begin
        reg_dst    = 1'b0;
        branch     = 1'b0;
        mem_read   = 1'b0;
        mem_to_reg = 1'b0;
        alu_op     = 3'b000;
        mem_write  = 1'b0;
        alu_src    = 1'b0;
        reg_write  = 1'b0;
        jump       = 1'b0;

        case (opcode)
            // --- ( TYPE-R ) ---
            // ADD, SUB, AND, OR, SLT 
            6'b000000: begin
                reg_dst    = 1'b1;
                alu_src    = 1'b0; 
                mem_to_reg = 1'b0;
                reg_write  = 1'b1; 
                mem_read   = 1'b0;
                mem_write  = 1'b0;
                branch     = 1'b0;
                jump       = 1'b0;
                alu_op     = 3'b010; 
            end

            // --- ( TYPE I ) ---
            // LW (Load Word) 
            6'b100011: begin
                reg_dst    = 1'b0;
                alu_src    = 1'b1; 
                mem_to_reg = 1'b1;
                reg_write  = 1'b1; 
                mem_read   = 1'b1; 
                mem_write  = 1'b0;
                branch     = 1'b0;
                jump       = 1'b0;
                alu_op     = 3'b000;
            end

            // SW (Store Word) 
            6'b101011: begin
                reg_dst    = 1'bx; 
                alu_src    = 1'b1; 
                mem_to_reg = 1'bx; 
                reg_write  = 1'b0; 
                mem_read   = 1'b0;
                mem_write  = 1'b1;
                branch     = 1'b0;
                jump       = 1'b0;
                alu_op     = 3'b000; 
            end

            // BEQ (Branch Equal) 
            6'b000100: begin
                reg_dst    = 1'bx;
                alu_src    = 1'b0; 
                mem_to_reg = 1'bx;
                reg_write  = 1'b0;
                mem_read   = 1'b0;
                mem_write  = 1'b0;
                branch     = 1'b1;
                jump       = 1'b0;
                alu_op     = 3'b001; 
            end

            // ADDI (Add Immediate) 
            6'b001000: begin
                reg_dst    = 1'b0; 
                alu_src    = 1'b1; 
                mem_to_reg = 1'b0; 
                reg_write  = 1'b1;
                mem_read   = 1'b0;
                mem_write  = 1'b0;
                branch     = 1'b0;
                jump       = 1'b0;
                alu_op     = 3'b000; 
            end

            // ANDI (And Immediate) 
            6'b001100: begin
                reg_dst    = 1'b0;
                alu_src    = 1'b1;
                mem_to_reg = 1'b0;
                reg_write  = 1'b1;
                mem_read   = 1'b0;
                mem_write  = 1'b0;
                branch     = 1'b0;
                jump       = 1'b0;
                alu_op     = 3'b011; 
            end

            // ORI (Or Immediate) 
            6'b001101: begin
                reg_dst    = 1'b0;
                alu_src    = 1'b1;
                mem_to_reg = 1'b0;
                reg_write  = 1'b1;
                mem_read   = 1'b0;
                mem_write  = 1'b0;
                branch     = 1'b0;
                jump       = 1'b0;
                alu_op     = 3'b100;
            end
            
            // XORI (Xor Immediate) 
            6'b001110: begin
                reg_dst    = 1'b0;
                alu_src    = 1'b1;
                mem_to_reg = 1'b0;
                reg_write  = 1'b1;
                mem_read   = 1'b0;
                mem_write  = 1'b0;
                branch     = 1'b0;
                jump       = 1'b0;
                alu_op     = 3'b101; 
            end

            // SLTI (Set Less Than Immediate) 
            6'b001010: begin
                reg_dst    = 1'b0;
                alu_src    = 1'b1;
                mem_to_reg = 1'b0;
                reg_write  = 1'b1;
                mem_read   = 1'b0;
                mem_write  = 1'b0;
                branch     = 1'b0;
                jump       = 1'b0;
                alu_op     = 3'b110; 
            end

            // --- ( TYPE J ) ---
            // J (Jump) 
            6'b000010: begin
                reg_dst    = 1'bx;
                alu_src    = 1'bx;
                mem_to_reg = 1'bx;
                reg_write  = 1'b0;
                mem_read   = 1'b0;
                mem_write  = 1'b0;
                branch     = 1'b0;
                jump       = 1'b1;  
                alu_op     = 3'bxxx;
            end

            default: begin
                reg_dst    = 1'b0;
                branch     = 1'b0;
                mem_read   = 1'b0;
                mem_to_reg = 1'b0;
                alu_op     = 3'b000;
                mem_write  = 1'b0;
                alu_src    = 1'b0;
                reg_write  = 1'b0;
                jump       = 1'b0;
            end
        endcase
    end
	
endmodule