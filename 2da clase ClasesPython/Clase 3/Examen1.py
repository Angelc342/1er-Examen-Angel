# Crear una clase bateria para instanciar una bateria y demostrar el uso de copy.deepcopy modificando la copia sin afectar la original
# Crear nodo bateria y lista bateria con unico puntero cabeza implementar los metodos insertar al inicio bateria y
# el metodo de purgar agotadas al cual debe recorrer la lista y recolectar los punteros y elimine las baterias con menos de 3V.

import copy

# Definicion de Objeto 
class Bateria:
    """clase que representa una bateria con identificador y su voltaje."""

    def __init__(self, identificador, voltaje) -> None:
        self.indentificador = identificador
        self.voltaje = voltaje

    def __str__(self):
        return f"[{self.indentificador}:{self.voltaje}V"

class NodoBateria:
    """Nodo que almacena una bateria con un identificador y un puntero al siguiente nodo."""
    def __init__(self, bateria):
        self.bateria = bateria
        self.siguiente = None

class ListaBateria:
    """Lista enlazada simple de baterias con un unico puntero cabeza."""
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, bateria):
        """Insertar el Nuevo nodo con la bateria al principio de la lista."""
        nuevo_nodo = NodoBateria(bateria)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def purgar_agotadas(self):
        """Recorre la lista, recolectay elimina las baterias con menos de 3V."""
        # Eliminar nodos al inicio si cumplen la condicion (< 3V)

        while self.cabeza is not None and self.cabeza.bateria.voltaje < 3.0:
            print(f"Purgando (Agotada):{self.cabeza.bateria}")
            self.cabeza = self.cabeza.siguiente
        
        # Recorrer el resto de la lista para eliminar nodos inmediatos o finales
        actual = self.cabeza
        while actual is not None and actual.siguiente is not None:
            if actual.siguiente.bateria.voltaje < 3.0:
             print(f"Purgando (Agotada):{actual.siguiente.bateria}")
             actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente

    def mostrar_lista(self):
        """Muestra los Elementos actuales en la lista enlazada."""
        actual = self.cabeza
        elementos = []
        while actual is not None:
            elementos.append(str(actual.bateria))
            actual = actual.siguiente
            print(" -> ".join(elementos) if elementos else "Lista vacia")

# MIS PRUEBAS

# 1. Prueba de copy.deepcopy
print("--- PRUEBA DECOPY ---")
original = Bateria("Bateria-A", 3.7)
copia = copy.deepcopy(original)
copia.voltaje = 1.5  # Modificamos la copia
print("Original:", original)
print("Copia modificada:", copia)

# 2. Prueba de la Lista y la Purga de baterías < 3V
print("\n--- PRUEBA DE LISTA Y PURGA ---")
mi_lista = ListaBateria()

# Insertamos varias baterías (algunas con menos de 3V)
mi_lista.insertar_al_inicio(Bateria("Bat-1", 4.1))
mi_lista.insertar_al_inicio(Bateria("Bat-2", 2.2))  # Se debe purgar (< 3V)
mi_lista.insertar_al_inicio(Bateria("Bat-3", 3.5))
mi_lista.insertar_al_inicio(Bateria("Bat-4", 1.8))  # Se debe purgar (< 3V)

print("Estado inicial de la lista:")
mi_lista.mostrar_lista()

print("\nEjecutando purga (eliminando menores a 3V)...")
mi_lista.purgar_agotadas()

print("\nEstado final de la lista después de purgar:")
mi_lista.mostrar_lista()