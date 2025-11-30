import tkinter as tk
from tkinter import scrolledtext
from gui import create_button, create_frames

class MainWindowUI:
    def __init__(self, root, language_dictionary):
        self.root = root
        self.tr = language_dictionary
        
        self._build_ui()
  
    def _build_ui(self):
        self._create_input_section()
        self._create_output_section()
        self._create_buttons()
   
    def _create_input_section(self):
        self.input_lbl = tk.Label(self.root, text=self.tr["input_lbl"])
        self.input_lbl.pack(anchor='w', padx=10)
        
        self.text_input = scrolledtext.ScrolledText(
            self.root, 
            height=8, 
            width=70, 
            font=("Consolas", 11)
        )
        self.text_input.pack(padx=10, pady=5, fill='both', expand=True)    
        
        self.input_frame  = create_frames(self.root, 5, 'x', 2) # Declare this here just for aesthetic purposes.        

    def _create_output_section(self):
        self.output_lbl = tk.Label(self.root, text=self.tr["output_lbl"])
        self.output_lbl.pack(anchor='w', padx=10)
        
        self.text_output = scrolledtext.ScrolledText(
            self.root, 
            height=8, 
            width=70, 
            font=("Consolas", 11), 
            state='disabled'
        )
        self.text_output.pack(padx=10, pady=5, fill='both', expand=True)
   
    def get_text_input(self):
        return self.text_input
    
    def get_text_output(self):
        return self.text_output

    def _create_buttons(self):
        self._init_input_buttons()
        self._init_output_buttons()

    def _init_input_buttons(self): 
        self.load_from_file_btn = create_button(self.input_frame, self.tr["load_btn"], None)
        self.load_from_file_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.convert_btn = create_button(self.input_frame, self.tr["convert_btn"], None)
        self.convert_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    
    def _init_output_buttons(self): 
        self.output_frame = create_frames(self.root, pady_value=5, fill_value='x', range_size=2)

        self.copy_btn = create_button(self.output_frame, self.tr["copy_to_clipboard_btn"], None)
        self.save_btn = create_button(self.output_frame, self.tr["save_as_txt_btn"], None)
        self.clear_btn = create_button(self.output_frame, self.tr["clear_btn"], None)
        self.exit_btn = create_button(self.output_frame, self.tr["exit_btn"], self.root.destroy)
        self.settings_btn = create_button(self.output_frame, self.tr["settings_btn"], None)

        buttons = [self.copy_btn, self.save_btn, self.clear_btn]
        for i, btn in enumerate(buttons):
            btn.grid(row=0, column=i, padx=5, pady=5, sticky="ew")

        self.exit_btn.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
        self.settings_btn.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="ew")        

    def get_buttons(self):
        return {
            "load": self.load_from_file_btn,
            "convert": self.convert_btn,
            "copy": self.copy_btn,
            "save": self.save_btn,
            "clear": self.clear_btn,
            "exit": self.exit_btn,
            "settings": self.settings_btn,
        }

    def apply_language(self, new_tr):
        self.tr = new_tr
        self.input_lbl.config(text=self.tr["input_lbl"])
        self.output_lbl.config(text=self.tr["output_lbl"])

        for btn, key in [
            (self.load_from_file_btn, "load_btn"),
            (self.convert_btn, "convert_btn"),
            (self.copy_btn, "copy_to_clipboard_btn"),
            (self.save_btn, "save_as_txt_btn"),
            (self.clear_btn, "clear_btn"),
            (self.exit_btn, "exit_btn"),
            (self.settings_btn, "settings_btn"),
            ]:
                btn.config(text=self.tr[key])
