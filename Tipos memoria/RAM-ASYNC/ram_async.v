//1. Module definition
module ram (address, data_in, data_out, writeOn);
  input [7:0] address, data_in;
  output reg [7:0] data_out;
  input writeOn;
	
//2. Internal components

// RAM creation
  reg [7:0] RAM [0:10]; 

//3. Assignments, Sequential Blocks, and Module Instances:
  initial
  
  always @*
  begin    
    if (writeOn) begin
      RAM[address] = data_in;
    end

    data_out = RAM[address];
  end
  
endmodule
