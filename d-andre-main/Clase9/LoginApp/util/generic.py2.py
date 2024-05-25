def leer_imagen(path, size):
    from PIL import ImageTk, Image

    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))

def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    ventana.update_idletasks()  # Update the window to get correct winfo_width() and winfo_height()
    ventana_ancho = ventana.winfo_width()
    ventana_largo = ventana.winfo_height()

    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()

    x = int((pantall_ancho / 2) - (ventana_ancho / 2))
    y = int((pantall_largo / 2) - (ventana_largo / 2))

    ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")
