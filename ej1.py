class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.prestado_a = None

    def prestar(self, miembro):
        self.disponible = False
        self.prestado_a = miembro

    def devolver(self):
        self.disponible = True
        self.prestado_a = None


class Miembro:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.disponible:
            libro.prestar(self)
            self.libros_prestados.append(libro)
            print(f"{self.nombre} tomó prestado el libro '{libro.titulo}'.")
        else:
            print(f"El libro '{libro.titulo}' no está disponible.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} devolvió el libro '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no tiene prestado ese libro.")


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)

    def consultar_libros(self):
        print("\nEstado de los libros:")
        for libro in self.libros:
            if libro.disponible:
                print(f"'{libro.titulo}' - Disponible")
            else:
                print(f"'{libro.titulo}' - Prestado a {libro.prestado_a.nombre}")

    def consultar_miembros(self):
        print("\nEstado de los miembros:")
        for miembro in self.miembros:
            print(f"{miembro.nombre} - DNI: {miembro.dni}")
            if miembro.libros_prestados:
                for libro in miembro.libros_prestados:
                    print(f"  Libro prestado: {libro.titulo}")
            else:
                print("  No tiene libros prestados")


# Programa principal

biblioteca = Biblioteca()

libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "12345")
libro2 = Libro("1984", "George Orwell", "67890")

miembro1 = Miembro("Nicolás", "40123456")
miembro2 = Miembro("Sofía", "42111222")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.agregar_miembro(miembro1)
biblioteca.agregar_miembro(miembro2)

miembro1.tomar_prestado(libro1)

biblioteca.consultar_libros()
biblioteca.consultar_miembros()

miembro1.devolver_libro(libro1)

biblioteca.consultar_libros()
biblioteca.consultar_miembros()