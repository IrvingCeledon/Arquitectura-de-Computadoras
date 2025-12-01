import tkinter as tk
from .settings_window_ui import SettingsWindowUI
from .settings_window_actions import SettingsWindowActions

class SettingsWindow(tk.Toplevel):
    def __init__(self, root, language_dictionary, settings_manager, on_apply, change_language):
        super().__init__(root)
        
        self.tr = language_dictionary
        
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)
        
        self.ui = SettingsWindowUI(self, self.main_frame, self.tr)
        
        self.actions = SettingsWindowActions(
            self.ui,
            self.tr,
            settings_manager=settings_manager, 
            on_apply=on_apply,
            change_language=change_language,
        )