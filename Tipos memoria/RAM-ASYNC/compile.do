# Cleans work folder
vlib work
vmap work work

# Build verilog modules 
vlog ram_async.v
vlog ram_async_tb.v

# Simulation configuration
vsim work.ram_async_tb
do simulate.do