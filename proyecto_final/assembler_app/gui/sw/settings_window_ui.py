import tkinter as tk
from tkinter import ttk, messagebox

class SettingsWindowUI:
    def __init__(self, parent, main_frame, language_dictionary):
        self.parent = parent
        self.main_frame = main_frame
        self.tr = language_dictionary
        
        self._build_ui()
    
    def _build_ui(self):
        self._configure_window()
        self._build_header()
        self._build_body()

    def _configure_window(self):
        self.parent.title(self.tr["window_title"])
        self.parent.geometry("320x400")
        self.parent.resizable(False, False)
        self.main_frame.configure(bg="#f0f0f0")
        
    def _build_header(self):
        self.settings_title = tk.Label(
            self.main_frame, 
            text=self.tr["settings_title"], 
            font=("Arial", 14, "bold"), 
            bg="#f0f0f0"
        )
        self.settings_title.pack(pady=10)
    
    def _build_body(self):
        self._build_language_section()
        self._build_format_section()
        self._build_clean_section()
        self._build_decode_section()
        self._build_action_buttons()

    def _build_language_section(self):
        self.language_lbl = tk.Label(self.main_frame, text=self.tr["language_lbl"], bg="#f0f0f0")
        self.language_lbl.pack(anchor='w', padx=20)        
        
        self.language_var = tk.StringVar() 

        self.language_box = ttk.Combobox(
            self.main_frame,
            textvariable=self.language_var,
            state="readonly"
        )
        self.language_box.pack(padx=20, pady=5, fill='x')
    
    def _build_format_section(self):
        self.format_options_lbl = tk.Label(
            self.main_frame, 
            text=self.tr["format_options_lbl"], 
            bg="#f0f0f0"
        )
        self.format_options_lbl.pack(anchor='w', padx=20)
        
        self.format_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.format_frame.pack(anchor='w', padx=35, pady=5, fill='x')    
        
        self.dark_mode_checkbox = ttk.Checkbutton(
            self.format_frame, 
            text=self.tr["dark_mode_checkbox"]
        )
        self.dark_mode_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.bit_format_checkbox = ttk.Checkbutton(
            self.format_frame, 
            text=self.tr["bit_format_checkbox"]
        )
        self.bit_format_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="w")         
    
    def _build_clean_section(self):
        self.clean_options_lbl = tk.Label(
            self.main_frame, 
            text=self.tr["clean_options_lbl"], 
            bg="#f0f0f0"
        )
        self.clean_options_lbl.pack(anchor='w', padx=20)
        
        self.clean_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.clean_frame.pack(anchor='w', padx=35, pady=5, fill='x')

        self.clean_input_checkbox = ttk.Checkbutton(
            self.clean_frame, 
            text=self.tr["clean_input_checkbox"]
        )
        self.clean_input_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.clean_output_checkbox = ttk.Checkbutton(
            self.clean_frame, 
            text=self.tr["clean_output_checkbox"]
        )
        self.clean_output_checkbox.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    
    def _build_decode_section(self):
        self.decode_options_lbl = tk.Label(self.main_frame, text=self.tr["decode_options_lbl"], bg="#f0f0f0")
        self.decode_options_lbl.pack(anchor='w', padx=20)
        
        self.decode_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.decode_frame.pack(anchor='w', padx=35, pady=5, fill='x')
        
        self.accumulate_checkbox = ttk.Checkbutton(
            self.decode_frame, 
            text=self.tr["accumulate_checkbox"]
        )
        self.accumulate_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.truncate_checkbox = ttk.Checkbutton(
            self.decode_frame, 
            text=self.tr["truncate_checkbox"]
        )
        self.truncate_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")        
    
    def _build_action_buttons(self):
        button_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        button_frame.pack(pady=15, fill='x')
        
        self.close_btn = ttk.Button(
            button_frame, 
            text=self.tr["close_btn"]
        )
        self.close_btn.pack(side='right', padx=20)
    
    def apply_language(self, new_tr):
        self.tr = new_tr
        
        self.parent.title(self.tr["window_title"])
        self.settings_title.config(text=self.tr["settings_title"])
        
        self.language_lbl.config(text=self.tr["language_lbl"])
        self.format_options_lbl.config(text=self.tr["format_options_lbl"])
        self.clean_options_lbl.config(text=self.tr["clean_options_lbl"])
        self.decode_options_lbl.config(text=self.tr["decode_options_lbl"])

        self.dark_mode_checkbox.config(text=self.tr["dark_mode_checkbox"])
        self.bit_format_checkbox.config(text=self.tr["bit_format_checkbox"])
        self.clean_input_checkbox.config(text=self.tr["clean_input_checkbox"])
        self.clean_output_checkbox.config(text=self.tr["clean_output_checkbox"])
        self.accumulate_checkbox.config(text=self.tr["accumulate_checkbox"])
        self.truncate_checkbox.config(text=self.tr["truncate_checkbox"])
        self.close_btn.config(text=self.tr["close_btn"])    

    def get_widgets(self):
        return {
            "language":     self.language_box,
            "dark_mode":    self.dark_mode_checkbox,
            "bit_format":   self.bit_format_checkbox,
            "clean_input":  self.clean_input_checkbox,
            "clean_output": self.clean_output_checkbox,
            "accumulate":   self.accumulate_checkbox,
            "truncate":     self.truncate_checkbox,
            "close":        self.close_btn,
        }    
    
    def get_parent(self):
        return self.parent
    
    def show_error(self, title, text):
        messagebox.showerror(title, text, parent=self.parent)
    
    def show_info(self, title, text):
        messagebox.showinfo(title, text, parent=self.parent)