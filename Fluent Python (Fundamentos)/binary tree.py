#binary tree (Specifically, a Binary Search Tree)
class Node():
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.right = None # Corrected spelling
        self.left = None

    def __repr__(self):
        # Use str() for safer representation, handles non-string values
        return str(self.value)
    

class BinaryTree():
    def __init__(self):
        self.root = None

    # Optional: Add a __repr__ for the tree itself (e.g., using inorder traversal)
    def __repr__(self):
        nodes = []
        self._inorder_traversal(self.root, nodes)
        return " -> ".join(map(str, nodes)) # Display nodes in order

    def to_ascii(self) -> str:
        lines: list[str] = []

        def _walk(node: Node, prefix: str = "", is_left: bool = True):
            if node is None:
                return
            # rama derecha
            _walk(node.right, prefix + ("│   " if is_left else "    "), False)

            # nodo actual
            lines.append(prefix + ("└── " if is_left else "┌── ") + str(node.value))

            # rama izquierda
            _walk(node.left, prefix + ("    " if is_left else "│   "), True)

        _walk(self.root)
        return "\n".join(lines)

    def print_tree(self):
        """Imprime el árbol en consola."""
        print(self.to_ascii())

    def _inorder_traversal(self, node, nodes_list):
        if node:
            self._inorder_traversal(node.left, nodes_list)
            nodes_list.append(node.value)
            self._inorder_traversal(node.right, nodes_list)

    # --- Método Search ---
    def search(self, x):
        """
        Busca un valor x en el árbol.
        Devuelve el Nodo si se encuentra, None en caso contrario.
        """
        return self.search_recursive(self.root, x)

    def search_recursive(self, current_node, x):
        """
        Función auxiliar recursiva para la búsqueda.
        """
        # Caso base 1: Se llegó a un final (o árbol vacío)
        if current_node is None:
            return None
        # Caso base 2: Valor encontrado
        if current_node.value == x:
            return current_node # Devolver el nodo encontrado

        # Paso recursivo
        if x < current_node.value:
            # Buscar en el subárbol izquierdo
            return self.search_recursive(current_node.left, x)
        else: # x >= current_node.value
            # Buscar en el subárbol derecho
            return self.search_recursive(current_node.right, x)

    # --- Método Insert ---
    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
            return self.root
        else:
            # Start recursive insertion from the root
            return self.insert_recursive(self.root, x)

    def insert_recursive(self, current_node, x):
        # Decide which path to take
        if x < current_node.value:
            # Go left
            if current_node.left is None:
                # Found the spot, create new node and link it
                new_node = Node(x)
                current_node.left = new_node
                new_node.parent = current_node # Set parent pointer
                return new_node # Return the newly inserted node
            else:
                # Continue searching down the left subtree
                return self.insert_recursive(current_node.left, x)
        else: # x >= current_node.value (insert duplicates on the right)
            # Go right
            if current_node.right is None:
                # Found the spot, create new node and link it
                new_node = Node(x)
                current_node.right = new_node # Corrected spelling
                new_node.parent = current_node # Set parent pointer
                return new_node # Return the newly inserted node
            else:
                # Continue searching down the right subtree
                return self.insert_recursive(current_node.right, x) # Corrected spelling

    # --- Solución para encontrar nodos intercambiados ---
    def find_swapped_nodes(self):
        """
        Identifica los dos nodos cuyos valores fueron intercambiados por error.
        Devuelve una tupla (nodo1, nodo2) o (None, None) si no se encuentran
        o el árbol tiene menos de 2 nodos.
        Complejidad: O(n) tiempo, O(h) espacio (por la recursión, h=altura)
        """
        self.first = None
        self.middle = None # Para el caso de nodos adyacentes
        self.last = None
        self.previous = None

        self._find_swapped_recursive(self.root)

        # Determinar qué nodos devolver
        if self.first and self.last:
            # Caso no adyacente: primera violación (first) y segunda (last)
            return (self.first, self.last)
        elif self.first and self.middle:
            # Caso adyacente: la única violación involucra first y middle
            return (self.first, self.middle)
        else:
            # No se encontraron violaciones (árbol ya ordenado o muy pequeño)
            return (None, None)

    def _find_swapped_recursive(self, node):
        if node is None:
            return

        # 1. Recorrer subárbol izquierdo
        self._find_swapped_recursive(node.left)

        # 2. Procesar el nodo actual (comparar con el anterior)
        if self.previous is not None and self.previous.value > node.value:
            # ¡Violación encontrada!
            if self.first is None:
                # Primera violación
                self.first = self.previous
                self.middle = node # Posible segundo nodo si son adyacentes
            else:
                # Segunda violación (sabemos que no son adyacentes)
                self.last = node
                # No necesitamos buscar más violaciones después de la segunda

        # Actualizar el nodo anterior para la siguiente comparación
        self.previous = node

        # 3. Recorrer subárbol derecho
        # Solo continuar si no hemos encontrado definitivamente el segundo nodo (last)
        if self.last is None:
             self._find_swapped_recursive(node.right)


    def recover_tree(self):
        """
        Encuentra los dos nodos intercambiados y restaura sus valores.
        Devuelve True si se realizó una recuperación, False en caso contrario.
        """
        node1, node2 = self.find_swapped_nodes()

        if node1 and node2:
            print(f"Intercambiando valores de nodo {node1.value} y nodo {node2.value}")
            # Intercambiar solo los VALORES
            node1.value, node2.value = node2.value, node1.value
            return True
        else:
            print("No se encontraron nodos para intercambiar o el árbol es válido.")
            return False

    def balance_tree(self):
        nodes = []
        balance_tree = BinaryTree()
        self.create_balance_tree(nodes, balance_tree)
        self._inorder_traversal(self.root, nodes)
        return balance_tree
    

    def create_balance_tree(self, list, balance_tree):
        div = len(list) // 2
        if list:
            balance_tree.insert(list[div])
            left, rigth = list[0:div], list[div+1: -1]
            self.create_balance_tree(left,balance_tree)
            self.create_balance_tree(rigth,balance_tree)
         



