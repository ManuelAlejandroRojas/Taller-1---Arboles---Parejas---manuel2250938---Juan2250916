from bigtree import Node, print_tree, find_name

raiz = Node("50")

izquierdo  = Node("30", parent=raiz)
derecho    = Node("70", parent=raiz)

Node("20", parent=izquierdo)
Node("40", parent=izquierdo)

Node("60", parent=derecho)
Node("80", parent=derecho)



print("Estructura del arbol:")
print_tree(raiz)

#Recorridos

#Orden
def inorder(nodo):
    if nodo is None:
        return
    hijos = list(nodo.children)
    inorder(hijos[0] if len(hijos) > 0 else None)
    print(nodo.name, end=" ")
    inorder(hijos[1] if len(hijos) > 1 else None)

#Preorden
def preorder(nodo):
    if nodo is None:
        return
    hijos = list(nodo.children)
    print(nodo.name, end=" ")
    preorder(hijos[0] if len(hijos) > 0 else None)
    preorder(hijos[1] if len(hijos) > 1 else None)


print("\nIn-order  (ordenado):  ", end="")
inorder(raiz)

print("\nPre-order (raiz primero): ", end="")
preorder(raiz)

#Caracteristicas
total_nodos = 1 + len(list(raiz.descendants))

print(f"\n\nProfundidad maxima : {raiz.max_depth}")
print(f"Total de nodos     : {total_nodos}")


# Para buscar

objetivo = "40"
resultado = find_name(raiz, objetivo)

if resultado:
    print(f"\nNodo '{objetivo}' encontrado.")
    print(f"  Padre   : {resultado.parent.name}")
    print(f"  Nivel   : {resultado.depth}")
else:
    print(f"\nNodo '{objetivo}' no encontrado.")