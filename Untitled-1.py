def mostrar_menu():
    print("\n Menú")
    print("1. Crear persona")
    print("2. Eliminar persona")
    print("3. Listar personas")
    print("4. Buscar persona")
    


def crear_persona(personas):
    nombre = input("Introduce el nombre de la persona:")
    personas.append(nombre)
    print("Persona añadida:", nombre)
    print("Lista actual de personas:", personas)


def eliminar_persona(personas):
   
    
    print("Lista actual de personas:", personas)
    
    indice = int(input("Introduce el índice de la persona a eliminar: "))
    if 0 <= indice < len(personas):
            persona_eliminada = personas.pop(indice)
            print("Persona eliminada:", persona_eliminada)
            print("Lista actual de personas:", personas)
      
   

def listar_personas(personas):
    if not personas:
        print("La lista está vacía.")
    else:
        print("Lista actual de personas:", personas)


def buscar_persona(personas):
   
    nombre = input("Introduce el nombre de la persona a buscar: ")
    if nombre in personas:
        print("La persona fue encontrada.")
    else:
        print("La persona no fue encontrada.")


def main():
    personas = []
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Elige una opción: "))
        except:
            
            continue

        if opcion == 1:
            crear_persona(personas)
        elif opcion == 2:
            eliminar_persona(personas)
        elif opcion == 3:
            listar_personas(personas)
        elif opcion == 4:
            buscar_persona(personas)
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
           

if __name__ == "__main__":
    main()
