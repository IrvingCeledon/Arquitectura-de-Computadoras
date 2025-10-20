import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

def procesar_texto():
    entrada = entrada_texto.get("1.0", tk.END).strip()
    if not entrada:
        messagebox.showwarning("Advertencia", "El campo de entrada está vacío.")
        return

    try:
        campos = entrada.split('$')
        numeros = [int(p) for p in campos]
        binarios = [f"{n:08b}" for n in numeros]
        resultado = "\n".join(binarios)  # mostrar en líneas separadas
        global resultado_final
        resultado_final = "".join(binarios)  # sin espacios, para copiar o guardar

        salida_texto.config(state='normal')
        salida_texto.delete("1.0", tk.END)
        salida_texto.insert(tk.END, resultado)
        salida_texto.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Asegúrate de que todos los campos sean números enteros.")

def copiar_portapapeles():
    if not resultado_final:
        messagebox.showinfo("Info", "No hay resultado para copiar.")
        return
    ventana.clipboard_clear()
    ventana.clipboard_append(resultado_final)
    messagebox.showinfo("Copiado", "El resultado se copió al portapapeles.")

def guardar_como_txt():
    if not resultado_final:
        messagebox.showinfo("Info", "No hay resultado para guardar.")
        return
    ruta = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivo de texto", "*.txt")],
        title="Guardar resultado como..."
    )
    if ruta:
        with open(ruta, "w") as f:
            f.write(resultado_final)
        messagebox.showinfo("Guardado", f"Resultado guardado en:\n{ruta}")

# -----------------------
# Interfaz gráfica
# -----------------------
ventana = tk.Tk()
ventana.title("Procesador de entrada")
ventana.geometry("600x480")

resultado_final = ""

tk.Label(ventana, text="Entrada:").pack(anchor='w', padx=10)
entrada_texto = scrolledtext.ScrolledText(ventana, height=8, width=70, font=("Consolas", 11))
entrada_texto.pack(padx=10, pady=5, fill='both', expand=True)

tk.Button(ventana, text="Procesar", command=procesar_texto, font=("Arial", 11, "bold")).pack(pady=5)

tk.Label(ventana, text="Salida:").pack(anchor='w', padx=10)
salida_texto = scrolledtext.ScrolledText(ventana, height=8, width=70, font=("Consolas", 11), state='disabled')
salida_texto.pack(padx=10, pady=5, fill='both', expand=True)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)
tk.Button(frame_botones, text="Copiar al portapapeles", command=copiar_portapapeles).grid(row=0, column=0, padx=10)
tk.Button(frame_botones, text="Guardar como TXT", command=guardar_como_txt).grid(row=0, column=1, padx=10)

ventana.mainloop()
