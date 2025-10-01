//1. Module definition
module ram_async (address, data_in, data_out, writeOn);
  input [2:0] address;
  input [19:0] data_in;
  output reg [19:0] data_out;
  input writeOn;
	
//2. Internal components

// RAM creation
  reg [19:0] RAM [0:4]; 

//3. Assignments, Sequential Blocks, and Module Instances:
  initial begin
	  $readmemb("instructions.txt", RAM);  // Load of data  
  end
  
  always @* begin    
	if (writeOn) begin  // if flag rises
	  RAM[address] = data_in;  // Asynchronous writing
    end

	data_out = RAM[address];  // Asynchronous reading is always on
  end
  
endmodule