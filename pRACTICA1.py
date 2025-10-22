import tkinter as tk


ventana = tk.Tk()
ventana.title("Inicio de sesion")
ventana.geometry("300x500")
ventana.resizable(False,False)



usuario_correcto = "Mesi"
clave_correcta = "holasoymessi12345"


etiqueta_usuario = tk.Label(ventana, text="usuario:")
etiqueta_usuario.pack()
ingreso_usuario = tk.Entry(ventana)
ingreso_usuario.pack()


etiqueta_contraseña = tk.Label(ventana, text="contraseña:")
etiqueta_contraseña.pack()
ingreso_contraseña = tk.Entry(ventana)
ingreso_contraseña.pack()


def iniciar_sesion():
    Usuario = ingreso_usuario.get()
    contrasenia = ingreso_contraseña.get()
    if Usuario == usuario_correcto and contrasenia == clave_correcta:
        etiqueta_resultado.config(text="Inicio sesion exitosamente.",fg= "green")
    else:
        etiqueta_resultado.config(text="usuario o contraseña incorrectos.", fg="red")


boton = tk.Button(ventana, text = "iniciar sesion", bg = "sky blue", command = iniciar_sesion)
boton.pack()


etiqueta_resultado = tk.Label(ventana)
etiqueta_resultado.pack()


ventana.mainloop()

