import os
import sys

print("--------------------------------------------")
print("-------!!!SOLO PERSONAL AUTORIZADO!!!-------")
print("--------------------------------------------")
contraseña = input("Ingrese la contraseña correcta: ")
if contraseña == "cisco":
    file = open("Inicio_Prueba.txt", "r")
    for item in file:
        print(item)
    file.close()
else:
    print("Contraseña incorrecta")
    sys.exit()

while True:
    print("Escoja la accion que desea realizar:")
    print("1. Crear un archivo")
    print("2. Abrir un archivo ")
    print("3. Agregar texto a un archivo")
    print("4. Eliminar un archivo")
    print("5. Salir del programa")

    user_choice = input("> ")

    if user_choice == "1":
        file_name = input("Ingrese el nombre del nuevo archivo: ")
        with open(file_name, 'w') as f:
            pass
        print("El archivo "f"{file_name} se creo correctamente")

    elif user_choice == "2":
        file_list = os.listdir()
        print("Archivos disponibles:")
        for file_name in file_list:
            if file_name.endswith(".txt"):
                print(file_name)
        file_name = input("Que archivo desea abrir: ")
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                print(f.read())
        else:
            print("El archivo "f"{file_name} no existe.")

    elif user_choice == "3":
        file_list = os.listdir()
        print("Archivos disponibles:")
        for file_name in file_list:
            if file_name.endswith(".txt"):
                print(file_name)
        file_name = input("¿Que archivo desea editar?: ")
        if os.path.exists(file_name):
            with open(file_name, 'a') as f:
                new_text = input("Introduzca el texto que desea agregar: ")
                f.write(new_text)
            print("El archivo "f"{file_name} fue editado correctamente")
        else:
            print("El archivo"f"{file_name} no existe")

    elif user_choice == "4":
        file_list = os.listdir()
        print("Archivos disponibles:")
        for file_name in file_list:
            if file_name.endswith(".txt"):
                print(file_name)
        file_name = input("¿Cual es el archivo que desea borrar?: ")
        if os.path.exists(file_name):
            os.remove(file_name)
            print("El archivo "f"{file_name} se elimino correctamente ")
        else:
            print("El archivo "f"{file_name} no existe.")

    elif user_choice == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Intentelo nuevamente")