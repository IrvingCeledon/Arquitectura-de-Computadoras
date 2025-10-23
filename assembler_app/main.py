import tkinter as tk
from tkinter import scrolledtext, messagebox
from core.assemblerController import AssemblerController

window = tk.Tk()
window.title("Assembler to Binary")
window.geometry("700x580")

def on_copy():
    bin_output = text_output.get("1.0", tk.END)
    
    if not bin_output:
        messagebox.showinfo("Empty fields", "There is nothing to copy.")
        return
        
    window.clipboard_clear()
    window.clipboard_append(bin_output)
    messagebox.showinfo("Copied", "The result has been copied to clipboard.")
    
def close_program():
    window.destroy()
 
''' [On Hold]
def create_std_btn(parent, text_field, method):
    btn = tk.Button(parent, text_field, method, font=("Arial", 11, "bold"))
    return btn
'''
 
# -----------------------
# Grafic User Interface
# -----------------------

tk.Label(window, text="Assembler input:").pack(anchor='w', padx=10)
text_input = scrolledtext.ScrolledText(window, height=8, width=70, font=("Consolas", 11))
text_input.pack(padx=10, pady=5, fill='both', expand=True)

input_related_buttons = tk.Frame(window)
input_related_buttons.pack(pady=5)

tk.Label(window, text="Binary ouput:").pack(anchor='w', padx=10)
text_output = scrolledtext.ScrolledText(window, height=8, width=70, font=("Consolas", 11), state='disabled')
text_output.pack(padx=10, pady=5, fill='both', expand=True)

controller = AssemblerController(text_input, text_output)
    
tk.Button(input_related_buttons, text="Load from file", command=controller.on_load, font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10, pady=5)
tk.Button(input_related_buttons, text="Convert", command=controller.on_convert, font=("Arial", 11, "bold")).grid(row=0, column=1, padx=10, pady=5)

output_related_buttons = tk.Frame(window)
output_related_buttons.pack(pady=5)
tk.Button(output_related_buttons, text="Copy to clipboard", command=on_copy, font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10)
tk.Button(output_related_buttons, text="Save as .txt", command=controller.on_save, font=("Arial", 11, "bold")).grid(row=0, column=1, padx=10)
tk.Button(output_related_buttons, text="Clear", command=controller.on_clear, font=("Arial", 11, "bold")).grid(row=0, column=2, padx=10)
tk.Button(output_related_buttons, text="Exit", command=close_program, font=("Arial", 11, "bold")).grid(row=1, column=0, columnspan=3, padx=10)
window.mainloop()
