import tkinter as tk
from tkinter import messagebox
import random
from gui import SettingsWindow

class MainWindowActions:
    def __init__(self, root, language_dictionary, ui, io_controller, assembler_controller, settings_manager, change_language):
        self.root = root
        self.tr = language_dictionary
        self.ui = ui
        self.io = io_controller
        self.assembler = assembler_controller
        self.settings = settings_manager
        self.settings_window = None
        self.change_language = change_language
        
        self.input_container = self.ui.get_text_input()
        self.output_container = self.ui.get_text_output()

    def bind_widgets(self):
        self.assembler.set_text_containers(self.input_container, self.output_container)
        self.io.set_text_containers(self.input_container, self.output_container)
        self._bind_buttons()

    def _bind_buttons(self):
        btns = self.ui.get_buttons()

        btns["load"].config(command=self.io.on_load)
        btns["convert"].config(command=self.assembler.on_convert)
        btns["generator"].config(command=self.on_generator)
        btns["copy"].config(command=self.on_copy)
        btns["save"].config(command=self.io.on_save)
        btns["clear"].config(command=self.on_clear)
        btns["exit"].config(command=self.root.destroy)
        btns["settings"].config(command=self.open_settings)

    # ----------------- ACTIONS -----------------  
    # Provisional
    def on_generator(self):
        data_size = self.input_container.get("1.0", tk.END).strip()

        self.output_container.config(state='normal')
        
        if not data_size.isdigit():
            self.output_container.insert("1.0", self.tr["not_integer_flag"])
            return

        n = int(data_size)

        list = random.sample(range(1, n + 1), n)

        text = "\n".join(str(x) for x in list)

        self.output_container.delete("1.0", tk.END)
        self.output_container.insert(tk.END, text)   
        self.output_container.config(state='disabled')   
        
    def on_copy(self):
        bin_output = self.output_container.get("1.0", tk.END).strip()
        
        if not bin_output:
            messagebox.showinfo(self.tr["empty_output_title"], self.tr["empty_output_message"])
            return
            
        self.root.clipboard_clear()
        self.root.clipboard_append(bin_output)
        messagebox.showinfo(self.tr["copied_title"], self.tr["copied_message"])

    def on_clear(self):
        input_empty = not self.input_container.get("1.0", tk.END).strip()
        output_empty = not self.output_container.get("1.0", tk.END).strip()
        
        have_to_clean_input = self.settings.get("clean_input")
        have_to_clean_output = self.settings.get("clean_output")
        have_to_clean_all = have_to_clean_input and have_to_clean_output

        if have_to_clean_all and input_empty and output_empty:
            self._show_info(self.tr["nothing_to_clear_title"], self.tr["nothing_to_clear_message"])
            return
        elif not have_to_clean_all and have_to_clean_input and input_empty:
            self._show_info(self.tr["cannot_clean_input_title"], self.tr["cannot_clean_input_message"])
            return
        elif not have_to_clean_all and have_to_clean_output and output_empty:
            self._show_info(self.tr["cannot_clean_output_title"], self.tr["cannot_clean_output_message"])
            return            
        
        if have_to_clean_input:
            self.input_container.delete("1.0", tk.END)
        if have_to_clean_output:
            self._clear_output()
   
    # Candidate to a Utils class        
    def _show_info(self, msg_title, msg):
        messagebox.showinfo(msg_title, msg)

    def _clear_output(self):
            self.output_container.config(state='normal')
            self.output_container.delete("1.0", tk.END)
            self.output_container.config(state='disabled')

    def open_settings(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = SettingsWindow(
                self.root, 
                self.tr, 
                self.settings, 
                self.apply_settings_changes, 
                self.change_language
            )
            
            # To control destruction
            # self.settings_window.protocol("WM_DELETE_WINDOW", self.close_settings_window)
        else:
        # Exists? -> focus
            # self.settings_window.lift()
            self.settings_window.focus_force()

    # Prints log in terminal, i will follow this structure to make a "log error output".
    def apply_settings_changes(self):
        print("Settings applied:", self.settings.data)

    def apply_language(self, new_tr):
        self.tr = new_tr

"""        
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

Idea for a utils method
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
"""