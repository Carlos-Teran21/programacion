class Usuario:
    def __init__(self, nombre_completo="nombre_completo:", nickname="nickname:", clave="clave:", tipo="tipo:", fecha_creacion="fecha_creacion:"): 
        self.nombre_completo = nombre_completo
        self.nickname = nickname
        self.clave = clave
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion

    def imprimir_datos(self):
        print(f"Nombre Completo: {self.nombre_completo}")
        print(f"Nickname: {self.nickname}")
        print(f"Clave: {self.clave}")
        print(f"Tipo: {self.tipo}")
        print(f"Fecha de Creación: {self.fecha_creacion}")

def crear_usuario(personas, mapa_usuarios):
    nombre = input("Introduce el nombre de la persona: ")
    nuevo_usuario = Usuario(nombre_completo=nombre)
    personas.append(nuevo_usuario)
    
   
    mapa_usuarios[len(personas) - 1] = nuevo_usuario
    print("Persona añadida:", nombre)
    print("Lista actual de personas:")
    for persona in personas:
        persona.imprimir_datos()

def buscar_usuario(personas):
    nombre_buscado = input("Ingrese el nombre de la persona que desea buscar: ")
    for persona in personas:
        if persona.nombre_completo == nombre_buscado:
            print("La persona fue encontrada:")
            persona.imprimir_datos()
            return
    print("Persona no encontrada")  

def eliminar_usuario(personas, mapa_usuarios):
    print("Lista actual de usuarios:")
    for i, persona in enumerate(personas):
        print(f"{i}: {persona.nombre_completo}")
    
    indice = int(input("Ingrese el número de la persona a eliminar según su orden numérico en la lista (el primero es el número 0): "))
    
    if 0 <= indice < len(personas):
        usuario_eliminado = personas.pop(indice)
        del mapa_usuarios[indice]  
        print("Usuario eliminado:", usuario_eliminado.nombre_completo)
        
       
        for i in range(indice, len(personas)):
            mapa_usuarios[i] = personas[i]
        
    
        if len(personas) > indice:
            del mapa_usuarios[len(personas)]
        
        print("Lista de usuarios que quedaron:")
        for persona in personas:
            persona.imprimir_datos()

def mostrar_menu():
    print("\n*MENU PRINCIPAL*")
    print("1) Agregar usuario")
    print("2) Buscar usuario") 
    print("3) Eliminar usuario")


def main():
    personas = []
    mapa_usuarios = {}
    
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")
        
        if opcion == '1':
            crear_usuario(personas, mapa_usuarios)  
        elif opcion == '2':
            buscar_usuario(personas) 
        elif opcion == '3':
            eliminar_usuario(personas, mapa_usuarios)
        elif opcion == '4':
            break
     

if __name__ == "__main__":
    main()
