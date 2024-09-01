class Persona:
    def __init__(self, nombre="nombre:", apellido="apellido:", direccion="direccion:", telefono="telefono:", edad=0, email="email:"):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.edad = edad
        self.email = email

    def imprimir_detalle(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Edad: {self.edad}")
        print(f"Email: {self.email}")


class Empleado(Persona):
    def __init__(self, nombre, apellido, direccion, telefono, edad, email, salario=0.0, jefe_inmediato="Jefe Inmediato", anos_experiencia=0):
        super().__init__(nombre, apellido, direccion, telefono, edad, email)
        self.salario = salario
        self.jefe_inmediato = jefe_inmediato
        self.anos_experiencia = anos_experiencia
        self.cargo = self.asignarCargo()

    def asignarCargo(self):
        if self.salario > 5000000 and self.anos_experiencia >= 5 and 25 <= self.edad <= 45:
            return "se le a otorgado el cargo Senior"
        elif 900000 <= self.salario <= 1200000 and self.anos_experiencia <= 2 and 18 <= self.edad <= 22:
            return "se le a otorgado el cargo Junior"
       

    def imprimir_detalle(self):
        super().imprimir_detalle()
        print(f"Salario: ${self.salario}")
        print(f"Jefe Inmediato: {self.jefe_inmediato}")
        print(f"Años de Experiencia: {self.anos_experiencia}")
        print(f"Cargo: {self.cargo}")

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
direccion = input("Ingrese la dirección: ")
telefono = input("Ingrese el teléfono: ")
edad = int(input("Ingrese la edad: "))
email = input("Ingrese el email: ")
salario = float(input("Ingrese el salario: "))
jefe_inmediato = input("Ingrese el jefe inmediato: ")
anos_experiencia = int(input("Ingrese los años de experiencia: "))

empleado1 = Empleado(nombre, apellido, direccion, telefono, edad, email, salario, jefe_inmediato, anos_experiencia)
empleado1.imprimir_detalle()
