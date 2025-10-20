# Add and show every signal on wave
# add wave *

# Properties
add wave -radix unsigned sim:/rom_tb/address_tb
add wave -radix decimal sim:/rom_tb/data_out_tb

add wave -radix decimal sim:/rom_tb/instructions
# Execute for 500 ns
run 500ns
