import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from gui.widgets_factory import create_button, create_frames

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent, settings_manager, on_apply, change_language):
        super().__init__(parent)
        self.title("Settings")
        self.title(tr["window_title"])
        self.geometry("350x420")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")
        
        self.settings = settings_manager
        self.on_apply = on_apply
        self.change_language = change_language
        self.initialize_widgets()

    def initialize_widgets(self):
        # --- Header ---
        tk.Label(self, text="Settings", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)
        
        # ---- Body ----
        self.language_section()
        self.format_section()        
        self.clean_section()
        self.decode_section()
        self.validation_related_buttons()
        
    def format_section(self):
        tk.Label(self, text="Format options:", bg="#f0f0f0").pack(anchor='w', padx=20)
        self.format_frame = tk.Frame(self, bg="#f0f0f0")
        self.format_frame.pack(anchor='w', padx=35, pady=5, fill='x')    
        
        self.dark_mode = tk.BooleanVar(value=self.settings.get("dark_mode"))
        ttk.Checkbutton(self.format_frame, text="Enable dark mode", variable=self.dark_mode)\
        .grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.output_format = tk.BooleanVar(value=self.settings.get("32'b_format"))
        ttk.Checkbutton(self.format_frame, text="Use 32'b instruction format output", variable=self.output_format)\
        .grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
    
    def language_section(self):
        tk.Label(self, text="Language:", bg="#f0f0f0").pack(anchor='w', padx=20)        
        
        self.language_var = tk.StringVar(value=self.settings.get("language")) 
        language_box = ttk.Combobox(
            self,
            textvariable=self.language_var,
            values=["English", "Spanish"],
            state="readonly"  
        )
        language_box.pack(padx=20, pady=5, fill='x')

    def clean_section(self):
        tk.Label(self, text="Clean options", bg="#f0f0f0").pack(anchor='w', padx=20)
        self.clean_frame = tk.Frame(self, bg="#f0f0f0")
        self.clean_frame.pack(anchor='w', padx=35, pady=5, fill='x')

        self.clean_input = tk.BooleanVar(value=self.settings.get("clean_input"))
        ttk.Checkbutton(self.clean_frame, text="Clean input", variable=self.clean_input)\
        .grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.clean_output = tk.BooleanVar(value=self.settings.get("clean_output"))
        ttk.Checkbutton(self.clean_frame, text="Clean output", variable=self.clean_output)\
        .grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    def decode_section(self):
        tk.Label(self, text="Decode options", bg="#f0f0f0").pack(anchor='w', padx=20)
        self.decode_frame = tk.Frame(self, bg="#f0f0f0")
        self.decode_frame.pack(anchor='w', padx=35, pady=5, fill='x')
        
        self.accumulate_results = tk.BooleanVar(value=self.settings.get("accumulate_results"))
        ttk.Checkbutton(self.decode_frame, text="Accumulate results in binary output", variable=self.accumulate_results)\
        .grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.truncate_binaries = tk.BooleanVar(value=self.settings.get("truncate_binaries"))
        ttk.Checkbutton(self.decode_frame, text="Truncate integer inputs", variable=self.truncate_binaries)\
        .grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    def validation_related_buttons(self):
        button_frame = tk.Frame(self, bg="#f0f0f0")
        button_frame.pack(pady=15, fill='x')
        ttk.Button(button_frame, text="Apply", command=self.apply_changes).pack(side='left', padx=20)
        ttk.Button(button_frame, text="Close", command=self.destroy).pack(side='right', padx=20)

    def apply_changes(self):
        # If validate_changes() rise a flag, returns.
        if not self.validate_changes():
            return
        
        self.settings.set("language", self.language_var.get())
        self.settings.set("32'b_format", self.output_format.get())
        self.settings.set("dark_mode", self.dark_mode.get())
        self.settings.set("clean_input", self.clean_input.get())
        self.settings.set("clean_output", self.clean_output.get())
        self.settings.set("accumulate_results", self.accumulate_results.get())
        self.settings.set("truncate_binaries", self.truncate_binaries.get())
        
        self.settings.save()
        self.on_apply()
        self.change_language()
        self.destroy()
        
    def apply_language(self):
        language = self.settings.get("language")
        
        from resources.translations import translations

        tr = translations[language]
        
    def validate_changes(self):
        if not self.clean_input.get() and not self.clean_output.get():
            messagebox.showerror("Invalid configuration", 
                                "At least one of 'Clean input' or 'Clean output' must be selected.",
                                parent=self)                    
            return False
   
        if self.dark_mode.get() == True:
            messagebox.showinfo("Working on this, wait for it!", "Dark mode not available", parent=self)
            self.dark_mode.set(False)
            return False
            
        if self.truncate_binaries.get() == False:
            messagebox.showinfo("Permission required", "Administrator privileges are required", parent=self)
            self.truncate_binaries.set(True)
            return False
            
        return True
