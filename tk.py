import tkinter as tk
def calculadora():
    movil=float(entry_movil.get())
    tiempo=float(entry_tiempo.get())
    #op=entry_op.get()
    # r = eval(f"{movil}+{op}+{tiempo}")
    Label_result.configuret(f"result:´{distancia}")
   



#crear ventana
root = tk.Tk()
root.minsize(500,300)

#elements

#label
label_title=tk.Label(root,text="calculadora")

#texbax caja de texto 
text_movil=tk.StringVar()
text_tiempo=tk.StringVar()
# text_op=tk.StringVar()


#Entry
entry_movil=tk.Entry(root,width=20,textvariable=text_movil)
entry_tiempo=tk.Entry(root,width=20,textvariable=text_tiempo)
# entry_op=tk.Entry(root,width=20,textvariable=text_op)
#bt
button=tk.Button(root,text="calcular",command=calculadora)


#positions
label_title.grid(column=0,row=0)
entry_movil.grid(column=1,row=1)
entry_tiempo.grid(column=1,row=2)
button.grid(column=4,row=5)
# entry_op.grid(column=0,row=0)

#iniciar ventana 
root.mainloop()