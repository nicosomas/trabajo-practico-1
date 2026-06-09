class Libro:
    def __init__(self, titulo, autor, isbn):
        if not titulo.strip():
            raise ValueError("El título no puede estar vacío.")

        if not autor.strip():
            raise ValueError("El autor no puede estar vacío.")

        if not isbn.strip():
            raise ValueError("El ISBN no puede estar vacío.")

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.prestado_a = None


class Miembro:
    def __init__(self, nombre, dni):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not dni.isdigit():
            raise ValueError("El DNI debe contener solo números.")

        self.nombre = nombre
        self.dni = dni
        self.libros_prestados = []


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_miembro(self, dni):
        for miembro in self.miembros:
            if miembro.dni == dni:
                return miembro
        return None

    def prestar_libro(self, isbn, dni):

        libro = self.buscar_libro(isbn)

        if libro is None:
            raise Exception("Libro no encontrado.")

        miembro = self.buscar_miembro(dni)

        if miembro is None:
            raise Exception("Miembro no encontrado.")

        if not libro.disponible:
            raise Exception("El libro ya está prestado.")

        libro.disponible = False
        libro.prestado_a = miembro

        miembro.libros_prestados.append(libro)

    def devolver_libro(self, isbn, dni):

        libro = self.buscar_libro(isbn)

        if libro is None:
            raise Exception("Libro no encontrado.")

        miembro = self.buscar_miembro(dni)

        if miembro is None:
            raise Exception("Miembro no encontrado.")

        if libro not in miembro.libros_prestados:
            raise Exception("Ese miembro no tiene este libro.")

        miembro.libros_prestados.remove(libro)

        libro.disponible = True
        libro.prestado_a = None


# =====================
# FUNCIONES
# =====================

def registrar_libro(biblioteca):
    try:
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")

        libro = Libro(titulo, autor, isbn)

        biblioteca.agregar_libro(libro)

        print("Libro registrado correctamente.")

    except Exception as error:
        print("Error:", error)


def registrar_miembro(biblioteca):
    try:
        nombre = input("Nombre: ")
        dni = input("DNI: ")

        miembro = Miembro(nombre, dni)

        biblioteca.agregar_miembro(miembro)

        print("Miembro registrado correctamente.")

    except Exception as error:
        print("Error:", error)


def prestar_libro(biblioteca):
    try:
        isbn = input("ISBN del libro: ")
        dni = input("DNI del miembro: ")

        biblioteca.prestar_libro(isbn, dni)

        print("Préstamo realizado.")

    except Exception as error:
        print("Error:", error)


def devolver_libro(biblioteca):
    try:
        isbn = input("ISBN del libro: ")
        dni = input("DNI del miembro: ")

        biblioteca.devolver_libro(isbn, dni)

        print("Libro devuelto.")

    except Exception as error:
        print("Error:", error)


def mostrar_libros(biblioteca):

    print("\n=== LIBROS ===")

    for libro in biblioteca.libros:

        estado = "Disponible"

        if not libro.disponible:
            estado = f"Prestado a {libro.prestado_a.nombre}"

        print(
            f"Título: {libro.titulo} | "
            f"Autor: {libro.autor} | "
            f"ISBN: {libro.isbn} | "
            f"Estado: {estado}"
        )


def mostrar_miembros(biblioteca):

    print("\n=== MIEMBROS ===")

    for miembro in biblioteca.miembros:

        print(
            f"\nNombre: {miembro.nombre} | DNI: {miembro.dni}"
        )

        if miembro.libros_prestados:

            print("Libros prestados:")

            for libro in miembro.libros_prestados:
                print("-", libro.titulo)

        else:
            print("No tiene libros prestados.")


def menu():

    biblioteca = Biblioteca()

    while True:

        print("\n===== BIBLIOTECA =====")
        print("1. Registrar libro")
        print("2. Registrar miembro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Ver libros")
        print("6. Ver miembros")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_libro(biblioteca)

        elif opcion == "2":
            registrar_miembro(biblioteca)

        elif opcion == "3":
            prestar_libro(biblioteca)

        elif opcion == "4":
            devolver_libro(biblioteca)

        elif opcion == "5":
            mostrar_libros(biblioteca)

        elif opcion == "6":
            mostrar_miembros(biblioteca)

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


menu()