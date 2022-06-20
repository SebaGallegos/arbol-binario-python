'''
Modulo para utilizar con el archivo Arbol.py
'''

class Nodo:

	'''
	Metodo constructor

	Se inicializan por defecto los 3 atributos:

	raiz -> nodo padre (se inicializa con 0)
	izq -> nodo hijo izquierdo (se inicializa con None)
	der -> nodo hijo derecho (se inicializa con None)
	'''
	def __init__(self):
		self.raiz = 0
		self.izq = None
		self.der = None

	'''
	funcion insertar():

	Inserta un nodo nuevo de la siguiente forma:

	1.- Si el valor de la raiz del nodo actual es menor al valor de
	la raiz del nodo nuevo a insertar, entonces se inserta el nuevo nodo
	en la posicion del nodo hijo derecho del nodo actual

	2.- De lo contrario, se inserta el nuevo nodo
	en la posicion del nodo hijo izquierdo del nodo actual
	'''
	def insertar(self, nodo_nuevo):
		if self.raiz < nodo_nuevo.raiz:
			self.der = nodo_nuevo
		else:
			self.izq = nodo_nuevo

	'''
	funcion puedeSerPadre():

	A partir de un valor ingresado:

	1.- Si la raiz es menor que el valor ingresado y si el nodo hijo derecho
	es None, devuelve 'True', lo que significa que el nodo actual puede ser padre, en caso
	contrario devuelve 'False', lo que significa que el nodo actual no puede ser padre.

	2.- Si la raiz es mayor que el valor ingresado y si el nodo hijo iquierdo
	es None, devuelve 'True', lo que significa que el nodo actual puede ser padre, en caso
	contrario devuelve 'False', lo que significa que el nodo actual no puede ser padre.
	'''
	def puedeSerPadre(self, valor):
		if self.raiz < valor:
			if self.der == None:
				return True
			return False
		else:
			if self.izq == None:
				return True
			return False
