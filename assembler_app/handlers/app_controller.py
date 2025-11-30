import tkinter as tk
from resources import TRANSLATIONS
from core import AssemblerController, IOController, SettingsManager
from gui import init_styles, MainWindow

class ApplicationController:
    def __init__(self):
        self.root = tk.Tk()
        self.settings = SettingsManager()
        
        self.current_language = None
        self.language_dictionary = None
        
        self._configure_window()
        self._load_language()
        self._init_controllers()
        self._init_gui()

    # ----- Internal Methods ----- #
    def _configure_window(self):
        self.root.geometry("700x580")

    def _load_language(self):
        self.current_language = self.settings.get("language")
        self.language_dictionary = TRANSLATIONS[self.current_language]
        self.root.title(self.language_dictionary["app_title"])    
   
    def _init_controllers(self):
        self.assembler_controller = AssemblerController(
            None, None, self.settings, self.language_dictionary
        )
        
        self.io_controller = IOController(
            None, None, self.language_dictionary
        )
   
    def _init_gui(self):
        init_styles()
        
        self.main_window = MainWindow(
            self.root, 
            self.language_dictionary, 
            self.io_controller, 
            self.assembler_controller, 
            self.settings, 
            self.refresh_language
        )

    # ----- Public Methods ----- #
    def refresh_language(self):
        new_language = self.settings.get("language")
        
        if self.current_language == new_language: 
            return
        
        self.current_language = new_language
        self.language_dictionary = TRANSLATIONS[self.current_language]
        
        self.root.title(self.language_dictionary["app_title"])
        self.assembler_controller.apply_language(self.language_dictionary)
        self.io_controller.apply_language(self.language_dictionary)
        self.main_window.apply_language(self.language_dictionary)
  
    def run(self):
        self.root.mainloop()