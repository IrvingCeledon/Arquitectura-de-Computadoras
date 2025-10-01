# Add and show every signal on wave
# add wave *

# Properties
add wave -radix binary sim:/Burrito_TB/WEnable_tb
add wave -radix unsigned sim:/Burrito_TB/Op_tb
add wave -radix unsigned sim:/Burrito_TB/D1_tb
add wave -radix unsigned sim:/Burrito_TB/D2_tb
add wave -radix unsigned sim:/Burrito_TB/RD_tb

add wave -radix binary sim:/Burrito_TB/we_tb
add wave -radix unsigned sim:/Burrito_TB/addr_tb
add wave -radix binary sim:/Burrito_TB/dout_tb
add wave -radix unsigned sim:/Burrito_TB/i
# Execute for 500 ns
run 500ns