# --- Ejemplo de Uso ---
tree = BinaryTree()
# Crear un BST válido: 1, 2, 3, 4, 5, 6, 7 (insertados en un orden que crea el árbol)
nodes = [4, 2, 6, 1, 3, 5, 7]
for val in nodes:
    tree.insert(val)

print("Árbol original (in-order):", tree) # Usa __repr__ que hace in-order

# Probar la búsqueda
print("\n--- Probando Search ---")
search_val = 3
found_node = tree.search(search_val)
if found_node:
    print(f"Search({search_val}): Encontrado nodo con valor {found_node.value}")
    if found_node.parent:
         print(f"  El padre de {found_node.value} es {found_node.parent.value}")
    if found_node.left:
         print(f"  El hijo izquierdo de {found_node.value} es {found_node.left.value}")
    if found_node.right:
         print(f"  El hijo derecho de {found_node.value} es {found_node.right.value}")

else:
    print(f"Search({search_val}): No encontrado")

search_val = 8
found_node = tree.search(search_val)
if found_node:
    print(f"Search({search_val}): Encontrado nodo con valor {found_node.value}")
else:
    print(f"Search({search_val}): No encontrado") # Esperado


# --- Simular el intercambio erróneo (ej: 3 y 6) ---
node3 = tree.search(3)
node6 = tree.search(6)

if node3 and node6:
    print("\nSimulando intercambio erróneo de valores 3 y 6...")
    node3.value, node6.value = node6.value, node3.value # Intercambio incorrecto
    print("Árbol después del intercambio erróneo:", tree) # Debería mostrar un orden incorrecto
else:
    print("Error: No se encontraron los nodos 3 o 6 para simular el intercambio.")
    exit()


# --- Usar el algoritmo para encontrar y arreglar ---
print("\nIntentando recuperar el árbol...")
recovered = tree.recover_tree()

if recovered:
    print("\nÁrbol después de la recuperación (in-order):", tree) # Debería estar ordenado de nuevo

# --- Otro ejemplo: Intercambio adyacente (ej: 5 y 6) ---
tree2 = BinaryTree()
nodes2 = [4, 2, 6, 1, 3, 5, 7]
for val in nodes2:
    tree2.insert(val)

print("\n\n--- Ejemplo Adyacente ---")
print("Árbol original 2 (in-order):", tree2)
node5 = tree2.search(5)
node6 = tree2.search(6)
if node5 and node6:
    print("\nSimulando intercambio erróneo de valores 5 y 6...")
    node5.value, node6.value = node6.value, node5.value
    print("Árbol 2 después del intercambio erróneo:", tree2)
else:
    print("Error: No se encontraron los nodos 5 o 6 para simular el intercambio.")
    exit()

print("\nIntentando recuperar el árbol 2...")
recovered2 = tree2.recover_tree()
if recovered2:
    print("\nÁrbol 2 después de la recuperación (in-order):", tree2)

tree3 = BinaryTree()
for v in ['10', '20', '30','40', '50', '60', '70']:
        tree3.insert(v)
tree3.balance_tree().print_tree()
tree3.print_tree()
