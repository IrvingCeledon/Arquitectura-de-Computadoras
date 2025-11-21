import tkinter as tk
from tkinter import messagebox
from . import io_utils

class IOController:
    def __init__(self, input_widget, output_widget, language_dictionary):
        self.input_widget = input_widget
        self.output_widget = output_widget
        self.tr = language_dictionary
        
        self.utils = io_utils.IOUtils(self.tr)

    def on_load(self):
        file_content = self.utils.load_from_file()
        
        if file_content:
            self.input_widget.delete("1.0", tk.END)
            self.input_widget.insert(tk.END, file_content)
            
    def on_save(self):
        text = self.output_widget.get("1.0", tk.END).strip()
        
        try:
            self.utils.save_as_txt(text)
        except ValueError as e:
            messagebox.showinfo(self.tr["missing_fields_info_title"], str(e))
            
    def set_text_containers(self, input_widget, output_widget): 
        self.input_widget = input_widget
        self.output_widget = output_widget
        
    def apply_language(self, new_tr):
        self.tr = new_tr
        self.utils.apply_language(self.tr)
