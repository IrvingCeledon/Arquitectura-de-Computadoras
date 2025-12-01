`timescale 1ns/1ns

module instruction_memory(
    input wire [31:0] address, 
    output wire [31:0] instruction
);

    // 1KB (1024 bytes) memory
    reg [7:0] memory [0:1023];

    initial begin
        $readmemb("instructions.txt", memory);
    end

    // Read in Big Endian 
    assign instruction = {
        memory[address],     // More significant Byte
        memory[address + 1],
        memory[address + 2],
        memory[address + 3]  // Less significant Byte
    };

endmodule