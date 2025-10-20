module register_bank(address, inst_out);
  input [31:0] address;
  output reg [31:0] inst_out;

  reg [7:0] memory_bank [0:255];
  
  initial begin 
    $readmemb("instructions.txt", memory_bank);
  end
// It will be nice an if to avoid overflow.
  always @* begin 
    inst_out = {memory_bank[address], memory_bank[address + 1],
                memory_bank[address + 2], memory_bank[address + 3]};
  end

endmodule
