'''
Modulo Arbol.py
'''

# se importa la clase Nodo del archivo nodo.py
from Nodo import Nodo

class Arbol:

	'''
	Metodo constructor

	Se inicializa el atributo raiz con el valor None por defecto
	'''
	def __init__(self):
		self.raiz = None

	'''
	funcion insertar():

	Funcion para insertar un dato en el arbol:

	1.- se guarda la raiz actual en la variable aux
	2.- Luego, mientras la variable auxiliar sea 'None' y la funcion puedeSerPadre de la clase Nodo devuelve False
	pasa lo siguiente:
		- si la raiz es menor que el valor, entonces el valor se inserta a la derecha
		- de lo contrario, el valor se inserta a la izquierda
	3.- Luego se crea un objeto de la clase Nodo denominada 'nuevo' y se guarda el valor a ingresar
	en la raiz de este objeto
	4.- Finalmente:
		- Si el valor de 'aux' es None, entonces se actualiza la raiz del arbol actual
		con el objeto del nuevo valor
		- de lo contrario, entonces se inserta el valor mediante el metodo insertar()
	'''
	def insertar(self, valor):
		aux = self.raiz
		while aux != None and aux.puedeSerPadre(valor)==False:
			if aux.raiz < valor:
				aux = aux.der
			else:
				aux = aux.izq
		nuevo = Nodo()
		nuevo.raiz = valor
		if aux == None:
			self.raiz = nuevo
		else:
			aux.insertar(nuevo)

	'''
	funcion preOrden():

	A partir de un nodo raiz, hace un recorrido recursivo y va imprimiendo en pantalla los valores.

	A nivel teorico hace el recorrido desde el nodo raiz hacia distintos sub-arboles de la siguiente manera:
	nodo raiz, nodo izquierdo, nodo derecho.

	Mas informacion: https://es.wikipedia.org/wiki/%C3%81rbol_binario#Recorrido_en_preorden
	'''
	def preOrden(self, nodo):
		print(nodo.raiz)
		if nodo.izq != None:
			self.preOrden(nodo.izq)
		if nodo.der != None:
			self.preOrden(nodo.der)

	'''
	funcion inOrden():

	A partir de un nodo raiz, hace un recorrido recursivo y va imprimiendo en pantalla los valores.

	A nivel teorico hace el recorrido desde el nodo raiz hacia distintos sub-arboles de la siguiente manera:
	nodo izquierdo, nodo raiz, nodo derecho

	Mas informacion: https://es.wikipedia.org/wiki/%C3%81rbol_binario#Recorrido_en_inorden
	'''
	def inOrden(self, nodo):
		if nodo.izq != None:
			self.inOrden(nodo.izq)
		print(nodo.raiz)
		if nodo.der != None:
			self.inOrden(nodo.der)

	'''
	funcion postOrden():

	A partir de un nodo raiz, hace un recorrido recursivo y va imprimiendo en pantalla los valores.

	A nivel teorico hace el recorrido desde el nodo raiz hacia distintos sub-arboles de la siguiente manera:
	nodo izquierdo, nodo derecho, nodo raiz

	Mas informacion: https://es.wikipedia.org/wiki/%C3%81rbol_binario#Recorrido_en_postorden
	'''
	def postOrden(self, nodo):
		if nodo.izq != None:
			self.postOrden(nodo.izq)
		if nodo.der != None:
			self.postOrden(nodo.der)
		print(nodo.raiz)
