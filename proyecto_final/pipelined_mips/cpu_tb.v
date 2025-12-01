`timescale 1ns/1ns

module cpu_tb();
    reg clk;
    reg reset;

    cpu DUV ( .clk(clk), .reset(reset) );

    integer i;  

    initial begin
        clk = 0;
        forever #5 clk = ~clk;
    end

    initial begin
        $display("=== SIMULATION START: BUBBLE SORT MIPS 32 ===");
        reset = 1;
        #20;        
        reset = 0;  
        $display("CPU STARTING... EXECUTING BUBBLE SORT");

        repeat(100000) @(posedge clk);

        $display("\n=== CHECK RESULTS IN DATA MEMORY ===");

        $display("=== SORTED RESULT ===");
        for (i = 0; i < 25; i = i + 1) begin
            $write("%0d ", DUV.DATA_MEM.memory[i]);
        end
        $write("\n");

        $display("=== SIMULATION END ===");
        $stop; 
    end

endmodule
