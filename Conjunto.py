class Cojunto:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    
    def agregarNumero(self,num):
        if type(num)==int:
            if num not in self.__lista:
                self.__lista.append(num)
        else:
            print("No se pudo agregar al conjunto")
    def __str__(self):
        cadena=''
        bandera=True
        for numero in self.__lista:
            if bandera:
                cadena=str(numero)
                bandera=not bandera
            else:
                cadena=cadena+','+str(numero)
        cadena='{'+cadena+'}'
        return cadena
    
    def consultarValor(self,numero):
        return numero in self.__lista
    def __sub__(self,conjuntoB):
        cojuntoResultado=Cojunto()
        for numero in self.__lista:
            if(not conjuntoB.consultarValor(numero)):
                cojuntoResultado.agregarNumero(numero)
        return cojuntoResultado   
    def longitud(self):
        return len(self.__lista)
    def __eq__(self,conjuntoB):
        resultado=False
        i=0
        lon=len(self.__lista)
        bandera=True
        if len(self.__lista)==conjuntoB.longitud():
            while i <lon and bandera:
                if conjuntoB.consultarValor(self.__lista[i]):
                    i+=1
                else:
                    bandera=not bandera 
            if bandera:
                resultado=True
        return resultado        
    def cargarValores(self,conjuntoC):
        for num in self.__lista:
            conjuntoC.agregarNumero(num)
    def __add__(self,conjuntoB):
        conjuntoC=Cojunto()
        self.cargarValores(conjuntoC)
        conjuntoB.cargarValores(conjuntoC)
        return conjuntoC
    def funcionTest(self):
        conjunto1=Cojunto()
        conjunto2=Cojunto()
        conjunto3=Cojunto()
        print("****Funcion test Conjunto****")
        print("Metodo agregarNumero()")
        conjunto1.agregarNumero(1)
        conjunto1.agregarNumero(2)
        conjunto1.agregarNumero(3)
        for i in range(4,0,-1):
            conjunto2.agregarNumero(i)
        print("Conjunto A={}, Cojunto B={}".format(conjunto1,conjunto2))
        print("Metodo consultarValor")
        print(conjunto2.consultarValor(4))
        print("Metodo unir conjuntos:")
        print("A+B={}".format(conjunto1+conjunto2))
        print("Metodo diferencia de conjuntos")
        print("A-B={}".format(conjunto1-conjunto2))
        print("Metodo verificar igualdad")
        print(conjunto1==conjunto2)
        print("Metodo longitud")
        print("Cantidad de elementos del conjunto A:{}".format(conjunto1.longitud()))
        print("Metodo cargarValores")
        conjunto1.cargarValores(conjunto3)
        print(conjunto3)
