import tkinter as tk 
import os 

def create_folder(name):
 path_folder= os.mkdir(name)
root = tk.Tk()
root.title("crear carpeta")
root.geometry("350x350")
name_folder =tk.Label(root,text="nombre de la carpeta ")
text_name_folder = tk.StringVar()
entry_name_folder=tk.Entry(root, textvariable=text_name_folder)

name_folder.grid(colum=0,row=0)
entry_name_folder.grid(colum=1,row=0)
button = tk.Button(root,text="crear", command=lambda: create_folder(entry_name_folder.get))
button.grid(colum=0,row=1) 


root.mainloop()