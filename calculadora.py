from tkinter import *

ventana = Tk()
ventana.title("Calculadora PY")

i = 0;
#texto
e_texto = Entry(ventana, font=("Arial 15"))

#row -> definimos la fila // column -> definimos la columna
#columnspan -> columnas que ocupa (en este caso todas las que habrá)
#padx -> borde entre elemento y ventana en eje X
#pady -> borde entre elemento y ventana en eje Y
e_texto.grid(row=0,column=0, columnspan=4, padx=15 , pady=8)

#Funciones
def clicBoton(contenido):
    global i
    if i==0:
        e_texto.delete(0,END)
    e_texto.insert(i, contenido)
    i += 1 

def borrar():
    global i
    e_texto.delete(0,END)
    i=0

def calcular():
    global i
    resultado = eval(e_texto.get())
    i=0
    e_texto.delete(0,END)
    e_texto.insert(i,resultado)
    print(i)
    

#Botones
boton1 = Button(ventana, text="1", width=5,height=2, command=lambda: clicBoton(1))
boton2 = Button(ventana, text="2", width=5,height=2, command=lambda: clicBoton(2))
boton3 = Button(ventana, text="3", width=5,height=2, command=lambda: clicBoton(3))
boton4 = Button(ventana, text="4", width=5,height=2, command=lambda: clicBoton(4))
boton5 = Button(ventana, text="5", width=5,height=2, command=lambda: clicBoton(5))
boton6 = Button(ventana, text="6", width=5,height=2, command=lambda: clicBoton(6))
boton7 = Button(ventana, text="7", width=5,height=2, command=lambda: clicBoton(7))
boton8 = Button(ventana, text="8", width=5,height=2, command=lambda: clicBoton(8))
boton9 = Button(ventana, text="9", width=5,height=2, command=lambda: clicBoton(9))
boton0 = Button(ventana, text="0", width=13,height=2, command=lambda: clicBoton(0))

#Operaciones
botonSuma = Button(ventana, text="+", width=5,height=2, command=lambda: clicBoton("+"))
botonResta = Button(ventana, text="-", width=5,height=2, command=lambda: clicBoton("-"))
botonMul = Button(ventana, text="*", width=5,height=2, command=lambda: clicBoton("*"))
botonDiv = Button(ventana, text="/", width=5,height=2, command=lambda: clicBoton("/"))

#resultado - borrar
botonResult = Button(ventana, text="=", width=5,height=2, command=calcular)
botonDel = Button(ventana, text="AC", width=5,height=2, command=borrar)

#parentesis
botonParentesis1 = Button(ventana, text="(", width=5,height=2, command=lambda: clicBoton("("))
botonParentesis2 = Button(ventana, text=")", width=5,height=2, command=lambda: clicBoton(")"))

#decimal
botonPunto = Button(ventana, text=".", width=5,height=2, command=lambda: clicBoton("."))

#Añadir botones
botonDel.grid(row=1,column=0,padx=5,pady=5)
botonParentesis1.grid(row=1,column=1,padx=5,pady=5)
botonParentesis2.grid(row=1,column=2,padx=5,pady=5)
botonDiv.grid(row=1,column=3,padx=5,pady=5)

boton7.grid(row=2,column=0,padx=5,pady=5)
boton8.grid(row=2,column=1,padx=5,pady=5)
boton9.grid(row=2,column=2,padx=5,pady=5)
botonMul.grid(row=2,column=3,padx=5,pady=5)

boton4.grid(row=3,column=0,padx=5,pady=5)
boton5.grid(row=3,column=1,padx=5,pady=5)
boton6.grid(row=3,column=2,padx=5,pady=5)
botonResta.grid(row=3,column=3,padx=5,pady=5)

boton1.grid(row=4,column=0,padx=5,pady=5)
boton2.grid(row=4,column=1,padx=5,pady=5)
boton3.grid(row=4,column=2,padx=5,pady=5)
botonSuma.grid(row=4,column=3,padx=5,pady=5)

boton0.grid(row=5,column=0,padx=5,pady=5,columnspan=2)
botonPunto.grid(row=5,column=2,padx=5,pady=5)
botonResult.grid(row=5,column=3,padx=5,pady=5)

ventana.mainloop()