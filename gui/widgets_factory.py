import tkinter as tk

def create_button(parent, text_field, fuction):
    return tk.Button(parent, text=text_field, command=fuction, font=("Arial", 11, "bold"))
    
def create_frames(parent, pady_value, fill_value, range_size):
    generic_frame = tk.Frame(parent)
    generic_frame.pack(pady=pady_value, fill=fill_value)
        
    for i in range(range_size):
        generic_frame.grid_columnconfigure(i, weight=1, uniform="btn")
       
    return generic_frame