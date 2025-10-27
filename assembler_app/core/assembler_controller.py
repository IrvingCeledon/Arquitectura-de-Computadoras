import tkinter as tk
from tkinter import messagebox
from . import assembler

class AssemblerController:
    def __init__(self, input_widget, output_widget, settings_manager):
        self.input_widget = input_widget
        self.output_widget = output_widget
        self.settings = settings_manager
        
    def on_convert(self):
        text = self.input_widget.get("1.0", tk.END)
        
        try: 
            result = assembler.assembler_to_binary(text)
            formatted = self.format_output(result)
            self.output_widget.config(state='normal')
            self.insert_to_output(formatted)
            self.output_widget.config(state='disabled')
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            
    def set_text_containers(self, input_widget, output_widget): 
        self.input_widget = input_widget
        self.output_widget = output_widget
        
    def insert_to_output(self, result):
        if self.settings.get("accumulate_results"):
            existing = self.output_widget.get("1.0", tk.END).rstrip("\n")
            
            if existing:
                new_output = existing + "\n" + result
            else:
                new_output = result + "\n"
            
            self.output_widget.delete("1.0", tk.END)
            self.output_widget.insert(tk.END, new_output)
        else:            
            self.output_widget.delete("1.0", tk.END)
            self.output_widget.insert(tk.END, result)
            
    def format_output(self, result):
        if not self.settings.get("32'b_format"):
            return "\n".join(result.replace("\n", " ").split(' '))
        else:
            return result