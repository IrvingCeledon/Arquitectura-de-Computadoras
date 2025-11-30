INSTRUCTIONS = {
    # --------- R-TYPE ---------
    "ADD": {"type": "R", "opcode": 0b000000, "shamt": 0b00000, "funct": 0b100000},
    "SUB": {"type": "R", "opcode": 0b000000, "shamt": 0b00000, "funct": 0b100010},
    "AND": {"type": "R", "opcode": 0b000000, "shamt": 0b00000, "funct": 0b100100},
    "OR":  {"type": "R", "opcode": 0b000000, "shamt": 0b00000, "funct": 0b100101},
    "SLT": {"type": "R", "opcode": 0b000000, "shamt": 0b00000, "funct": 0b101010},

    # --------- I-TYPE ---------
    
    # Arithmetic/Logical
    "ADDI":  {"type": "I", "opcode": 0b001000},
    "ANDI":  {"type": "I", "opcode": 0b001100},
    "ORI":   {"type": "I", "opcode": 0b001101},
    "XORI":  {"type": "I", "opcode": 0b001110},
    "SLTI":  {"type": "I", "opcode": 0b001010},
    "ADDIU": {"type": "I", "opcode": 0b001001}, # I-TYPE doesn't have an SUB instruction, we'll use negative addition. 


    # Flow control
    "BEQ": {"type": "I", "opcode": 0b000100},

    # Memory
    "LW":  {"type": "I", "opcode": 0b100011},
    "SW":  {"type": "I", "opcode": 0b101011},

    # --------- J-TYPE ---------
    "J":   {"type": "J", "opcode": 0b000010}
}
