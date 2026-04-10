# Clase Nodo
class Nodo:
	def __init__(self, data):
		self.data = data
		self.anterior = None
		self.siguiente = None
		self.hijos = None

# CLase Listas enlazada simple
class ListaSE:
	def __init__(self):
		self.cabeza = None
		self.final = None
  
  
	# Lista Vacia
	def vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else: 
			print("Lista no vacía")



# Agregar al inicio
	def agregarInicio(self, data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo
			

Nivel1 = ListaSE()
Nivel2 = ListaSE()
Nivel3 = ListaSE()

#Creo la raiz del arbol
Nivel1.agregarInicio(1)

#Agrego el segundo nivel
Nodo_a = Nivel1.cabeza
Nodo_a.hijos = Nivel2
Nivel2.agregarInicio(4)
Nivel2.agregarInicio(3)
Nivel2.agregarInicio(2)

#Agrego el tercer nivel
Nodo_a = Nivel2.cabeza
Nodo_a.hijos = Nivel3
Nivel3.agregarInicio(5)





"""a = ListaSE() #raiz
b = ListaSE() 
c = ListaSE() 
d = ListaSE() #hoja
e = ListaSE () #hoja
f = ListaSE() #hoja


b.agregarInicio(e)
b.agregarInicio(d)

c.agregarInicio(f)

a.agregarInicio(c)
a.agregarInicio(b)"""

