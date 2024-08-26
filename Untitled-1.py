def mostrarMenu():
    print("\nMenú")
    print("1. Crear persona")
    print("2. Eliminar persona")
    print("3. Listar personas")
    print("4. Buscar persona")
  

def crearPersona(personas):
    nombre = input("Introduce el nombre de la persona:")
    personas.append(nombre)
    print("Persona añadida:", nombre)
    print("Lista actual de personas:", personas)

def eliminarPersona(personas):
    print("Lista actual de personas:", personas)
    
    try:
        indice = int(input("ingrese a la persona a eliminar segun su orden numerico en la lista, el primero es el numero 0:"))
        if 0 <= indice < len(personas):
            persona_eliminada = personas.pop(indice)
            print("Persona eliminada:", persona_eliminada)
       
    except ValueError:
        print("Por favor, introduce un número entero válido.")
    
    print("Lista actual de personas:", personas)

def listarPersonas(personas):
  
        print("Lista actual de personas:", personas)

def buscarPersona(personas):
    nombre = input("Introduce el nombre de la persona a buscar: ")
    if nombre in personas:
        print("La persona fue encontrada.")
    else:
        print("La persona no fue encontrada.")

def main():
    personas = []
    while True:
        mostrarMenu()
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Por favor, introduce un número entero válido.")
            continue

        if opcion == 1:
            crearPersona(personas)
        elif opcion == 2:
            eliminarPersona(personas)
        elif opcion == 3:
            listarPersonas(personas)
        elif opcion == 4:
            buscarPersona(personas)
      
      

if __name__ == "__main__":
    main()

