import tkinter as tk


def salirPrograma(ventana):
    ventana.quit()
def insertarCliente(ventana):  
    print("Insertar cliente") 
def listarCliente(ventana):  
    print("listar todos los clientes") 
          

def mostrarMenu(ventana):
        barra_menu = tk.Menu(ventana)#crear barra de menu
        menu_archivo = tk.Menu(barra_menu, tearoff=0)#tearoff es para que no se permitan mover o desgarrar los menus
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)#Annadir opciones a la barra de menu
        menu_archivo.add_command(label="Salir",
                                 command=lambda: salirPrograma(ventana))#Annadir comandos al menu... tiene que ser una lambda para que permita annadir parametros
        
        menu_ayuda= tk.Menu(barra_menu,tearoff=0)
        menu_ayuda.add_command(label="Acerca de ...")
        barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)#Annadir opciones a la barra de menu

        menu_cliente= tk.Menu(barra_menu,tearoff=0)
        menu_cliente.add_command(label="Insertar un cliente", 
                                 command =lambda:insertarCliente(ventana))
        menu_cliente.add_command(label="Listar clientes", 
                                 command =lambda:listarCliente(ventana))
        barra_menu.add_cascade(label="Cliente", menu=menu_cliente)
        
        ventana.config(menu=barra_menu)