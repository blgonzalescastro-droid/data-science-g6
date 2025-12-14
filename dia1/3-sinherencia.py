class Alumno:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        
class Profesor:
    def __init__(self,nombre,email,especialidad):
        self.nombre = nombre
        self.email = email
        self.especialidad = especialidad
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")   
        print(f"Especialidad: {self.especialidad}")

alumno1 = Alumno("Juan Perez", "jperez@gmail.com")
alumno1.mostrar()

profesor1 = Profesor("Ana Gomez", "ana@gmail.com","Matemáticas")
profesor1.mostrar()