`timescale 1ns/1ns

module ram_sync_tb();
  reg clk_tb, writeOn_tb;
  reg [4:0] address_tb;
  reg [31:0] data_in_tb;
  wire [31:0] data_out_tb;

  ram_sync DUV (.clk(clk_tb), .writeOn(writeOn_tb),
                .address(adress_tb),
                .data_in(data_in_tb),
                .data_out(data_out_tb));

  integer i;
  reg [38:0] instructions [0:4];

  // [0] address, 6'b.
  // [1] flag, 1'.
  // [2] data, 32'b.
  reg [31:0] instr_parts [2:0];

initial begin
  $readmemb("instructions.txt", instructions);

  for (i = 0; i < 5; i = i + 1) begin
    address_tb = instructions[i][38:33]; // Could be an "unused" variable
    instr_parts[0] = {27'b0, address_tb}; // Or this 

    writeOn_tb = instructions[i][32];
    instr_parts[1] = {31'b0, address_tb};

    data_in_tb = instructions[i][31:0];
    instr_parts[2] = data_in_tb;
    #100;
  end

  $stop;
end

endmodule
