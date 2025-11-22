from resources import assembler_data

class Assembler:
    def __init__(self, language_dictionary):
        self.tr = language_dictionary 

    # This method works as an error handler for decoding. It receives user's input and returns the output.
    def assembler_to_binary(self, text_input):
        # Checks if the user input is empty and removes possible initial Tkinter values. 
        assembly_input = text_input.strip()
        
        if not assembly_input: # If empty, raises a flag.
            raise ValueError(self.tr["assembly_input_empty_flag"])

        # Split by '\n' to support multiple instructions.
        instructions = assembly_input.split('\n')
        
        try: # Delegates the decoding process to format_instructions.
            return self.format_instructions(instructions)
        except ValueError as e:
            raise ValueError(f"{e}")

    # Formats one or multiple assembly instructions by parsing each and converting them to binary.
    def format_instructions(self, instructions):
        # Auxiliary list to store the resulting binary instructions, whether a single instruction or several.
        formatted_instructions = []
        
        for instr in instructions:
            # Removes possible residual '\n' characters or extra spaces.
            if instr.strip():
                parsed_instruction = self.parser(instr)
                binary_instruction = self.format_binary(parsed_instruction)
                formatted_instructions.append(binary_instruction)
            
        # Returns all binary instructions separated by a newline.   
        return "\n".join(formatted_instructions)
            
    def parser(self, assembly_input : str):
        fields = assembly_input.split('$')
        instr_op = fields[0].upper().strip()
        
        instr_info = assembler_data.INSTRUCTIONS.get(instr_op)
        if instr_info is None :
            raise ValueError(f"{self.tr['invalid_isntruction_flag']} {instr_op}")
            
        instr_type = instr_info["type"]
        
        if instr_type == "R":
            return self.parser_r_fields(instr_info, fields)
        elif instr_type == "I":
            return self.parser_i_fields(instr_info, fields)

    def parser_r_fields(self, instr_info, fields):
        self.validate_range(fields, 4)
        numbers = [fields[1], fields[2], fields[3]]
            
        return self.instruction_builder(instr_info, self.to_int(numbers))
        
    def parser_i_fields(self, instr_info, fields):
        self.validate_range(fields, 3)
            
        if '#' not in fields[2]:
            raise ValueError(f"{self.tr['hash_not_found_flag']} {fields[2]}")
            
        parts = fields[2].split('#')
        numbers = [fields[1], parts[0], parts[1]]    
            
        return self.instruction_builder(instr_info, self.to_int(numbers))
        
    def validate_range(self, data, limit_bound):
        if len(data) > limit_bound :
            raise ValueError(self.tr["upper_limit_flag"])
        elif len(data) < limit_bound :
            raise ValueError(self.tr["lower_limit_flag"])

    def to_int(self, data):
        try:
            print("DEBUG → to_int:", data) 
            return [int(p.strip()) for p in data]
        except ValueError:
            raise ValueError(self.tr["is_not_integer_flag"])
        
    def instruction_builder(self, type_info, numbers_data):
        instr_type = type_info["type"]
        print("DEBUG → instruction_builder:", numbers_data) 
        
        if instr_type == "R":
            return self.build_r_type(type_info, numbers_data)
        elif instr_type == "I":
            return self.build_i_type(type_info, numbers_data)

    def build_r_type(self, info, data):
        """Builds the binary instruction (R-type MIPS)."""
        op  = f"{int(info['opcode']):06b}"
        rs  = f"{self.truncate_to_bits(data[1], 5):05b}"
        rt  = f"{self.truncate_to_bits(data[2], 5):05b}"
        rd  = f"{self.truncate_to_bits(data[0], 5):05b}"
        sh  = f"{int(info['shamt']):05b}"
        fnc = f"{int(info['funct']):06b}"

        return (op + rs + rt + rd + sh + fnc)

    def build_i_type(self, info, data):
        """Builds the binary instruction (I-type MIPS)."""
        op  = f"{int(info['opcode']):06b}"
        rs  = f"{self.truncate_to_bits(data[1], 5):05b}"
        rt  = f"{self.truncate_to_bits(data[0], 5):05b}"
        inm = f"{self.truncate_to_bits(data[2], 16):016b}"
        print("DEBUG → build_i_type:", data) 
        
        return (op + rs + rt + inm)
        
    def truncate_to_bits(self, value, bits):
        mask = (1 << bits) - 1 
        return value & mask
        
    def format_binary(self, binary : str):
        return " ".join([binary[i:i+8] for i in range(0, len(binary), 8)])
        
    def apply_language(self, new_tr):
        self.tr = new_tr