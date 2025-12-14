from tkinter import *
from tkinter import messagebox

def saludar():
    nombre = txt_nombre.get()
    print(f"Hola, {nombre}!")
    messagebox.showinfo("Saludo", f"Hola, {nombre}!")
    
#creamos un objeto de la clase Tk
app = Tk()
#titulo de la ventana
app.title("Registro Alumnos")
# dimensiones de la ventana 
app.geometry("300x200")

#crear un objeto frame
frame = Frame(app)
frame.grid(row=0,column=0,padx=30,pady=30)

#crear una etiqueta (label) dentro del frame
lb_nombre = Label(frame,text="Nombre :")
lb_nombre.grid(row=0,column=0)
#crear una caja de texto (entry) dentro del frame
txt_nombre = Entry(frame)
txt_nombre.grid(row=0,column=1)
#crear una etiqueta (label) dentro del frame
lb_email = Label(frame,text="Email :")
lb_email.grid(row=1,column=0)
#crear una caja de texto (entry) dentro del frame
txt_email = Entry(frame)
txt_email.grid(row=1,column=1)
#crear un botón (button) dentro del frame
btn_saludar = Button(frame,text="Saludar",command=saludar)
btn_saludar.grid(row=5,column=1)

#mostramos la ventana
app.mainloop()
