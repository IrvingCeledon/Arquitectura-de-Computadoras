`timescale 1ns/1ns

module register_bank(
    clk,
    reset,
    reg_write,
    read_reg1,
    read_reg2,
    write_reg,
    write_data,
    read_data1,
    read_data2
);
    input wire clk;
    input wire reset;
    input wire reg_write;       
    
    input wire [4:0]  read_reg1; 
    input wire [4:0]  read_reg2;
    input wire [4:0]  write_reg; 
    input wire [31:0] write_data;
    
    output wire [31:0] read_data1;
    output wire [31:0] read_data2;

    reg [31:0] registers [0:31];
    integer i;

    // --- Write (Synchronous) ---
    always @(posedge clk) begin
        if (reset) begin
            for (i = 0; i < 32; i = i + 1) begin
                registers[i] <= 32'b0;
            end
        end
        else if (reg_write) begin
            if (write_reg != 5'b0) begin
                registers[write_reg] <= write_data;
            end
        end
    end

    // --- Read (Asynchronous/Combinational) ---
    // If address is 0, force 0 output (Hardware MIPS standard)
    assign read_data1 = (read_reg1 == 5'b0) ? 32'b0 : registers[read_reg1];
    assign read_data2 = (read_reg2 == 5'b0) ? 32'b0 : registers[read_reg2];

endmodule