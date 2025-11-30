import tkinter as tk
from tkinter import scrolledtext, messagebox
from gui import MainWindowUI, MainWindowActions

class MainWindow:
    def __init__(self, root, language_dictionary, io_controller, assembler_controller, settings_manager, change_language):
        self.root = root
        self.tr = language_dictionary
        
        self.ui = MainWindowUI(self.root, self.tr)
        self.actions = MainWindowActions(
            self.root,
            self.tr,
            self.ui,
            io_controller=io_controller,
            assembler_controller=assembler_controller,
            settings_manager=settings_manager,
            change_language=change_language
        )
        
        self.actions.bind_controllers()

    def apply_language(self, new_tr):
        self.tr = new_tr
        
        self.ui.apply_language(self.tr)
        self.actions.apply_language(self.tr)
