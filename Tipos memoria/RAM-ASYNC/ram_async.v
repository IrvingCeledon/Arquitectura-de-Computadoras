//1. Module definition
module ram (address, data_in, data_out, writeOn);
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
  
  always @* begin    
	if (writeOn) begin  // if flag rises
	  RAM[address] = data_in;  // Asynchronous writing
    end

	data_out = RAM[address];  // Asynchronous reading is always on
  end
  
endmodule
