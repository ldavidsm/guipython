import tkinter as tk    #(libreria para crear ventanas)
from menu import *


ventana = tk.Tk() #(Metodo de la libreria para crer ventana)
ventana.title("Programa de Luis David") #para asignarle titulo a la ventana
ventana.geometry("512x512") #para asignarle dimensiones a la ventana

nombre_cliente=tk.StringVar()
apellido_cliente=tk.StringVar()
email_cliente=tk.StringVar()

mostrarMenu()

panel_bienvenida = tk.Frame(ventana) #para crear un panel
panel_bienvenida.pack() #(annadir el frame a la interfaz de usuario.. lp empaqueta)
titulo = tk.Label(panel_bienvenida, text="Programa Luis David")
titulo.pack(padx=50, pady=50) # crear margenes sobre el objeto

panel_insertar= tk.Frame(ventana)
panel_insertar.pack()
tk.label(panel_insertar, text="Introduce el nombre del cliente").pack()
tk.Entry(panel_insertar,
         textvariable= nombre_cliente).pack()
tk.label(panel_insertar, text="Introduce el apellido del cliente").pack()
tk.Entry(panel_insertar,
         textvariable= apellido_cliente).pack()
tk.label(panel_insertar, text="Introduce el email del cliente").pack()
tk.Entry(panel_insertar,
         textvariable= email_cliente).pack()


ventana.mainloop()  #(para cerrar la ventana)
