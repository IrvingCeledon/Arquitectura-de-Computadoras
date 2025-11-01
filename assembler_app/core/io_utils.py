from tkinter import filedialog, messagebox
import os

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
    
    folder_path = filedialog.askdirectory(title="Select folder to save instructions")
    
    if folder_path:
        file_path = os.path.join(folder_path, "instructions.txt")
    
        with open(file_path, "w") as f:
            f.write(binary)
            
        messagebox.showinfo("Exported correctly", f"File save it in:\n{file_path}")
