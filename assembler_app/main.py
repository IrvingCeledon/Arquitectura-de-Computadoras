from tkinter import filedialog, messagebox
import string

def load_from_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Text file", "*.txt"), ("All files", "*.*"))
    )

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
        return result, "".join(binaries)  # sin espacios, para copiar o guardar
    except ValueError:
        raise ValueError("Make sure to enter a valid input.")
    
def save_as_txt(binary : string):
    if not binary:
        raise ValueError("There is nothing to export.")
    
    root = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text file", "*.txt")],
            title="Save as. . ."
    )
    
    if root: 
        with open(root, "w") as f:
            f.write(binary)
        messagebox.showinfo("Exported correctly", f"File save it in:\n{root}")    
