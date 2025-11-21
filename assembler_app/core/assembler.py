from resources import assembler_data

# This method works as an error handler for decoding. It receives user's input and returns the output.
def assembler_to_binary(text_input : str):
    # Checks if the user input is empty and removes possible initial Tkinter values. 
    assembly_input = text_input.strip()
    
    if not assembly_input: # If empty, raises a flag.
        raise ValueError("The input field is empty.")

    # Split by '\n' to support multiple instructions.
    instructions = assembly_input.split('\n')
    
    try: # Delegates the decoding process to format_instructions.
        return format_instructions(instructions)
    except ValueError as e:
        raise ValueError(f"{e}")

# Formats one or multiple assembly instructions by parsing each and converting them to binary.
def format_instructions(instructions):
    # Auxiliary list to store the resulting binary instructions, whether a single instruction or several.
    formatted_instructions = []
    
    for instr in instructions:
        # Removes possible residual '\n' characters or extra spaces.
        if instr.strip():
            parsed_instruction = parser(instr)
            binary_instruction = format_binary(parsed_instruction)
            formatted_instructions.append(binary_instruction)
        
    # Returns all binary instructions separated by a newline.   
    return "\n".join(formatted_instructions)
        
def parser(assembly_input : str):
    fields = assembly_input.split('$')
    instr_op = fields[0].upper().strip()
    
    instr_info = assembler_data.INSTRUCTIONS.get(instr_op)
    if instr_info is None :
        raise ValueError(f"Invalid instruction: '{instr_op}' not found.")
        
    instr_type = instr_info["type"]
    
    if instr_type == "R":
        return parser_r_fields(instr_info, fields)
    elif instr_type == "I":
        return parser_i_fields(instr_info, fields)

def parser_r_fields(instr_info, fields):
    validate_range(fields, 4)
    numbers = [fields[1], fields[2], fields[3]]
        
    return instruction_builder(instr_info, to_int(numbers))
    
def parser_i_fields(instr_info, fields):
    validate_range(fields, 3)
        
    if '#' not in fields[2]:
        raise ValueError(f"I-type instruction missing immediate (#): {fields[2]}")
        
    parts = fields[2].split('#')
    numbers = [fields[1], parts[0], parts[1]]    
        
    return instruction_builder(instr_info, to_int(numbers))
    
def validate_range(data, limit_bound):
    if len(data) > limit_bound :
        raise ValueError(f"Invalid input, too many arguments.")
    elif len(data) < limit_bound :
        raise ValueError(f"Invalid input, too few arguments.")

def to_int(data):
    try:
        print("DEBUG → to_int:", data) 
        return [int(p.strip()) for p in data]
    except ValueError:
        raise ValueError("Invalid input, please enter only whole numbers.")
    
def instruction_builder(type_info, numbers_data):
    instr_type = type_info["type"]
    print("DEBUG → instruction_builder:", numbers_data) 
    
    if instr_type == "R":
        return build_r_type(type_info, numbers_data)
    elif instr_type == "I":
        return build_i_type(type_info, numbers_data)

def build_r_type(info, data):
    """Builds the binary instruction (R-type MIPS)."""
    op  = f"{int(info['opcode']):06b}"
    rs  = f"{truncate_to_bits(data[1], 5):05b}"
    rt  = f"{truncate_to_bits(data[2], 5):05b}"
    rd  = f"{truncate_to_bits(data[0], 5):05b}"
    sh  = f"{int(info['shamt']):05b}"
    fnc = f"{int(info['funct']):06b}"

    return (op + rs + rt + rd + sh + fnc)

def build_i_type(info, data):
    """Builds the binary instruction (I-type MIPS)."""
    op  = f"{int(info['opcode']):06b}"
    rs  = f"{truncate_to_bits(data[1], 5):05b}"
    rt  = f"{truncate_to_bits(data[0], 5):05b}"
    inm = f"{truncate_to_bits(data[2], 16):016b}"
    print("DEBUG → build_i_type:", data) 
    
    return (op + rs + rt + inm)
    
def truncate_to_bits(value, bits):
    mask = (1 << bits) - 1 
    return value & mask
    
def format_binary(binary : str):
    return " ".join([binary[i:i+8] for i in range(0, len(binary), 8)])
