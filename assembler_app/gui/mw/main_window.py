import tkinter as tk
from .main_window_ui import MainWindowUI
from .main_window_actions import MainWindowActions

class MainWindow:
    def __init__(self, root, language_dictionary, io_controller, assembler_controller, settings_manager, change_language):
        self.root = root
        self.tr = language_dictionary
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
        
        self.ui = MainWindowUI(self.main_frame, self.tr)
        
        self.actions = MainWindowActions(
            self.root,
            self.tr,
            self.ui,
            io_controller=io_controller,
            assembler_controller=assembler_controller,
            settings_manager=settings_manager,
            change_language=change_language
        )
        
        self.actions.bind_widgets()

    def apply_language(self, new_tr):
        self.tr = new_tr
        
        self.ui.apply_language(self.tr)
        self.actions.apply_language(self.tr)