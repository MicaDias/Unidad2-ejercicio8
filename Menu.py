from Conjunto import Cojunto
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.salir
            }
    def lanzarMenu(self,conjunto):
        #Menu opciones
        if type(conjunto)==Cojunto:
            i=str(len(self.__opciones))
            opcion=0
            while(i!=opcion):
                print('Menu:')
                print('-Ingrese 1:Unir conjuntos.')
                print('-Ingrese 2: Diferenciar conjuntos.')
                print('-Ingrese 3: Verificar igualdad de conjuntos.')
                print('-Ingrese 4: Funcion test.')
                print('-Ingrese 5: Salir.')
                opcion=input('Ingrese opcion:\n')
                ejecutar=self.__opciones.get(opcion,self.error)
                if (opcion=='1'or opcion=='2' or opcion=='3'or opcion=='4'):
                    ejecutar(conjunto)
                else:
                    ejecutar()
    def cargarConjuntoB(self):
        print("Cargar conjunto B")
        conjuntoB=Cojunto()
        opc='1'
        while opc!='s':
            opc=input("Ingrese un numero o la opcion 's' para salir: ")
            if opc!='s':
                conjuntoB.agregarNumero(int(opc))
            else:
                print("Finalizo la carga del conjunto B")
        return conjuntoB
    def opcion1(self,conjunto):
        conjuntoB=self.cargarConjuntoB()
        conjuntoRes=conjunto+conjuntoB
        print("Union del conjunto A={} y conjunto B{} es A+B{}".format(conjunto,conjuntoB,conjuntoRes))
    def opcion2(self,conjunto):
        conjuntoB=self.cargarConjuntoB()
        conjuntoC=conjunto-conjuntoB
        print("Diferencia de dos conjuntos: A={},B={},A-B={}".format(conjunto,conjuntoB,conjuntoC))
    def opcion3(self,conjunto):
        conjuntoB=self.cargarConjuntoB()
        res=conjunto==conjuntoB
        if res:
            print("El conjunto A={} y el conjunto B={} son iguales".format(conjunto,conjuntoB))
        else:
            print("El conjunto A={} y el conjunto B={} son distintos".format(conjunto,conjuntoB))  
    def opcion4(self,conjunto):
       conjunto.funcionTest()
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')
    