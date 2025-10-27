import tkinter as tk
from gui.main_window import MainWindow
from core.assembler_controller import AssemblerController
from core.io_controller import IOController
from core.settings_manager import SettingsManager

class ApplicationController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Assembler to Binary")
        self.root.geometry("700x580")
        
        self.settings = SettingsManager()
        self.assembler_controller = AssemblerController(None, None, self.settings)
        self.io_controller = IOController(None, None)
        self.main_window = MainWindow(self.root, self.assembler_controller, self.io_controller, self.settings)

    def run(self):
        self.root.mainloop()
