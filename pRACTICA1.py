import tkinter as tk


ventana = tk.Tk()
ventana.title("Inicio de sesion")
ventana.geometry("300x500")
ventana.resizable(False,False)


frame1 = tk.Frame(ventana, bg="pink", width=200, height=300,bd = 5)
frame1.pack(pady=20)


usuario_correcto = "Mesi"
clave_correcta = "holasoymessi12345"


etiqueta_usuario = tk.Label(frame1, text="usuario:",bg="pink")
etiqueta_usuario.pack(pady=10)
ingreso_usuario = tk.Entry(frame1)
ingreso_usuario.pack()

etiqueta_contraseña = tk.Label(frame1, text="contraseña:",bg="pink")
etiqueta_contraseña.pack()
ingreso_contraseña = tk.Entry(frame1)
ingreso_contraseña.pack()


def iniciar_sesion():
    Usuario = ingreso_usuario.get()
    contrasenia = ingreso_contraseña.get()
    if Usuario == usuario_correcto and contrasenia == clave_correcta:
        etiqueta_resultado.config(text="!Inicio sesion exitosamente¡.",fg= "green")
    else:
        etiqueta_resultado.config(text="usuario o contraseña incorrectos!.", fg="red")


boton = tk.Button(ventana, text = "iniciar sesion", bg = "sky blue", command = iniciar_sesion)
boton.pack()


etiqueta_resultado = tk.Label(ventana)
etiqueta_resultado.pack()


ventana.mainloop()

