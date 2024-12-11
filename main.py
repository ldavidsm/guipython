import tkinter as tk    #(libreria para crear ventanas)
from menu import *
from insertar import *
from bienvenida import *
import json
import time
import os


def listadoClientes():
    print("todos los clientes")
    carpeta = "db"
    archivos = files =os.listdir(carpeta)
    for archivo in archivos :
        ventana_texto.insert(tk.END, archivo)

ventana = tk.Tk() #(Metodo de la libreria para crer ventana)
ventana.title("Programa de Luis David") #para asignarle titulo a la ventana
ventana.geometry("512x512") #para asignarle dimensiones a la ventana

mostrarMenu(ventana)
panelBienvenida(ventana)
panelInsertar(ventana)

marco_listado = tk.Frame(ventana)
marco_listado.pack()
tk .Button(marco_listado, text="Obtener Clientes", command=lambda: listadoClientes())

ventana_texto = tk.Text

ventana.mainloop()  #(para cerrar la ventana)
