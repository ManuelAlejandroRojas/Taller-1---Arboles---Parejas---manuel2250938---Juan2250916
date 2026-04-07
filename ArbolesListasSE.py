# Clase Nodo
class Nodo:
	def __init__(self, data):
		self.data = data
		self.siguiente = None

# CLase Listas enlazada simple
class ListaSE:
	def __init__(self):
		self.cabeza = None
		
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
			

a = ListaSE() #raiz
b = ListaSE() 
c = ListaSE() 
d = ListaSE() #hoja
e = ListaSE () #hoja
f = ListaSE() #hoja


b.agregarInicio(e)
b.agregarInicio(d)

c.agregarInicio(f)

a.agregarInicio(c)
a.agregarInicio(b)

