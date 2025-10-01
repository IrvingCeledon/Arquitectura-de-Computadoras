# Add and show every signal on wave
# add wave *

# Properties
add wave -radix unsigned sim:/ram_async_tb/address_tb
add wave -radix binary sim:/ram_async_tb/writeOn_tb
add wave -radix decimal sim:/ram_async_tb/data_in_tb
add wave -radix decimal sim:/ram_async_tb/data_out_tb
add wave -radix binary sim:/ram_async_tb/instructions
add wave -radix unsigned sim:/ram_async_tb/i

add wave -radix unsigned sim:/ram_async_tb/instr_parts[0]
add wave -radix unsigned sim:/ram_async_tb/instr_parts[1]
add wave -radix unsigned sim:/ram_async_tb/instr_parts[2]

# Execute for 500 ns
run 500ns
