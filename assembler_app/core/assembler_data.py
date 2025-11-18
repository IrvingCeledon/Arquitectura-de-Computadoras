INSTRUCTIONS = {
    # --------- R-TYPE ---------
    "ADD": {"type": "R", "opcode": 0b000000, "shamt": 0b00000, "funct": 0b100000},
    "SUB": {"type": "R", "opcode": 0b000000, "shamt": 0b00000, "funct": 0b100010},
    "OR":  {"type": "R", "opcode": 0b000000, "shamt": 0b00000, "funct": 0b100101},

    # --------- I-TYPE ---------
    "ADDI":  {"type": "I", "opcode": 0b001000},  
    "ADDIU": {"type": "I", "opcode": 0b001001}, # I-TYPE doesn't have an SUB instruction, we'll use negative addition. 
    "ORI":   {"type": "I", "opcode": 0b001101},  

    # --------- OTHER I-TYPE INSTRUCTIONS ---------
    "LW":  {"type": "I", "opcode": 0b100011},     
    "SW":  {"type": "I", "opcode": 0b101011},
    "BEQ": {"type": "I", "opcode": 0b000100}    
}
