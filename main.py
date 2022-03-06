import pandas
from dataGenerator import DataGenerator,FileManager
import sqlite3



from tkinter import ttk

import tkinter as tk

import sqlite3

#carga los datos desde sqlite 
#       name: nombre de la tabla
#       tree: tabla en interfaz donde cargara los datos 
def LoadData(name,tree):

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(name))
    rows = cur.fetchall()    

    for row in rows:
        tree.insert("", tk.END, values=row)        

    conn.close()

#Intanciando el generador de datos 
dg = DataGenerator()
dg.createData()

#Guardando los datos en los archivos sqlite y json
FileManager().save_to_json(dg.data)
FileManager().save_to_sqlite(dg.data)
FileManager().save_to_sqlite(dg.metrics,"metrics")




root = tk.Tk()

#Creación de tabla de paises en interfaz
tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5"), show='headings')

tree.column("1", anchor=tk.CENTER)
tree.heading("1", text="Region")

tree.column("2", anchor=tk.CENTER)
tree.heading("2", text="Country Name")

tree.column("3", anchor=tk.CENTER)
tree.heading("3", text="Language")

tree.column("4", anchor=tk.CENTER)
tree.heading("4", text="Time (MS)")

tree.pack()
button1 = tk.Button(text="Cargar Paises", command= lambda: LoadData("data",tree))
button1.pack(pady=10)


#tabla de metricas
tree2 = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5"), show='headings', height=1)

tree2.column("1", anchor=tk.CENTER)
tree2.heading("1", text="Total (ms)")

tree2.column("2", anchor=tk.CENTER)
tree2.heading("2", text="Maximo (ms)")

tree2.column("3", anchor=tk.CENTER)
tree2.heading("3", text="Minimo (ms)")

tree2.column("4", anchor=tk.CENTER)
tree2.heading("4", text="Promedio (ms)")

tree2.pack()
button2 = tk.Button(text="Cargar metricas", command= lambda: LoadData("metrics",tree2))
button2.pack(pady=10)
root.mainloop()