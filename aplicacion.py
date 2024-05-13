import time
import sys
#ABRE EL LOGIN.TXT Y LEE EL USUARIO
login = open ("login.txt","rt")
login_user = login.read()

#ABRE EL CLAVE.TXT Y LEE LA CLAVE
clave = open ("clave.txt","rt")
clave_user = clave.read()

#VALIDA QUE EL USUARO Y EL LOGIN SEAN CORRECTOS
def login():
    confirmacion=0
    while confirmacion <=1:
        
        login=input("Ingrese usuario: ")
        clave=input("Ingrese clave: ")
        
        if login == login_user and clave == clave_user:
            print("\nUsuario y Clave correcto")
            menu()
        else:
            confirmacion+=1
            print("Usuario y/o clave incorrectos.\n Intente nuevamente.\n")
    print("Se equivoco mas de dos veces") 
    time.sleep(3)
            
#MENU QUE SE MUESTRA CUANDO ES CORRECTO
def menu():
    print("\nDatos Persona: \n1. Listar personas\n2. Agregar personas\n3. Salir")
    opcion = input("Opcion: ")
    if opcion == "1":
        listar_personas()
    elif opcion == "2":
        agregar_personas()
    elif opcion == "3":
        salir()
    else:
        print("\nOpcion no valida, ingrese nuevamente una opcion\n")
        menu()

def listar_personas():
    personas = open ("nombre.txt","rt",encoding='utf8')
    nom = personas.read()
    lista_nom = nom.split()
    
    apellidos = open ("apellido.txt","rt", encoding='utf8')
    ap = apellidos.read()
    lista_ap = ap.split()
    
    dni = open ("dni.txt","rt", encoding='utf8')
    documento = dni.read()
    lista_dni= documento.split()
    
    fin= len(lista_dni)
    
    print("\nLista de Personas\n")
    
    for indice in range(fin):
        nombre_formateado = lista_nom[indice].ljust(15)
        apellido_formateado = lista_ap[indice].ljust(15)
        
        print(f"{nombre_formateado}\t{apellido_formateado}\t{lista_dni[indice]}")
    menu()
    
def agregar_personas():
    
    
    print("\n Agregar persona\n")
    
    nombre = input("Ingrese nombre: ")
    archivo1 = open("nombre.txt","at")
    archivo1.write("\n"+ nombre)
    archivo1.close()
    
    apellido = input("Ingrese apellido: ")
    archivo2 = open("apellido.txt","at")
    archivo2.write("\n"+ apellido)
    archivo2.close()
    
    dni = input("Ingrese dni: ")
    archivo3 = open("dni.txt","at")
    archivo3.write("\n"+ dni)
    archivo3.close()
    
    print("\nPersona agredada correctamente\n")
    menu()
def salir():
    sys.exit()
    
login ()
