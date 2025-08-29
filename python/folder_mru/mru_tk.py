import tkinter as tk
def calculadora():
    movil=float(entry_movil.get())
    tiempo=float(entry_tiempo.get())
    distancia=float(entry_tiempo.get())
    #op=entry_op.get()
    # r = eval(f"{movil}+{op}+{tiempo}")
    distancia=movil*tiempo
    Label_result.configure(text=f"result:´{distancia}")
   



#crear ventana
root = tk.Tk()
root.minsize(800,300)

#elements

#label
label_title=tk.Label(root,text="movil")
label_title=tk.Label(root,text="tiempo")
label_title=tk.Label(root,text="distancia")


label_result=tk.Label(root,text="distancia recorrida")

#texbax caja de texto 
text_movil=tk.StringVar()
text_tiempo=tk.StringVar()
text_distancia=tk.StringVar()

# text_op=tk.StringVar()


#Entry
entry_movil=tk.Entry(root,width=20,textvariable=text_movil)
entry_tiempo=tk.Entry(root,width=20,textvariable=text_tiempo)
entry_distancia=tk.Entry(root,width=20,textvariable=text_distancia)
# entry_op=tk.Entry(root,width=20,textvariable=text_op)
#bt
button=tk.Button(root,text="calcular",command=calculadora)


#positions
label_title.grid(column=0,row=0)
entry_movil.grid(column=3,row=2)
entry_tiempo.grid(column=3,row=4)
entry_distancia.grid(column=3,row=6)
button.grid(column=4,row=6)
label_result.grid(column=8,row=8)

# entry_op.grid(column=0,row=0)

#iniciar ventana 
root.mainloop()