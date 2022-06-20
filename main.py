from Arbol import Arbol

def main():
	abb = Arbol()
	abb.insertar(10)
	abb.insertar(24)
	abb.insertar(7)
	abb.insertar(17)
	abb.insertar(27)
	abb.insertar(4)
	print("PreOrden")
	abb.preOrden(abb.raiz)
	print("InOrden")
	abb.inOrden(abb.raiz)
	print("PostOrden")
	abb.postOrden(abb.raiz)

if __name__ == "__main__":
	main()
