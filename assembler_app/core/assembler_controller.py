import tkinter as tk
from tkinter import messagebox
from . import assembler

class AssemblerController:
    def __init__(self, input_widget, output_widget):
        self.input_widget = input_widget
        self.output_widget = output_widget
        
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
            
    def set_text_containers(self, input_widget, output_widget): 
        self.input_widget = input_widget
        self.output_widget = output_widget