# Cleans work folder
vlib work
vmap work work

# Build verilog modules 
vlog ram_sync.v
vlog ram_sync_tb.v

# Simulation configuration
vsim work.ram_sync_tb
do simulate.do