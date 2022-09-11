def triangolo_positivo():
	for i in range(10):
	    for j in range(0, 10 - i):
	        print(end=" ")
	    for k in range(10 - i, 10):
	        print("*", end=" ")
	
	    print("")


def triangolo_invertido():
	for i in range(10):
	    for j in range(0, i):
	        print(end=" ")
	    for k in range(i, 10):
	        print("*", end=" ")
	
	    print("")



def triangolo_superior_izquierdo():
	for i in range(10):
	    for j in range(0, 10 - i):
	        print("*", end=" ")
	
	    print("")


def triangolo_de_esquina_inferior_izquierdo():
	for i in range(10):
	    for j in range(0, i):
	        print("*", end=" ")
	
	    print("")


def triangolo_superior_derecho():
	for i in range(10):
	    for j in range(0,i):
	        print(" ", end=" ")
	    for k in range(i,10):
	        print("*", end=" ")
	
	    print("")


def triangolo_más_bajo_crudo():
	for i in range(10):
	    for j in range(0, 10 - i):
	        print(" ", end=" ")
	    for k in range(10 - i, 10):
	        print("*", end=" ")
	
	    print("")


if __name__ == "__main__":
    print("\n")
    triangolo_positivo()
    print("\n")
