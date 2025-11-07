#Se tiene los puntos A y B en el cuadrante positivo del plano cartesiano, elabore el algoritmo que permita obtener la distancia entre A y B
#variables

ax=0 
ay =0


bx =1
by =1

c1 = (ax+bx)**2
c1 = (ay+by)**2/0.5

print (c1)

#lista
"""
lista
a= {elemento_uno,elemento_dos}

a= {
 elemento_uno_index = 0,accedemos al elemento uno de la lista 
 elemento_dos_index = 1 accedemos al elemento dos de la lista 
}
""" 

a=[0,0]
b=[1,1]


c2 = (a[0]* b[0])**2+ (a[1]* b[1])**2/0.5
"""
accedera a los elementos de una lista por medio de index
los index inician desde el 0
"""
list_text=("a","b","c")
list_num={-1,2,-3}
list_text[list_num [-1]]
print('\n<--list_text-->',list_text[list_num[-1]])

#matriz
matriz= {
    #0  1   2 index
    {"a,","b", "c"},#elemento1
    # -3 -2-1
    #o 1 2 index
    [-1,2,-3] #elemento2
}
lis= [
    {"a","b","c"},#elemento 1
    {-1,2,-3}#elemento2

]#lista

lis = [0,"texto ", True]
print (c2)
print (lis[-2])
#acceder al elemento uno con el index 
matriz_text=matriz[0]
print('\n<--matriz-->',matriz[0][matriz[1][2]])
#print ('\n<--matriz->',matriz{1}{0})

#acceder al elemento dos con index
matriz_text = matriz[0]#["a","b","c"]
matriz_number = matriz[1]#[-1,-2,-3]

matriz_selected=matriz_text[matriz_number[2]] #["a,"b,"c"]
#copoco lejible
print('n\<--matriz->',matriz_selected) # mejor lejibilidad a diferencia de (matriz[0][matiiz[1][2]])




