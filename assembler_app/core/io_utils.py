from tkinter import filedialog, messagebox

def load_from_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Text file", "*.txt"), ("Bin", "*.bin"), ("All files", "*.*"))
    )
    
    if not file_path : return None

    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{file_path}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    return None    
    
def save_as_txt(binary : str):
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
