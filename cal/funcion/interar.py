def hiterar_conjunto(n1,n2, op ):
    
    for n in list(n1):
        if n == "[" or n == " " or n == "," or n == "]" or n=="}" or n == "{":
            continue 
        if n=="a" :
            continue 
        print("error")
       
        print (  eval(f"{n}+ {op} + {n2}"))