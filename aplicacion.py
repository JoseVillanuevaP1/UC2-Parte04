#ABRE EL LOGIN.TXT Y LEE EL USUARIO
login = open ("login.txt","rt")
login_user = login.read()

#ABRE EL CLAVE.TXT Y LEE LA CLAVE
clave = open ("clave.txt","rt")
clave_user = clave.read()

#VALIDA QUE EL USUARO Y EL LOGIN SEAN CORRECTOS
def login():
    confirmacion=1
    while confirmacion ==1:
        
        login=input("Ingrese usuario: ")
        clave=input("Ingrese clave: ")
        
        if login == login_user and clave == clave_user:
            print("\nUsuario y Clave correcto")
            confirmacion=0
            menu()
        else:
             print("Usuario y/o clave incorrectos.\n Intente nuevamente.\n")

#MENU QUE SE MUESTRA CUANDO ES CORRECTO
def menu():
    print("\nDatos Persona: \n1. Listar personas\n2. Agregar personas\n3. Salir")
    opcion = input("Opcion: ")
    if opcion == "1":
        print("op1")
    elif opcion == "2":
        print("op2")
    elif opcion == "3":
        print("op3")
    else:
        print("\nOpcion no valida, ingrese nuevamente una opcion\n")
        menu()
        
login ()
