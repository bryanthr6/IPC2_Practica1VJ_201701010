from graphviz import Digraph

class Nodo:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = 'pendiente'
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.contador_id = 0

    def agregar_tarea(self, nombre, descripcion):
        nueva_tarea = Nodo(self.contador_id, nombre, descripcion)
        self.contador_id += 1
        if not self.cabeza:
            self.cabeza = nueva_tarea
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea
        print(f"Tarea '{nombre}' agregada con ID {nueva_tarea.id} y estado 'pendiente'.")
        print(" ")

    def cambiar_estado(self, id, nuevo_estado):
        actual = self.cabeza
        while actual:
            if actual.id == id:
                actual.estado = nuevo_estado
                print(f"Estado de la tarea con ID {id} cambiado a '{nuevo_estado}'.")
                return
            actual = actual.siguiente
        print(f"Tarea con ID {id} no encontrada.")

    def eliminar_tarea(self, id):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.id == id:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"Tarea con ID {id} eliminada.")
                return
            anterior = actual
            actual = actual.siguiente
        print(f"Tarea con ID {id} no encontrada.")

    def obtener_tareas(self):
        tareas = []
        actual = self.cabeza
        while actual:
            tareas.append(actual)
            actual = actual.siguiente
        return tareas

    def mostrar_tareas(self):
        tareas = self.obtener_tareas()
        if not tareas:
            print("¡No hay tareas registradas!")
            print(" ")
        else:
            print("Lista de tareas pendientes:")
            for tarea in tareas:
                print(f"ID: {tarea.id}, Nombre: {tarea.nombre}, Descripción: {tarea.descripcion}, Estado: {tarea.estado}")
                print(" ")

    def graficar_lista(self):
        dot = Digraph()
        actual = self.cabeza
        while actual:
            dot.node(str(actual.id), f"{actual.nombre} ({actual.estado})")
            if actual.siguiente:
                dot.edge(str(actual.id), str(actual.siguiente.id))
            actual = actual.siguiente
        dot.render('lista_tareas', view=True)
        print("Lista de tareas graficada y abierta.")

def mostrar_menu():
    lista_tareas = ListaEnlazada()
    
    while True:
        # Mostrar tareas antes de las opciones del menú
        tareas = lista_tareas.obtener_tareas()
        if not tareas:
            print("¡No hay tareas registradas!")
        else:
            print("Lista de tareas pendientes:")
            for tarea in tareas:
                print(f"ID: {tarea.id}, Nombre: {tarea.nombre}, Descripción: {tarea.descripcion}, Estado: {tarea.estado}")
        
        # Mostrar opciones del menú
        print("\nMenú de Administrador de Tareas")
        print("1. Agregar una nueva tarea")
        print("2. Asignar estado a 'En progreso' a una tarea")
        print("3. Terminar una tarea")
        print("4. Ver lista de tareas")
        print("5. Ver información del desarrollador")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            lista_tareas.agregar_tarea(nombre, descripcion)
        elif opcion == '2':
            id = int(input("ID de la tarea a cambiar estado a 'En progreso': "))
            lista_tareas.cambiar_estado(id, 'En Progreso')
        elif opcion == '3':
            id = int(input("ID de la tarea a eliminar: "))
            lista_tareas.eliminar_tarea(id)
        elif opcion == '4':
            lista_tareas.mostrar_tareas()
            lista_tareas.graficar_lista()
        elif opcion == '5':
            print("**********************************")
            print("*Datos del desarrollador:        *")
            print("*Carnet: 201701010               *")
            print("*Nombre: Bryant Herrera Rubio    *")
            print("*Curso: IPC 2 sección: A         *")
            print("**********************************")
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
