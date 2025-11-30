TRANSLATIONS = {
    "en_US": {
        # ----- AppTitle ----- #
        "app_title": "Assembler to Binary",
        
        # ----- MainWindow ----- #
        "input_lbl": "Assembler input:",
        "load_btn": "Load from file",
        "convert_btn": "Convert",
        "output_lbl": "Binary output:",
        "copy_to_clipboard_btn": "Copy to clipboard",
        "save_as_txt_btn": "Save as .txt",
        "clear_btn": "Clear",
        "exit_btn": "Exit",
        "settings_btn": "Settings",
        
        # Info messages:
        "empty_output_title": "Empty fields",
        "empty_output_message": "There is nothing to copy",
        "copied_title": "Copied!",
        "copied_message": "The result has been copied to clipboard",
        "nothing_to_clear_title": "Nothing to clear",
        "nothing_to_clear_message": "input and output are already empty",
        "cannot_clean_input_title": "Input empty",
        "cannot_clean_input_message": "Cannot clean, input is already empty",        
        "cannot_clean_output_title": "Output empty",
        "cannot_clean_output_message": "Cannot clean, output is already empty",     
        
        # ----- SettingsWindow ----- #
        "window_title": "Settings",
        "settings_title": "Settings",
        "language_lbl": "Language",
        "en_US": "English",
        "es_MX": "Spanish",
        "format_options_lbl": "Format options:",
        "dark_mode_checkbox": "Enable dark mode",
        "bit_format_checkbox": "Use 32'b instruction format output",
        "clean_options_lbl": "Clean options",
        "clean_input_checkbox": "Clean input",
        "clean_output_checkbox": "Clean output",
        "decode_options_lbl": "Decode options",
        "accumulate_checkbox": "Accumulate results in binary output",
        "truncate_checkbox": "Truncate integer inputs",
        "close_btn": "Close",
        
        # Error messages:
        "invalid_config_title": "Invalid configuration",
        "invalid_config_message": "At least one of 'Clean input' or 'Clean output' must be selected",
        
        # Info messages:
        "info_dark_mode_title": "Working on this, wait for it!",
        "info_dark_mode_message": "Dark mode not available",
        "perm_required_title": "Permission required",
        "perm_required_message": "Developer privileges are required",
        
        # ----- IOController ----- #
        "missing_fields_info_title": "Missing fields",
        
        # ----- IOUtils ----- #
        "select_file_title": "Select a file",
        "txt_option": "Text file",
        "bin_option": "Binary",
        "all_option": "All files",
        "generic_error_title": "Error",
        "error_while_opening_file_message": "File not found in: ",
        "generic_error_message": "An error occurred: ",  
        "nothing_to_export_error": "There is nothing to export.",
        "select_path": "Select the path to save the instructions",
        "export_success_title": "Exported correctly!",
        "export_success_message": "File save it in:\n",
      
        # ----- AssemblerController ----- #
        # No text to translate for the moment
        # Gonna be, gonna be golden Oh-oh-oh~~~
        
        # ----- Assembler ----- #
        "assembly_input_empty_flag": "The input field is empty",
        "unsoported_instruction_flag": "Unknow instruction, did you mistype?",
        "invalid_opcode_flag": "Invalid instruction, code not found: ",
        "hash_not_found_flag": "Missing inmediate value (#) in: ",
        "upper_limit_flag": "Invalid input, too many arguments",
        "lower_limit_flag": "Invalid input, too few arguments",
        "is_not_integer_flag": "Invalid input, please enter only whole numbers"
    },
    
    "es_MX": {
        # ----- AppTitle ----- #
        "app_title": "Ensamblador a Binario",
        
        # ----- MainWindow ----- #
        "input_lbl": "Entrada en ensamblador:",
        "load_btn": "Cargar desde un archivo",
        "convert_btn": "Procesar",
        "output_lbl": "Salida en binario:",
        "copy_to_clipboard_btn": "Copiar al portapapeles",
        "save_as_txt_btn": "Guardar como archivo .txt",
        "clear_btn": "Limpiar",
        "exit_btn": "Salir",
        "settings_btn": "Ajustes",

        # Info messages:
        "empty_output_title": "Campos vacíos",
        "empty_output_message": "No hay nada para copiar",
        "copied_title": "Copiado!",
        "copied_message": "El resultado se ha copiado al portapapeles",
        "nothing_to_clear_title": "Nada por limpiar",
        "nothing_to_clear_message": "La entrada y salida ya están vacías",
        "cannot_clean_input_title": "Entrada vacía",
        "cannot_clean_input_message": "La entrada ya se encuentra limpia",        
        "cannot_clean_output_title": "Salida vacía",
        "cannot_clean_output_message": "La salida ya se encuentra limpia",            
        
        # ----- SettingsWindow ----- #
        "window_title": "Ajustes",
        "settings_title": "Ajustes generales",
        "language_lbl": "Idioma",
        "en_US": "Inglés",
        "es_MX": "Español",
        "format_options_lbl": "Opciones de formato",
        "dark_mode_checkbox": "Cambiar a modo oscuro",
        "bit_format_checkbox": "Usar formato de salida de 32'b",
        "clean_options_lbl": "Opciones de limpieza",
        "clean_input_checkbox": "Limpiar entrada",
        "clean_output_checkbox": "Limpiar salida",
        "decode_options_lbl": "Opciones de decodificación",
        "accumulate_checkbox": "Acumalar resultados binarios en la salida",
        "truncate_checkbox": "Truncar enteros de las entradas",
        "close_btn": "Cerrar",
        
        # Error messages:
        "invalid_config_title" : "Configuración inválida",
        "invalid_config_message" : "Debe haber al menos una opción de limpieza seleccionada",
        
        # Info messages:
        "info_dark_mode_title" : "¡Función en construcción!",
        "info_dark_mode_message" : "El modo oscuro no esta disponible por el momento",
        "perm_required_title" : "Permiso denegado",
        "perm_required_message" : "Se necesitan privilegios de desarrollador para continuar",
    
        # ----- IOController ----- #
        "missing_fields_info_title": "Campos vacíos",
        
        # ----- IOUtils ----- #
        "select_file_title": "Selecciona un archivo",
        "txt_option": "Archivo de texto",
        "bin_option": "Binario",
        "all_option": "Todos los archivos",
        "generic_error_title": "Error",
        "error_while_opening_file_message": "No se pudó abrir el archivo en: ",
        "generic_error_message": "Ocurrió un error: ",  
        "nothing_to_export_error": "No hay nada para exportar",
        "select_path": "Selecciona la ruta en la que quieres guardar tus instrucciones",
        "export_success_title": "¡Exportación existosa!",
        "export_success_message": "Archivo guardado en:\n",
        
        # ----- AssemblerController ----- #
        # No text to translate for the moment
        # Boat goes binted!
        
        # ----- Assembler ----- #
        "assembly_input_empty_flag": "La entrada esta vacía",
        "unsoported_instruction_flag": "No se pudo detectar el tipo de instrucción, ¿puedes revisar tu entrada?",
        "invalid_opcode_flag": "Instrucción inválida, código no encontrado: ",
        "hash_not_found_flag": "No fue posible determinar el valor inmediato (#) en:",
        "upper_limit_flag": "Entrada inválida, demasiados argumentos",
        "lower_limit_flag": "Entrada inválida, son necesarios más argumentos",
        "is_not_integer_flag": "Entrada inválida, por favor ingresa solo números enteros"
    }
}