from tkinter import ttk
 
def create_button(parent, text_field, function, style_name="Generic.TButton"):
    return ttk.Button(parent, text=text_field, command=function, style=style_name)

def create_frames(parent, pady_value, fill_value, range_size):
    generic_frame = ttk.Frame(parent)
    generic_frame.pack(pady=pady_value, fill=fill_value)
    
    for i in range(range_size):
        generic_frame.grid_columnconfigure(i, weight=1, uniform="btn")
        
    return generic_frame


