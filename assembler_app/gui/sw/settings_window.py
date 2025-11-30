import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from gui import create_button, create_frames

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent, settings_manager, on_apply, language_dictionary, change_language):
        super().__init__(parent)
        self.geometry("350x420")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")
        
        self.settings = settings_manager
        self.tr = language_dictionary
        self.title(self.tr["window_title"])
        
        self.on_apply = on_apply
        self.change_language = change_language
        self.initialize_widgets()

    def initialize_widgets(self):
        # --- Header ---
        self.settings_title = tk.Label(self, text=self.tr["settings_title"], font=("Arial", 14, "bold"), bg="#f0f0f0")
        self.settings_title.pack(pady=10)
        
        # ---- Body ----
        self.language_section()
        self.format_section()        
        self.clean_section()
        self.decode_section()
        self.validation_related_buttons()   
    
    def language_section(self):
        self.language_lbl = tk.Label(self, text=self.tr["language_lbl"], bg="#f0f0f0")
        self.language_lbl.pack(anchor='w', padx=20)        
        
        self.languages_model = [ ("en_US", self.tr["en_US"]), ("es_MX", self.tr["es_MX"]) ]
        visible_values = [text for _, text in self.languages_model]
        
        self.language_var = tk.StringVar() 
        self.language_box = ttk.Combobox(
            self,
            textvariable=self.language_var,
            values=visible_values,
            state="readonly"  
        )
        self.language_box.pack(padx=20, pady=5, fill='x')
        
        current_language = self.settings.get("language")
        for i, (code, _) in enumerate(self.languages_model):
            if code == current_language:
                self.language_box.current(i)
                
        self.language_box.bind("<<ComboboxSelected>>", self.on_language_selected)
        
    # This has to change
    def on_language_selected(self, event=None):
        index = self.language_box.current()
        language_code = self.languages_model[index][0]

        # Changes settings_manager data
        self.settings.set("language", language_code)

        # Executes app_manager set_language method.
        self.change_language()
        
        # Updates dictionary  
        from resources import TRANSLATIONS
        self.tr = TRANSLATIONS[language_code]

        # Automatic translation
        self.apply_language()
    
    def format_section(self):
        self.format_options_lbl = tk.Label(self, text=self.tr["format_options_lbl"], bg="#f0f0f0")
        self.format_options_lbl.pack(anchor='w', padx=20)
        
        self.format_frame = tk.Frame(self, bg="#f0f0f0")
        self.format_frame.pack(anchor='w', padx=35, pady=5, fill='x')    
        
        self.dark_mode = tk.BooleanVar(value=self.settings.get("dark_mode"))
        self.dark_mode_checkbox = ttk.Checkbutton(self.format_frame, text=self.tr["dark_mode_checkbox"], variable=self.dark_mode)
        self.dark_mode_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.output_format = tk.BooleanVar(value=self.settings.get("32'b_format"))
        self.bit_format_checkbox = ttk.Checkbutton(self.format_frame, text=self.tr["bit_format_checkbox"], variable=self.output_format)
        self.bit_format_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="w") 

    def clean_section(self):
        self.clean_options_lbl = tk.Label(self, text=self.tr["clean_options_lbl"], bg="#f0f0f0")
        self.clean_options_lbl.pack(anchor='w', padx=20)
        
        self.clean_frame = tk.Frame(self, bg="#f0f0f0")
        self.clean_frame.pack(anchor='w', padx=35, pady=5, fill='x')

        self.clean_input = tk.BooleanVar(value=self.settings.get("clean_input"))
        self.clean_input_checkbox = ttk.Checkbutton(self.clean_frame, text=self.tr["clean_input_checkbox"], variable=self.clean_input)
        self.clean_input_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.clean_output = tk.BooleanVar(value=self.settings.get("clean_output"))
        self.clean_output_checkbox = ttk.Checkbutton(self.clean_frame, text=self.tr["clean_output_checkbox"], variable=self.clean_output)
        self.clean_output_checkbox.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    def decode_section(self):
        self.decode_options_lbl = tk.Label(self, text=self.tr["decode_options_lbl"], bg="#f0f0f0")
        self.decode_options_lbl.pack(anchor='w', padx=20)
        
        self.decode_frame = tk.Frame(self, bg="#f0f0f0")
        self.decode_frame.pack(anchor='w', padx=35, pady=5, fill='x')
        
        self.accumulate_results = tk.BooleanVar(value=self.settings.get("accumulate_results"))
        self.accumulate_checkbox = ttk.Checkbutton(self.decode_frame, text=self.tr["accumulate_checkbox"], variable=self.accumulate_results)
        self.accumulate_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.truncate_binaries = tk.BooleanVar(value=self.settings.get("truncate_binaries"))
        self.truncate_checkbox = ttk.Checkbutton(self.decode_frame, text=self.tr["truncate_checkbox"], variable=self.truncate_binaries)
        self.truncate_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    def validation_related_buttons(self):
        button_frame = tk.Frame(self, bg="#f0f0f0")
        button_frame.pack(pady=15, fill='x')
        
        self.close_btn = ttk.Button(button_frame, text=self.tr["close_btn"], command=self.apply_changes)
        self.close_btn.pack(side='right', padx=20)

    def apply_changes(self):
        # If validate_changes() rise a flag, returns.
        if not self.validate_changes():
            return
        
        index = self.language_box.current()
        selected_language = self.languages_model[index][0] 
        self.settings.set("language", selected_language)

        self.settings.set("32'b_format", self.output_format.get())
        self.settings.set("dark_mode", self.dark_mode.get())
        self.settings.set("clean_input", self.clean_input.get())
        self.settings.set("clean_output", self.clean_output.get())
        self.settings.set("accumulate_results", self.accumulate_results.get())
        self.settings.set("truncate_binaries", self.truncate_binaries.get())
        
        self.settings.save()
        self.on_apply()
        self.destroy()
        
    def apply_language(self):
        self.title(self.tr["window_title"])
        self.settings_title.config(text=self.tr["settings_title"])
        self.language_lbl.config(text=self.tr["language_lbl"])
        
        visible_values = [self.tr[code] for code, _ in self.languages_model]
        self.language_box["values"] = visible_values
        
        current_language = self.settings.get("language")

        for i, (code, _) in enumerate(self.languages_model):
            if code == current_language:
                self.language_box.current(i)
                break
        
        self.format_options_lbl.config(text=self.tr["format_options_lbl"])
        self.dark_mode_checkbox.config(text=self.tr["dark_mode_checkbox"])
        self.bit_format_checkbox.config(text=self.tr["bit_format_checkbox"])
        self.clean_options_lbl.config(text=self.tr["clean_options_lbl"])
        self.clean_input_checkbox.config(text=self.tr["clean_input_checkbox"])
        self.clean_output_checkbox.config(text=self.tr["clean_output_checkbox"])
        self.decode_options_lbl.config(text=self.tr["decode_options_lbl"])
        self.accumulate_checkbox.config(text=self.tr["accumulate_checkbox"])
        self.truncate_checkbox.config(text=self.tr["truncate_checkbox"])
        self.close_btn.config(text=self.tr["close_btn"])
        
    def validate_changes(self):
        if not self.clean_input.get() and not self.clean_output.get():
            messagebox.showerror(self.tr["invalid_config_title"], 
                                self.tr["invalid_config_message"],
                                parent=self)                    
            return False
   
        if self.dark_mode.get() == True:
            messagebox.showinfo(self.tr["info_dark_mode_title"], self.tr["info_dark_mode_message"], parent=self)
            self.dark_mode.set(False)
            return False
            
        if self.truncate_binaries.get() == False:
            messagebox.showinfo(self.tr["perm_required_title"], self.tr["perm_required_message"], parent=self)
            self.truncate_binaries.set(True)
            return False
            
        return True
