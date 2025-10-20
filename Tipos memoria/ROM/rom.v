//1. Module definition
module rom (address, data_out);
  input [5:0] address;
  output reg [31:0] data_out;
	
//2. Internal components

// ROM creation
  reg [31:0] ROM [0:31]; 

//3. Assignments, Sequential Blocks, and Module Instances:
  initial begin
    $readmemb("data.txt", ROM);  // Load of data  
  end
	
  always @* begin    
    data_out = ROM[address];  // Read Only Memory
  end
  
endmodule
