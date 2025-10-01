# Cleans work folder
vlib work
vmap work work

# Build verilog modules 
vlog ALU.v
vlog BR.v
vlog burrito.v
vlog ram_async.v
vlog Burrito_TB.v

# Simulation configuration
vsim work.Burrito_TB
do simulate.do