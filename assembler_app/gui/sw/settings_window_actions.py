import tkinter as tk
from resources import TRANSLATIONS

class SettingsWindowActions:
    def __init__(self, ui, language_dictionary, settings_manager, on_apply, change_language):
        self.ui = ui
        self.tr = language_dictionary
        self.settings = settings_manager
        self.on_apply = on_apply
        self.change_language = change_language

        self._extract_widgets()
        self._load_initial_values()
        self._bind_events()
   
    def _extract_widgets(self):
        widgets = self.ui.get_widgets()

        self.language_box   = widgets["language"]
        self.dark_mode      = widgets["dark_mode"]
        self.bit_format     = widgets["bit_format"]
        self.clean_input    = widgets["clean_input"]
        self.clean_output   = widgets["clean_output"]
        self.accumulate     = widgets["accumulate"]
        self.truncate       = widgets["truncate"]
        self.close_btn      = widgets["close"]
    
    def _load_initial_values(self):
        self._language_setup()
        self._boolean_settings()
   
    def _language_setup(self):
        self.languages_model = [ ("en_US", self.tr["en_US"]), ("es_MX", self.tr["es_MX"]) ]

        visible_values = [text for _, text in self.languages_model]
        self.language_box["values"] = visible_values

        current_language = self.settings.get("language")

        for i, (code, _) in enumerate(self.languages_model):
            if code == current_language:
                self.language_box.current(i)
                break
    
    def _boolean_settings(self):         
        self.dark_mode_var = tk.BooleanVar(value=self.settings.get("dark_mode"))
        self.dark_mode.config(variable=self.dark_mode_var)

        self.bit_format_var = tk.BooleanVar(value=self.settings.get("32'b_format"))
        self.bit_format.config(variable=self.bit_format_var)

        self.clean_input_var = tk.BooleanVar(value=self.settings.get("clean_input"))
        self.clean_input.config(variable=self.clean_input_var)

        self.clean_output_var = tk.BooleanVar(value=self.settings.get("clean_output"))
        self.clean_output.config(variable=self.clean_output_var)

        self.accumulate_var = tk.BooleanVar(value=self.settings.get("accumulate_results"))
        self.accumulate.config(variable=self.accumulate_var)

        self.truncate_var = tk.BooleanVar(value=self.settings.get("truncate_binaries"))
        self.truncate.config(variable=self.truncate_var)
  
    def _bind_events(self):
        self.language_box.bind("<<ComboboxSelected>>", self._on_language_selected)
        self.close_btn.config(command=self.apply_changes)
   
    def _on_language_selected(self, event=None):
        index = self.language_box.current()
        language_code = self.languages_model[index][0]

        # Update settings data
        self.settings.set("language", language_code)

        # Notify AppController so MainWindowUI elements updates
        self.change_language()

        # Reload translations
        new_tr = TRANSLATIONS[language_code]
        self.tr = new_tr

        # Apply translation to SettingsWindowUI
        self.ui.apply_language(new_tr)

        # Updates combobox visible text
        visible = [new_tr[code] for code, _ in self.languages_model]
        self.language_box["values"] = visible

        # Restore current selection
        self.language_box.current(index)
    
        self.language_box.current(index)  

    def apply_changes(self):
        if not self._validate_changes():
            return

        index = self.language_box.current()
        selected_language = self.languages_model[index][0]
        self.settings.set("language", selected_language)

        self.settings.set("32'b_format", self.bit_format_var.get())
        self.settings.set("dark_mode", self.dark_mode_var.get())
        self.settings.set("clean_input", self.clean_input_var.get())
        self.settings.set("clean_output", self.clean_output_var.get())
        self.settings.set("accumulate_results", self.accumulate_var.get())
        self.settings.set("truncate_binaries", self.truncate_var.get())

        self.settings.save()

        if self.on_apply:
            self.on_apply()

        self.ui.get_parent().destroy()    
   
    def _validate_changes(self):
        if not self.clean_input_var.get() and not self.clean_output_var.get():
            self.ui.show_error( self.tr["invalid_config_title"], self.tr["invalid_config_message"] )
            return False

        if self.dark_mode_var.get():
            self.ui.show_info( self.tr["info_dark_mode_title"], self.tr["info_dark_mode_message"] )
            self.dark_mode_var.set(False)
            return False

        if not self.truncate_var.get():
            self.ui.show_info( self.tr["perm_required_title"], self.tr["perm_required_message"] )
            self.truncate_var.set(True)
            return False

        return True  