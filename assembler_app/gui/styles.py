from tkinter import ttk

_initialized = False

def init_styles():
    global _initialized
    
    if _initialized:
        return

    style = ttk.Style()
    print(style.theme_use())
    # style.theme_use("clam")
    print(style.theme_use())

    # style.configure("Main.TFrame", background="#f5f5f5")

    style.configure(
        "Generic.TButton",
        font=("Arial", 11, "bold")#,
        #padding=6
    )

    style.configure(
        "Main.TButton",
        font=("Arial", 11, "bold"),
        padding=8,
        foreground="white",
        background="#0078D7"
    )

    style.map(
        "Main.TButton",
        background=[("active", "#005A9E"), ("disabled", "#A0A0A0")]
    )

    _initialized = True
