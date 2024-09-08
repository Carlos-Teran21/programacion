class Usuario:
    def __init__(self, nombre_completo, nickname, clave, tipo, fecha_creacion):
        self.datos = {
            'nombre_completo': nombre_completo,
            'nickname': nickname,
            'clave': clave,
            'tipo': tipo,
            'fecha_creacion': fecha_creacion
        }

def agregar_usuario(usuarios):
    nombre_completo = input("Ingrese el nombre completo: ")
    nickname = input("Ingrese el nickname: ")
    clave = input("Ingrese la clave: ")
    tipo = input("Ingrese el tipo: ")
    fecha_creacion = input("Ingrese la fecha de creación: ")
    
    usuario = Usuario(nombre_completo, nickname, clave, tipo, fecha_creacion)
    usuarios[nickname] = usuario.datos
    print(f"Usuario {nickname} agregado.")

def buscar_usuario(usuarios):
    nickname = input("Ingrese el nickname a buscar: ")
    if nickname in usuarios:
        print("Datos del usuario:", usuarios[nickname])
    else:
        print("Usuario no encontrado.")

def eliminar_usuario(usuarios):
    nickname = input("Ingrese el nickname a eliminar: ")
    if nickname in usuarios:
        del usuarios[nickname]
        print(f"Usuario {nickname} eliminado.")

def menu():
    usuarios = {}
    
    while True:
        print("\*MENU PRINCIPAL*")
        print("1. Agregar Usuario")
        print("2. Buscar Usuario")
        print("3. Eliminar Usuario")
    
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_usuario(usuarios)
        elif opcion == '2':
            buscar_usuario(usuarios)
        elif opcion == '3':
            eliminar_usuario(usuarios)
