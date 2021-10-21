
#from _typeshed import Self
from tkinter import * 
from tkinter import ttk

from tkinter.ttk import Combobox, Treeview


class Product:
    db_name = 'database.db' 
    def __init__(self,window):

        self.wind = window
        window.title('Pantalla Base')
        
        self.frame = LabelFrame(self.wind, text='Query de aduitoria')
        self.frame.grid(row= 0, column=0, columnspan=3, pady=20)

#nombre
        Label(self.frame, text ='MAC de camara: ').grid(row=1,column=0)
        self.nombre=Entry(self.frame)
        self.nombre.focus()
        self.nombre.grid(row=1, column=1)

#hora inicio
        Label(self.frame,text='hora inicio: ').grid(row=2,column=0)
        self.horaI=Entry(self.frame)
        self.horaI.grid(row=2,column=1)
        
#hora termino
        Label(self.frame,text='hora termino: ').grid(row=2,column=2)
        self.horaT = Entry(self.frame)
        self.horaT.grid(row=2, column=3)

#buscar BUTTON        
        B = Button(self.frame, text ="Buscar").grid(row=3,column=1)

        
#tabla de resultado
        self.tabla = Treeview(self.frame,columns=("#1"))
        self.tabla.grid(row=4  ,column=0,columnspan=4,sticky=W + E)
        self.tabla.heading('#0',text='Entrada')
        self.tabla.heading('#1',text='Salida')

'''
#esta funcion inicia y conecta la base de datos
    def run_query(self,query,parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result=cursor.execute(query, parameters)
            conn.commit()
            return result
'''
if __name__ == '__main__':
    window=Tk()
    applicaton=Product(window)
    window.mainloop()
