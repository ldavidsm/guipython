import tkinter as tk

def panelBienvenida(ventana):
    panel_bienvenida = tk.Frame(ventana) #para crear un panel
    panel_bienvenida.pack() #(annadir el frame a la interfaz de usuario.. lp empaqueta)
    titulo = tk.Label(panel_bienvenida, text="Programa Luis David")
    titulo.pack(padx=50, pady=50) # crear margenes sobre el objeto