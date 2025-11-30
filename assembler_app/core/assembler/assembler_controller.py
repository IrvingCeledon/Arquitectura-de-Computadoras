import tkinter as tk
from tkinter import messagebox
from .assembler import Assembler

class AssemblerController:
    def __init__(self, input_widget=None, output_widget=None, settings_manager=None, language_dictionary=None):
        self.input_widget = input_widget
        self.output_widget = output_widget
        self.settings = settings_manager
        self.tr = language_dictionary
        self.assembler = Assembler(self.tr)
  
    # ----- Public methods ----- #    
    def on_convert(self):
        text = self.input_widget.get("1.0", tk.END)
        
        try: 
            content = self.assembler.assembler_to_binary(text)
            formatted = self._format_output(content)
            self._write_output(formatted)
        except ValueError as e:
            messagebox.showerror(self.tr["generic_error_title"], str(e))

    def set_text_containers(self, input_widget, output_widget): 
        self.input_widget = input_widget
        self.output_widget = output_widget
 
    def apply_language(self, new_tr):
        self.tr = new_tr
        self.assembler.apply_language(new_tr)

    # ----- Internal methods ----- #
    def _format_output(self, result):
        if not self.settings.get("32'b_format"):
            return "\n".join(result.replace("\n", " ").split(' '))

        return result
    
    def _write_output(self, content : str):
        self.output_widget.config(state='normal')
        
        if self.settings.get("accumulate_results"):
            existing = self.output_widget.get("1.0", tk.END).rstrip("\n")
            content = f"{existing}\n{content}" if existing else content

        self.output_widget.delete("1.0", tk.END)
        self.output_widget.insert(tk.END, content)   
        self.output_widget.config(state='disabled')            
