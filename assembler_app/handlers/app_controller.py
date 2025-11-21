import tkinter as tk
from gui.styles import init_styles
from gui.main_window import MainWindow
from core.assembler_controller import AssemblerController
from core.io_controller import IOController
from core.settings_manager import SettingsManager

class ApplicationController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x580")
        
        from resources.translations import translations
        
        self.settings = SettingsManager()
        self.current_language = self.settings.get("language")
        self.language_dictionary = translations[self.current_language]
        self.root.title(self.language_dictionary["app_title"])
        
        self.assembler_controller = AssemblerController(None, None, self.settings)
        self.io_controller = IOController(None, None, self.language_dictionary)
        init_styles()
        self.main_window = MainWindow(self.root, self.assembler_controller, self.io_controller, self.settings, self.language_dictionary, self.set_language)

    def run(self):
        self.root.mainloop()

    # Consider making a get_language function.
    def set_language(self):
        from resources.translations import translations
        
        if self.current_language == self.settings.get("language"): 
            return
        
        self.current_language = self.settings.get("language")
        self.language_dictionary = translations[self.current_language]
        
        self.root.title(self.language_dictionary["app_title"])
        self.main_window.apply_language(self.language_dictionary)
        self.io_controller.apply_language(self.language_dictionary)
