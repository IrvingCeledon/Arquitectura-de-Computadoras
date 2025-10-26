# settings.py
import tkinter as tk
from tkinter import ttk, messagebox

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        self.geometry("400x250")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")

        # --- Widgets ---
        tk.Label(self, text="Settings", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

        # Fuente del texto
        tk.Label(self, text="Font:", bg="#f0f0f0").pack(anchor='w', padx=20)
        self.font_var = tk.StringVar(value="Consolas")
        font_entry = ttk.Entry(self, textvariable=self.font_var, width=30)
        font_entry.pack(padx=20, pady=5, fill='x')

        # Tamaño del texto
        tk.Label(self, text="Font size:", bg="#f0f0f0").pack(anchor='w', padx=20)
        self.font_size = tk.IntVar(value=11)
        ttk.Spinbox(self, from_=8, to=30, textvariable=self.font_size, width=5).pack(padx=20, pady=5, anchor='w')

        # Modo oscuro
        self.dark_mode = tk.BooleanVar(value=False)
        ttk.Checkbutton(self, text="Enable dark mode", variable=self.dark_mode).pack(pady=10)

        # --- Botones ---
        button_frame = tk.Frame(self, bg="#f0f0f0")
        button_frame.pack(pady=15, fill='x')
        ttk.Button(button_frame, text="Apply", command=self.apply_changes).pack(side='left', padx=20)
        ttk.Button(button_frame, text="Close", command=self.destroy).pack(side='right', padx=20)

    def apply_changes(self):
        """Aquí puedes integrar la lógica de actualización."""
        font = self.font_var.get()
        size = self.font_size.get()
        dark = self.dark_mode.get()

        messagebox.showinfo(
            "Settings saved",
            f"Font: {font}\nSize: {size}\nDark mode: {'On' if dark else 'Off'}"
        )

        # Ejemplo: podrías enviar estos valores a un controlador global
        # o guardarlos en un archivo de configuración .ini o .json.

