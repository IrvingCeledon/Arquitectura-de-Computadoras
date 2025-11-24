import tkinter as tk
from tkinter import messagebox
from .io_utils import IOUtils

class IOController:
    def __init__(self, input_widget=None, output_widget=None, language_dictionary=None):
        self.input_widget = input_widget
        self.output_widget = output_widget
        self.tr = language_dictionary
        self.utils = IOUtils(self.tr)

    # ----- Public methods ----- #
    def on_load(self):
        file_content = self.utils.load_from_file()
        
        if file_content is not None:
            self._write_to_input(file_content)
    
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

    # ----- Internal methods ----- #
    def _write_to_input(self, content : str):
        self.input_widget.delete("1.0", tk.END)
        self.input_widget.insert(tk.END, content)