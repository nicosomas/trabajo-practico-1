class Estudiante:
    def __init__(self, nombre, apellido, matricula, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.carrera = carrera
        self.cursos_inscriptos = []

    def inscribirse(self, curso):
        if curso.hay_cupo():
            curso.agregar_estudiante(self)
            self.cursos_inscriptos.append(curso)
            print(f"{self.nombre} se inscribió en {curso.nombre}.")
        else:
            print(f"No hay cupo disponible en {curso.nombre}.")

    def darse_de_baja(self, curso):
        if curso in self.cursos_inscriptos:
            curso.eliminar_estudiante(self)
            self.cursos_inscriptos.remove(curso)
            print(f"{self.nombre} se dio de baja de {curso.nombre}.")
        else:
            print(f"{self.nombre} no está inscripto en {curso.nombre}.")


class Curso:
    def __init__(self, nombre, codigo, profesor, capacidad_maxima):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad_maxima = capacidad_maxima
        self.estudiantes = []

    def hay_cupo(self):
        return len(self.estudiantes) < self.capacidad_maxima

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            self.estudiantes.remove(estudiante)


class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def consultar_cursos(self):
        print("\nEstado de los cursos:")
        for curso in self.cursos:
            inscriptos = len(curso.estudiantes)
            cupos_disponibles = curso.capacidad_maxima - inscriptos

            print(f"{curso.nombre} - Código: {curso.codigo}")
            print(f"Profesor: {curso.profesor}")
            print(f"Inscriptos: {inscriptos}")
            print(f"Cupos disponibles: {cupos_disponibles}")
            print("------------------------")

    def consultar_estudiantes(self):
        print("\nEstado de los estudiantes:")
        for estudiante in self.estudiantes:
            print(f"{estudiante.nombre} {estudiante.apellido}")
            print(f"Matrícula: {estudiante.matricula}")
            print(f"Carrera: {estudiante.carrera}")

            if estudiante.cursos_inscriptos:
                print("Cursos inscriptos:")
                for curso in estudiante.cursos_inscriptos:
                    print(f"- {curso.nombre}")
            else:
                print("No está inscripto en ningún curso.")

            print("------------------------")


# Programa principal

facultad = Facultad()

estudiante1 = Estudiante("Nicolás", "Somaschini", "A001", "Desarrollo de Software")
estudiante2 = Estudiante("Lucía", "Gómez", "A002", "Analista de Sistemas")

curso1 = Curso("Programación I", "PROG101", "Carlos Pérez", 2)
curso2 = Curso("Base de Datos", "BD202", "María López", 1)

facultad.agregar_estudiante(estudiante1)
facultad.agregar_estudiante(estudiante2)

facultad.agregar_curso(curso1)
facultad.agregar_curso(curso2)

estudiante1.inscribirse(curso1)
estudiante2.inscribirse(curso1)
estudiante1.inscribirse(curso2)

facultad.consultar_cursos()
facultad.consultar_estudiantes()

estudiante1.darse_de_baja(curso2)

facultad.consultar_cursos()
facultad.consultar_estudiantes()