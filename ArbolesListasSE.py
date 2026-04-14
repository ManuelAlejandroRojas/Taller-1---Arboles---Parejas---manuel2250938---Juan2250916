#Trabajo de: 
# Manuel Alejandro Rojas Sierra - 2250938
# Juan David Castro Pacheco 2250916

# Clase Nodo
class Nodo:
	def __init__(self, data):
		self.data = data
		self.siguiente = None
		self.hijos = None

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



	#Recorrer el árbol hasta encontrar el dato buscado (Nodo que será el padre)
	def buscar_nodo(self, nodo_actual, dato_buscado):
		if nodo_actual is None:
			return None

		if nodo_actual.data == dato_buscado:
			return nodo_actual

		encontrado = self.buscar_nodo(nodo_actual.hijos, dato_buscado)
		if encontrado is not None:
			return encontrado
		
		return self.buscar_nodo(nodo_actual.siguiente, dato_buscado)

		

	#Funcion para agregar nodos
	def Agregar_nodo_al_padre(self, dato_padre, dato_nuevo):
		# Buscar el padre
		padre = self.buscar_nodo(self.cabeza, dato_padre)

		if padre is None:
			print("No se encontró el padre")
			return None

		nuevo_nodo = Nodo(dato_nuevo)

		# Si no tiene hijos, el nuevo nodo será el primero
		if padre.hijos is None:
			padre.hijos = nuevo_nodo
			return nuevo_nodo

		# Si ya tiene hijos, irá al último hermano
		N_actual = padre.hijos
  
		while N_actual.siguiente is not None:
			N_actual = N_actual.siguiente

		N_actual.siguiente = nuevo_nodo
		return nuevo_nodo


	#calcular grado del nodo actual
	def Calcular_grado(self, nodo_actual):
		if nodo_actual is None:
			return 0
   
		# Si el nodo actual tiene hijos
		if nodo_actual.hijos is not None:
			HijoActual = nodo_actual.hijos
			CuentaHijos = 0
											
		#Entonces saco una variable que mire los hijos y otra que me permita contar cuantos hijos tiene en el bucle:
			while HijoActual is not None:
				CuentaHijos += 1
				HijoActual = HijoActual.siguiente

			return CuentaHijos

		#Si no hay hijos, entonces tiene 0 hijos xd
		if nodo_actual.hijos is None:
			CuentaHijos = 0
			return CuentaHijos


	#calcular orden del árbol
	def calcular_orden(self, nodo_actual):
		if nodo_actual is None:
			return 0

		# Orden provisional: cuantos hijos tiene este nodo
		orden_maximo = self.Calcular_grado(nodo_actual)

		# Revisar cada hijo de este nodo
		hijo_actual = nodo_actual.hijos
		while hijo_actual is not None:
			orden_hijo = self.calcular_orden(hijo_actual)

			if orden_hijo > orden_maximo:
				orden_maximo = orden_hijo

			hijo_actual = hijo_actual.siguiente

		return orden_maximo
	

	def calcular_altura(self, nodo_actual):

		# Caso arbol vacío
		if nodo_actual is None:
			return 0

		# Caso hoja 
		if nodo_actual.hijos is None:
			return 1

		# Caso si tiene hijos
		max_altura = 0
		hijo_actual = nodo_actual.hijos

		while hijo_actual is not None:

			altura_hijo = self.calcular_altura(hijo_actual)

			if altura_hijo > max_altura:
				max_altura = altura_hijo

			hijo_actual = hijo_actual.siguiente

		return 1 + max_altura


	def calcular_peso(self, nodo_actual):

		# Caso base
		if nodo_actual is None:
			return 0

		total = 1  # contar el nodo actual

		hijo_actual = nodo_actual.hijos

		while hijo_actual is not None:

			total += self.calcular_peso(hijo_actual)

			hijo_actual = hijo_actual.siguiente

		return total






#Bienvenida e inicio
Arbol = ListaSE()
print("Bienvenido al creador de árboles, ingrese la raíz")
Arbol.agregarInicio(input("Elemento: "))

Continuacion = "n"

while True:

	#Menú principal

	print("\n¿Qué desea hacer?")
	print("1. Agregar un nodo")
	print("2. Calcular orden del árbol")
	print("3. Calcular altura del árbol")
	print("4. Calcular el peso del árbol")
	print("5. Salir")
	
	# Leer opción del usuario
	Eleccion = int(input("Seleccione una opción: "))

	match Eleccion:
		case 1:
			# Agregar nodos al árbol 
			Continuacion = "s"
			while Continuacion == "s":
				dato_padre = input("Ingrese el dato del nodo padre: ")
				dato_nuevo = input("Ingrese el dato del nuevo nodo: ")
				Arbol.Agregar_nodo_al_padre(dato_padre, dato_nuevo)

				# Preguntar si desea agregar otro nodo
				Continuacion = input("Desea agregar otro nodo? (s/n) ").lower()

				try:
					Continuacion = str(input("Desea agregar otro nodo? (s/n) ").lower())

				except ValueError:
					print("Entrada no válida, por favor ingrese 's' o 'n'")
					Continuacion = input("Desea agregar otro nodo? (s/n) ").lower()
					

				if Continuacion == "n":
					print("Saliendo del ingreso de nodos...")
					break

		case 2:
			# Calcular orden del árbol 
			orden = Arbol.calcular_orden(Arbol.cabeza)
			print(f"El orden del árbol es: {orden}")

		case 3:
			# Calcular altura del árbol
			altura = Arbol.calcular_altura(Arbol.cabeza)
			print(f"La altura del árbol es: {altura}")

		case 4:
			# Calcular peso del árbol
			peso = Arbol.calcular_peso(Arbol.cabeza)
			print(f"El peso del árbol es: {peso}")

		case 5:
			# Salir del programa
			print("Saliendo...")
			break

		case _:
		
			print("Opción no válida, por favor seleccione una opción del 1 al 5")
			Eleccion = int(input("Seleccione una opción: "))