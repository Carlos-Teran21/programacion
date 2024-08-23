class Estudiantes:
    def __init__(self,nombre,apellido,edad,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        
    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, sexo{self.sexo} ")
        
        if(edad >=18):
            print("Es mayor de edad")
        else:
            print("Es menor de edad") 
            
        if(sexo==1 && sexo!=1):
            print("Es hombre")
        else:
            print("Es mujer")    
            
        
E = Estudiantes('juan','teran',18,1)

E.imprimir_datos()