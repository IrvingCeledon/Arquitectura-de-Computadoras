from . import assembler_data

def assembler_to_binary(text_input : str):
    assembly_input = text_input.strip()
    
    if not assembly_input:
        raise ValueError("The input field is empty.")

    instructions = assembly_input.split('\n')
    
    try:
        return format_instructions(instructions)
    except ValueError as e:
        raise ValueError(f"{e}")

def format_instructions(instructions):
    formatted_instructions = []
    
    for instr in instructions:
        if instr.strip():
            parsed_instruction = parser(instr)
            binary_instruction = format_binary(parsed_instruction)
            formatted_instructions.append(binary_instruction)
        
    return "\n".join(formatted_instructions)
        
def parser(assembly_input : str):
    fields = assembly_input.split('$')
    
    # This could be just one if.
    if len(fields) > 4 :
        raise ValueError(f"Invalid input, too many arguments.")
    elif len(fields) < 4 :
        raise ValueError(f"Invalid input, too few arguments.")
    
    instr_op = fields[0].upper().strip()
    instr_info = assembler_data.INSTRUCTIONS.get(instr_op)
    
    if instr_info is None :
        raise ValueError(f"Invalid instruction: '{instr_op}' not found.")
        
    try:
        # Skip first element (opcode), convert rest to int.
        numbers = [int(p) for p in fields[1:]]
    except ValueError:
        raise ValueError("Invalid input, please enter only whole numbers.")
        
    return instruction_builder(instr_info, numbers)
    
def instruction_builder(instr_info, numbers):
    """Builds the binary instruction (R-type MIPS)."""
    op  = f"{int(instr_info['opcode']):06b}"
    rs  = f"{truncate_to_bits(numbers[1], 5):05b}"
    rt  = f"{truncate_to_bits(numbers[2], 5):05b}"
    rd  = f"{truncate_to_bits(numbers[0], 5):05b}"
    sh  = f"{int(instr_info['shamt']):05b}"
    fnc = f"{int(instr_info['funct']):06b}"

    return (op + rs + rt + rd + sh + fnc)
    
def truncate_to_bits(value, bits):
    mask = (1 << bits) - 1 
    return value & mask
    
def format_binary(binary : str):
    return " ".join([binary[i:i+8] for i in range(0, len(binary), 8)])
