def password():
    contraseña = "12345EDD"
    peticion = input("Dime tu contraseña")

    if contraseña == peticion:
        print("Contraseña correcta")
    else:
        while peticion != contraseña:
                print("vuelve a intentarlo")
                peticion = input("Dime tu contraseña")
        else:
                print("la contraseña es correcta")

password()