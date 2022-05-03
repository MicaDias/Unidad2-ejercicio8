from Conjunto import Cojunto
from Menu import Menu
if __name__=='__main__':
    conjuntoA=Cojunto()
    print("Cargar el conjunto A, para finalizar la carga ingrese 's' para salir")
    opcion='1'
    while opcion!='s':
        opcion=input("Ingrese un numero o's' para salir: ")
        if opcion!='s':
            conjuntoA.agregarNumero(int(opcion))
        else:
            print("Finalizo la carga del conjunto A.")
    menu=Menu()
    menu.lanzarMenu(conjuntoA)