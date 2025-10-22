# -----------------------
# Grafic User Interface
# -----------------------

import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import assembler as assem

window = tk.Tk()
window.title("Assembler to Binary")
window.geometry("700x580")

bin_output = ""

tk.Label(window, text="Assembler input:").pack(anchor='w', padx=10)
tk.Button(window, text="Load from file", command=assem.cargar_archivo, font=("Arial", 11, "bold")).pack(pady=5)

text_input = scrolledtext.ScrolledText(window, height=8, width=70, font=("Consolas", 11))
text_input.pack(padx=10, pady=5, fill='both', expand=True)

tk.Button(window, text="Convert", command=assem.procesar_texto, font=("Arial", 11, "bold")).pack(pady=5)
tk.Button(window, text="Clear", command=assem.limpiar_texto, font=("Arial", 11, "bold")).pack(pady=5)

tk.Label(window, text="Binary ouput:").pack(anchor='w', padx=10)
text_output = scrolledtext.ScrolledText(window, height=8, width=70, font=("Consolas", 11), state='disabled')
text_output.pack(padx=10, pady=5, fill='both', expand=True)

frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=5)
tk.Button(frame_buttons, text="Copy to clipboard", command=assem.copiar_portapapeles).grid(row=0, column=0, padx=10)
tk.Button(frame_buttons, text="Save as .txt", command=assem.guardar_como_txt).grid(row=0, column=1, padx=10)

window.mainloop()
