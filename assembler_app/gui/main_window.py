import tkinter as tk
from tkinter import scrolledtext, messagebox
from gui import create_button, create_frames, SettingsWindow

class MainWindow:
    def __init__(self, root, assembler_controller, io_controller, settings_manager, language_dictionary, change_language):
        self.root = root
        self.settings = settings_manager    
        self.settings_window = None
        self.assembler_controller = assembler_controller
        self.io_controller = io_controller
        self.tr = language_dictionary
        self.change_language = change_language
        
        self.init_io_containers()
        self.init_input_buttons()
        self.init_output_buttons()
        
        # Set containers to controllers
        self.assembler_controller.set_text_containers(self.text_input, self.text_output)
        self.io_controller.set_text_containers(self.text_input, self.text_output)
  
    # def _build_ui(self):
        
    # def _bind_controllers(self):

    def init_io_containers(self):
        self.input_lbl = tk.Label(self.root, text=self.tr["input_lbl"])
        self.input_lbl.pack(anchor='w', padx=10)
        
        self.text_input = scrolledtext.ScrolledText(self.root, height=8, width=70, font=("Consolas", 11))
        self.text_input.pack(padx=10, pady=5, fill='both', expand=True)    
        
        self.input_frame  = create_frames(self.root, 5, 'x', 2) # Declare this here just for aesthetic purposes.

        self.output_lbl = tk.Label(self.root, text=self.tr["output_lbl"])
        self.output_lbl.pack(anchor='w', padx=10)
        self.text_output = scrolledtext.ScrolledText(self.root, height=8, width=70, font=("Consolas", 11), state='disabled')
        self.text_output.pack(padx=10, pady=5, fill='both', expand=True)                
     
    def init_input_buttons(self): 
        self.load_from_file_btn = create_button(self.input_frame, self.tr["load_btn"], self.io_controller.on_load)
        self.load_from_file_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.convert_btn = create_button(self.input_frame, self.tr["convert_btn"], self.assembler_controller.on_convert)
        self.convert_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    
    def init_output_buttons(self): 
        self.output_frame  = create_frames(self.root, pady_value=5, fill_value='x', range_size=2)
        
        # Same row
        self.copy_to_clipboard_btn = create_button(self.output_frame, self.tr["copy_to_clipboard_btn"], self.on_copy)
        self.copy_to_clipboard_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        self.save_as_txt_btn = create_button(self.output_frame, self.tr["save_as_txt_btn"], self.io_controller.on_save)
        self.save_as_txt_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        self.clear_btn = create_button(self.output_frame, self.tr["clear_btn"], self.on_clear)
        self.clear_btn.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
         
        # Different row
        self.exit_btn = create_button(self.output_frame, self.tr["exit_btn"], self.root.destroy)
        self.exit_btn.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
        
        self.settings_btn = create_button(self.output_frame, self.tr["settings_btn"], self.open_settings)
        self.settings_btn.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
        
    def on_copy(self):
        bin_output = self.text_output.get("1.0", tk.END).strip()
        
        if not bin_output:
            messagebox.showinfo(self.tr["empty_output_title"], self.tr["empty_output_message"])
            return
            
        self.root.clipboard_clear()
        self.root.clipboard_append(bin_output)
        messagebox.showinfo(self.tr["copied_title"], self.tr["copied_message"])
        
    def on_clear(self):
        input_text = self.text_input.get("1.0", tk.END).strip()
        output_text = self.text_output.get("1.0", tk.END).strip()
        
        have_to_clean_input = self.settings.get("clean_input")
        have_to_clean_output = self.settings.get("clean_output")
        have_to_clean_all = have_to_clean_input and have_to_clean_output
        
        if not input_text and not output_text and have_to_clean_all:
            messagebox.showinfo(self.tr["nothing_to_clear_title"], self.tr["nothing_to_clear_message"])
            return
        elif not input_text and have_to_clean_input:
            messagebox.showinfo(self.tr["cannot_clean_input_title"], self.tr["cannot_clean_input_message"])
            return
        elif not output_text and have_to_clean_output:
            messagebox.showinfo(self.tr["cannot_clean_output_title"], self.tr["cannot_clean_output_message"])
            return            
        
        # Unifying these two conditions is more problematic than keeping them separate it.
        if have_to_clean_input:
            self.text_input.delete("1.0", tk.END)
        
        if have_to_clean_output:
            self.text_output.config(state='normal')
            self.text_output.delete("1.0", tk.END)
            self.text_output.config(state='disabled')
        
    def open_settings(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = SettingsWindow(self.root, self.settings, self.apply_settings_changes, self.tr, self.change_language)
            
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
    def apply_language(self, new_tr):
        self.tr = new_tr
        
        self.input_lbl.config(text=self.tr["input_lbl"])
        self.load_from_file_btn.config(text=self.tr["load_btn"])
        self.convert_btn.config(text=self.tr["convert_btn"])
        self.output_lbl.config(text=self.tr["output_lbl"])
        self.copy_to_clipboard_btn.config(text=self.tr["copy_to_clipboard_btn"])
        self.save_as_txt_btn.config(text=self.tr["save_as_txt_btn"])
        self.clear_btn.config(text=self.tr["clear_btn"])
        self.exit_btn.config(text=self.tr["exit_btn"])
        self.settings_btn.config(text=self.tr["settings_btn"])
