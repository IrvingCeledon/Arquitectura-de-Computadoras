//1. Module definition
module ram_sync (clk, address, data_in, data_out, writeOn);
  input clk;
  input [4:0] address;
  input [31:0] data_in;
  output reg [31:0] data_out;
  input writeOn;
	
//2. Internal components

// RAM creation
  reg [31:0] RAM [0:31]; 

//3. Assignments, Sequential Blocks, and Module Instances:
  initial begin
	  $readmemb("Data.txt", RAM);  // Load of data  
  end
  
  always @(posedge clk) begin    
	  if (writeOn) begin  // if flag rises
      RAM[address] = data_in;  // Synchronous writing
    end

    data_out = RAM[address];  // Synchronous reading
  end
  
endmodule
