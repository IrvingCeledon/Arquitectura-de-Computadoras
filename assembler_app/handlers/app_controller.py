import tkinter as tk
from gui.styles import init_styles
from gui.main_window import MainWindow
from core.assembler_controller import AssemblerController
from core.io_controller import IOController
from core.settings_manager import SettingsManager
from resources.translations import translations

class ApplicationController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Assembler to Binary")
        self.root.geometry("700x580")
        
        self.settings = SettingsManager()
        self.assembler_controller = AssemblerController(None, None, self.settings)
        self.io_controller = IOController(None, None)
        init_styles()
        self.main_window = MainWindow(self.root, self.assembler_controller, self.io_controller, self.settings, self.set_language)
        
        self.set_language()

    def run(self):
        self.root.mainloop()

    # Consider making a get_language function.
    def set_language(self):
        language = self.settings.get("language")
        
        if language == "English": return
        
        tr = translations[language]
        self.root.title(tr["app_title"])
        self.main_window.apply_language(tr)
