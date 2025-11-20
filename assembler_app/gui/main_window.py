import tkinter as tk
from tkinter import scrolledtext, messagebox
from gui.widgets_factory import create_button, create_frames
from . settings_window import SettingsWindow

class MainWindow:
    def __init__(self, root, assembler_controller, io_controller, settings_manager, set_language):
        self.root = root
        self.settings = settings_manager    
        self.settings_window = None
        self.assembler_controller = assembler_controller
        self.io_controller = io_controller
        self.change_language = set_language
        
        self.init_io_containers()
        
        # Set containers to controllers
        self.assembler_controller.set_text_containers(self.text_input, self.text_output)
        self.io_controller.set_text_containers(self.text_input, self.text_output)
        
        self.init_input_buttons()
        self.init_output_buttons()

    def init_io_containers(self):
        self.input_label = tk.Label(self.root, text="Assembler input:")
        self.input_label.pack(anchor='w', padx=10)
        
        self.text_input = scrolledtext.ScrolledText(self.root, height=8, width=70, font=("Consolas", 11))
        self.text_input.pack(padx=10, pady=5, fill='both', expand=True)    
        
        self.input_frame  = create_frames(self.root, 5, 'x', 2) # Declare this here just for aesthetic purposes.

        self.output_label = tk.Label(self.root, text="Binary output:")
        self.output_label.pack(anchor='w', padx=10)
        self.text_output = scrolledtext.ScrolledText(self.root, height=8, width=70, font=("Consolas", 11), state='disabled')
        self.text_output.pack(padx=10, pady=5, fill='both', expand=True)                
     
    def init_input_buttons(self): 
        self.load_from_file_button = create_button(self.input_frame, "Load from file", self.io_controller.on_load)
        self.load_from_file_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.convert_button = create_button(self.input_frame, "Convert", self.assembler_controller.on_convert)
        self.convert_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    
    def init_output_buttons(self): 
        self.output_frame  = create_frames(self.root, pady_value=5, fill_value='x', range_size=2)
        
        # Same row
        self.copy_to_clipboard_button = create_button(self.output_frame, "Copy to clipboard", self.on_copy)
        self.copy_to_clipboard_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.save_as_txt_button = create_button(self.output_frame, "Save as .txt", self.io_controller.on_save)
        self.save_as_txt_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        self.clear_button = create_button(self.output_frame, "Clear", self.on_clear)
        self.clear_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
         
        # Different row
        self.exit_button = create_button(self.output_frame, "Exit", self.root.destroy)
        self.exit_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
        
        self.settings_button = create_button(self.output_frame, "Settings", self.open_settings)
        self.settings_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
        
    def on_copy(self):
        bin_output = self.text_output.get("1.0", tk.END).strip()
        
        if not bin_output:
            messagebox.showinfo("Empty fields", "There is nothing to copy.")
            return
            
        self.root.clipboard_clear()
        self.root.clipboard_append(bin_output)
        messagebox.showinfo("Copied", "The result has been copied to clipboard.")
        
    def on_clear(self):
        input_text = self.text_input.get("1.0", tk.END).strip()
        output_text = self.text_output.get("1.0", tk.END).strip()
        
        if not input_text and not output_text:
            messagebox.showinfo("Nothing to clear", "input and output are already empty.")
            return
        
        # Unifying these two conditions is more problematic than keeping them separate.
        if self.settings.get("clean_input"):
            self.text_input.delete("1.0", tk.END)
        
        if self.settings.get("clean_output"):
            self.text_output.config(state='normal')
            self.text_output.delete("1.0", tk.END)
            self.text_output.config(state='disabled')
        
    def open_settings(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = SettingsWindow(self.root, self.settings, self.apply_settings_changes, self.change_language)
            
            # To control destruction
            # self.settings_window.protocol("WM_DELETE_WINDOW", self.close_settings_window)
        else:
        # Exists? -> focus
            self.settings_window.lift()
            self.settings_window.focus_force()

    # Prints log in terminal, i will follow this structure to make a "log error output".
    def apply_settings_changes(self):
        print("Settings applied:", self.settings.data)
        
    # tr = actual language dictionary
    def apply_language(self, tr):
        self.input_label.config(text=tr["input_label"])
        self.load_from_file_button.config(text=tr["load_button"])
        self.convert_button.config(text=tr["convert_button"])
        self.output_label.config(text=tr["output_label"])
        self.copy_to_clipboard_button.config(text=tr["copy_to_clipboard_button"])
        self.save_as_txt_button.config(text=tr["save_as_txt_button"])
        self.clear_button.config(text=tr["clear_button"])
        self.exit_button.config(text=tr["exit_button"])
        self.settings_button.config(text=tr["settings_button"])
