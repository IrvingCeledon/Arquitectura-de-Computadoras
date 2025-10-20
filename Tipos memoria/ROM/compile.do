# Cleans work folder
vlib work
vmap work work

# Build verilog modules 
vlog rom.v
vlog rom_tb.v

# Simulation configuration
vsim work.rom_tb
do simulate.do