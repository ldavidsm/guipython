import tkinter as tk
import time
import json


def panelInsertar (ventana):
    
    nombre_cliente=tk.StringVar()
    apellido_cliente=tk.StringVar()
    email_cliente=tk.StringVar()
    
    
    def guardadatos():
        print("Vamos a guardar los datos")
        nombre = nombre_cliente.get()
        apellidos = apellido_cliente.get()
        email = email_cliente.get()
        diccionario ={
        "nombre":nombre,
        "apellido":apellidos,
        "email":email
     }
        archivo = open("db/"+str(time.time())+".json", "w")
        json.dump(diccionario,archivo,indent=4)
        archivo.close()

    panel_insertar= tk.Frame(ventana)
    panel_insertar.pack()
    tk.Label(panel_insertar, text="Introduce el nombre del cliente").pack()
    tk.Entry(panel_insertar,
     textvariable= nombre_cliente).pack()
    tk.Label(panel_insertar, text="Introduce el apellido del cliente").pack()
    tk.Entry(panel_insertar,
     textvariable= apellido_cliente).pack()
    tk.Label(panel_insertar, text="Introduce el email del cliente").pack()
    tk.Entry(panel_insertar,
     textvariable= email_cliente).pack()
    tk.Button(
    panel_insertar, command=guardadatos, text="Enviar").pack()
    
    
    