`timescale 1ns/1ns

module data_memory(
    input wire clk,
    input wire mem_write,
    input wire mem_read,
    input wire [31:0] address,
    input wire [31:0] write_data,
    
    output wire [31:0] read_data
);
    // 1KB memory
    reg [7:0] memory [0:1023];
    
    integer i;

    // I think this initialization is optional
    initial begin
        for (i = 0; i < 1024; i = i + 1) begin
            memory[i] = 8'b0;
        end

		$readmemb("data.txt", memory);
    end

    // --- Synchronous Write (SW) ---
    always @(posedge clk) begin
        if (mem_write) begin
            // Big Endian
            memory[address]     <= write_data[31:24];
            memory[address + 1] <= write_data[23:16];
            memory[address + 2] <= write_data[15:8];
            memory[address + 3] <= write_data[7:0];
        end
    end

    // --- Asynchronous read (LW) ---
	// Build a 'word' from 4 bytes and force 32'b format
    assign read_data = (mem_read) ? 
                       {memory[address], memory[address+1], memory[address+2], memory[address+3]} : 
                       32'b0;

endmodule