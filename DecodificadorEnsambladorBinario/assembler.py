import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

def load_from_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",⁸;
        filetypes=(("Text file", "*.txt"), ("All files", "*.*"))
    )

    if not file_path:
        messagebox.showwarning("No File Selected", "No file was selected.")
        return None

    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{file_path}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    return None    
        
def assembler_to_text(text_input : str):
    text_input = text_input.strip()
    if not text_input:
        raise ValueError("The input field is empty.")

    try:
        fields = text_input.split('$')
        numbers = [int(p) for p in fields]
        binaries = [f"{n:08b}" for n in numbers]
        result = "\n".join(binaries)  # mostrar en líneas separadas
        resultado_final = "".join(binarios)  # sin espacios, para copiar o guardar
    except ValueError:
        raise ValueError("Make sure to enter a valid input.")

