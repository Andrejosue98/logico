###Progra de Diseño logico

#funciones definidas:
def ToBin(num, let): #pasa el numero octal a binario
    q=len(let)
    i=q-1
    x=""
    while i>=0:
        p=int(let[i])
        if p==0:
            x="000"+x
        elif p==1:
            x="001"+x
        elif p==2:
            x="010"+x
        elif p==3:
            x="011"+x
        elif p==4:
            x="100"+x
        elif p==5:
            x="101"+x
        elif p==6:
            x="110"+x
        else:
            x="111"+x
        i=i-1
    return x
        
def ToHex(bi):    #pasa el numero binario a Hexa
    
    
    

def submenu(): #submenu final que permite terminar el programa o continuar 
    print("1- digitar un nuevo número")
    print("2- salir")
    opcion=int(input("ocpión: "))
    if opcion ==1:
            menu()
    elif opcion==2:
            print("Adios")
    else :
            print ("opcion invalida")
            submenu()


    
def valid(ent, Largo): #valida que sea de 4 digitos, que este dentro del rango y que sea octal

    if len(Largo)<= 4:
        if ent < 0 or ent > 7777:
            print("El numero no es valido")
            menu()
            
        else:
            i=0
            y=len(Largo)-1
            while i<=y:
                x=int(Largo[i])
                if x>7:
                    print("El número no es valido")
                    menu()
                i=i+1
            return 1
            
    else:
            print("El número no es valido")
            menu()

def hexa(bina):
    largo=len(bina)
   
    if largo%4==0:#Aqui reviso si la longitud del binario es divisible entre 4, si no lo es, lo corrige y le pone 0s
        lista1=[]
        cont=0
        contf=0
        
        while cont<largo:
            aux=""
            while (contf<4):#Aqui voy dividiendo el binario en grupos de 4, ese aux se reinicia cada vez que llega a 3
                aux=aux+(bina[cont])
                contf+=1
                cont+=1
            
            lista1.append(aux)#Añade cada grupo de 4 en una posicion de la lista
            contf=0
        
        aux1=[]#Comparo los strings en lista1, y aqui se convierten a hexadecimal, entonces lista1 los tiene en binarios y aux1 en hexadecimal
        for n in range(0,len(lista1)):
            if lista1[n]=="0000":
                aux1.append("0")
            elif lista1[n]=="0001":
                aux1.append("1")
            elif lista1[n]=="0010":
                aux1.append("2")
            elif lista1[n]=="0011":
                aux1.append("3")
            elif lista1[n]=="0100":
                aux1.append("4")
            elif lista1[n]=="0101":
                aux1.append("5")
            elif lista1[n]=="0110":
                aux1.append("6")
            elif lista1[n]=="0111":
                aux1.append("7")
            elif lista1[n]=="1000":
                aux1.append("8")
            elif lista1[n]=="1001":
                aux1.append("9")
            elif lista1[n]=="1010":
                aux1.append("A")
            elif lista1[n]=="1011":
                aux1.append("B")
            elif lista1[n]=="1100":
                aux1.append("C")
            elif lista1[n]=="1101":
                aux1.append("D")
            elif lista1[n]=="1110":
                aux1.append("E")
            elif lista1[n]=="1111":
                aux1.append("F")
            else:
                print("Numero invalido")
        Hexa=""##Aqui meto en un string ya el numero en hexadecimal. 
        for ele in range(0,len(aux1)):
            Hexa=Hexa+(aux1[ele])
        print(Hexa)
    else: #Correcion en caso de que el numero binario no tenga todos los ceros, basicamente va añadiendo ceros a la operacion
        nuevo="0"
        nuevo=nuevo+bina
        print(nuevo)
        largo=len(nuevo)
        hexa(nuevo)
    
    
    return True
    
#programa principal 


def menu():
    
    try:
        
        Octal= int(input("Ingrese un número en base octal de 4 digitos: ")) #carga el octal
        
        Largo= str(Octal) #pasa el numero a string
        
        valid(Octal, Largo) #función valid

        NumBin= int(ToBin(Octal, Largo)) #funcion ineficiente para pasar a binario y lo guarda en la una variable tipo int 

       
        
        print(NumBin)
        hexa(str(NumBin))
        submenu()
        
    except ValueError:
        print("El valor no es valido")
        menu()
        
    
    

menu()
