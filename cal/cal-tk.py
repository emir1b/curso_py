#-*- coding:utf-8 -*-

import tkinter as tk
from tkinter import ttk
def calculadora():
    n1=float(entry_num1.get())
    n2=float(entry_num2.get())
    op=entry_op.get()
    r = eval(f"{n1}+{op}+{n2}")
    Label_result.configuret(f"result:´{r}")
    print(n1)
    print(n2)



#crear ventana
root = tk.Tk()
root.minsize(500,300)

#elements

#label
label_title=tk.Label(root,text="calculadora")

#texbax caja de texto 
text_num1=tk.StringVar()
text_num2=tk.StringVar()
text_op=tk.StringVar()


#Entry
entry_num1=tk.Entry(root,width=20,textvariable=text_num1)
entry_num2=tk.Entry(root,width=20,textvariable=text_num2)
entry_op=tk.Entry(root,width=20,textvariable=text_op)
#bt
button=tk.Button(root,text="calcular",command=calculadora)


#positions
label_title.grid(column=0,row=0)
entry_num1.grid(column=1,row=1)
entry_num2.grid(column=1,row=2)
button.grid(column=4,row=5)
entry_op.grid(column=0,row=0)

#iniciar ventana 
root.mainloop()