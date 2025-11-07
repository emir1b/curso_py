from funcion import interar
#variables
n1= input ("n1:") 
n2= input ("n2:")
op= input ("operador:")

print ("n1")
interar.hiterar_conjunto(n1,n2,op)
if not op == '/' and n2 == '0' or n2 == '' or n2 == 0:  
    interar.hiterar_conjunto(n1,n2,op)
        
# if op == "-":
#     if n1 [0] =="[" and n1 [-1]=="]":
#      print ("\n", int (n1[1])-int (n2))
#      print (int (n1[3])-int (n2), "\n")
#      interar.hiterar_conjunto(n1,n2,op)
    
# #print (int(n1 )- int (n2))
# elif op == "+":
#     print (int (n1)+ int (n2))
# elif op == "*":
#     print (int (n1)* int (n2))
# elif op == "/":
#     print (int (n1)/ int (n2))
# else:
#     print("error")
[]