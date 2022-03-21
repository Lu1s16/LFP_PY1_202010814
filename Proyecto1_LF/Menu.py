
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from Analizador import *
from Reporte_errores import *
from Reporte_tokens import *
from Formulario import *
import os



def Analizar():
    print("Analizando texto")
    contenido_total = texto1.get("1.0", "end")

    t = Analizador()
    f = Formulario()
    EstaVacio = t.analisis(contenido_total)

    if EstaVacio:
        f.Crear(contenido_total)
        print("ya")
        
    
    else:
        messagebox.showinfo(message="Hay errores lexicos", title="Error")
   
    
    
   
  

def Cargar_archivo():
    global contenido_total
    print("elija archivo")
    ruta = askopenfilename()

    if ".form" in ruta:
        print("archivo correcto")
        archivo = open(ruta, 'r')  #abre y r lee el archivo
        contenido = archivo.read()
        archivo.close()
        
        texto1.insert(INSERT, contenido)
        
    else:
        
        #cuadro de dialogo
        messagebox.showinfo(message="Archivo incorrecto", title="Error")


#para ejecutar las opciones del combobox
def op(event):
    
    

    if opciones.get() == "Reporte de tokens":
        print("Generando reporte de tokens")
        contenido_total = texto1.get("1.0", "end")
        r = Reporte_tokens()
        r.analisis(contenido_total)
        r.html_tokens()

        
        
    
    elif opciones.get() == "Reporte de errores":
        print("Generando reporte de errores")
        contenido_total = texto1.get("1.0", "end")
        x = Reporte_Errores()
        x.analisis(contenido_total)
        x.html_Errores()

        
    
    elif opciones.get() == "Manual de usuario":
        print("Mostrando manual de usuario")
        os.path.abspath('.')
        startfile("MANUAL DE USUARIO.pdf")
        print("manual mostrado")
    
    elif opciones.get() == "Manual tecnico":
        print("Mostrando manual tecnico")
        os.path.abspath('.')
        startfile("MANUAL TECNICO.pdf")
    
    

if __name__ == '__main__':

    


    #Se crea ventana
    ventana = Tk()
    ventana.title("Menu principal")
    ventana.resizable(0, 0)
    ventana['bg'] = '#D32D2D'
    ventana.geometry("1000x640")
    
    #textbox para mostrar contenido de archivo
    texto1 = Text(ventana, height=30, width=80, state=NORMAL)
    texto1.place(x=50, y=80)
    texto1.config(font=("ventana", 12))

    #Label
    label1 = Label(ventana, text="MENU")
    label1.place(x=50, y=20)
    label1.configure(bg='#D32D2D')
    label1.config(font=("verdana", 20))

    #boton para analizar texto
    boton1 = Button(ventana, height=3, width=15, text="Analizar", command=Analizar)
    boton1.place(x=800, y=90)
    boton1['bg'] = '#FFFA69'
    boton1.config(font=("verdana", 12))

    #boton para cargar archivo
    boton2 = Button(ventana, height=3, width=15, text="Cargar archivo", command=Cargar_archivo)
    boton2.place(x=800, y=180)
    boton2['bg'] = '#FFFA69'
    boton2.config(font=("verdana", 12))

    
    #combobox para diferentes opciones
    opciones = Combobox(ventana, heigh=30, width=25, values=["Reporte de tokens", "Reporte de errores", "Manual de usuario", "Manual tecnico"], state="readonly")
    opciones.place(x=800, y=270)
    
    opciones.bind("<<ComboboxSelected>>", op)

    ventana.mainloop()