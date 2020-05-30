from tkinter import ttk
from tkinter import *

class Operaciones:

    #iniciamos la clase y le indicamos que debe de traer una ventana para poder iniciar
    def __init__(self, window):

        #valor de de ancho y alto de la ventana
        ancho = 800
        alto = 300

        self.wind = window
        self.wind.geometry(str(ancho)+'x'+str(alto))
        self.wind.columnconfigure(0, weight=1)
        self.wind.title('Aplicacion para sumar 2 o numeros by Ing. Gerson Altamirano')

        #Creamos el contenedor de la aplicación
        frame = LabelFrame(self.wind, text = 'Sumar 2 valores')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #nombramos la etiqueta del 1er input
        Label(frame, text = 'primer numero: ').grid(row = 0, column = 0)
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 0, column = 1)

        #nombramos la etiqueta del 2ndo input
        Label(frame, text = 'segundo numero: ').grid(row = 1, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 1, column = 1)

        #Creamos el boton para ejecutar la función
        ttk.Button(frame, text = 'Sumar', command = self.sumar).grid(row = 2, columnspan = 2, sticky = W + E )

        #label donde veremos el resultado
        self.resultado = Label(self.wind, text = '', fg = 'red')
        self.resultado.grid(row = 1, column = 0, columnspan = 2, sticky = W + E)

    #las funciones que vamos a utilizar dentro de la ventana tienen que estar al mismo nivel que la función donde inicializamos la clase

    #definimos o creamos la Función para validar si los inputs tienen datos
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0
    
    #definimos o creamos la función que ejecutamos al llamarla con command
    def sumar(self):
        if self.validation():
            resultado = float( self.var1.get() ) + float( self.var2.get() )
            self.resultado['text'] = 'La suma de las 2 variables es: {}'.format(resultado)
        else:
            self.resultado['text'] = 'los campos son requeridos'

#comprobamos si es el archivo principal
if __name__ == '__main__':
    #si la comprobovación de ventana principal es verdadero entonces 
    #entonces ejecutamos TK y lo guardamos en una ventana (window), que es la ventana principal de la aplicación
    window = Tk()

    # ejecutamos la clase Operaciones y llamamos la ventada dentro de la clase
    #guardamos la clase operaciones dentro de una varible para obtener los datos que pueda devolver
    ope = Operaciones(window)

    #ejecutamos o inicializamos la ventana
    window.mainloop()