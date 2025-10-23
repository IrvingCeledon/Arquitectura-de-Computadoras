import tkinter as tk
from tkinter import messagebox
from . import assembler

class AssemblerController:
    def __init__(self, input_widget, output_widget):
        self.input_widget = input_widget
        self.output_widget = output_widget

    def on_load(self):
        file_content = assembler.load_from_file()
        if file_content:
            self.input_widget.delete("1.0", tk.END)
            self.input_widget.insert(tk.END, file_content)
    
    def on_convert(self):
        text = self.input_widget.get("1.0", tk.END)
        
        try: 
            result, full = assembler.assembler_to_text(text)
            self.output_widget.config(state='normal')
            self.output_widget.delete("1.0", tk.END)
            self.output_widget.insert(tk.END, result)
            self.output_widget.config(state='disabled')
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            
    def on_clear(self):
        self.input_widget.delete("1.0", tk.END)
        self.output_widget.config(state='normal')
        self.output_widget.delete("1.0", tk.END)
        self.output_widget.config(state='disabled')
        
    def on_save(self):
        text = self.output_widget.get("1.0", tk.END)
        
        try:
            assembler.save_as_txt(text)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
  
