def assembler_to_text(text_input : str):
    text_input = text_input.strip()
    if not text_input:
        raise ValueError("The input field is empty.")

    try:
        fields = text_input.split('$')
        numbers = [int(p) for p in fields]
        binaries = [f"{n:08b}" for n in numbers]
        result = "\n".join(binaries)  # mostrar en líneas separadas
        return result, "".join(binaries)  # sin espacios, para copiar o guardar
    except ValueError:
        raise ValueError("Make sure to enter a valid input.")