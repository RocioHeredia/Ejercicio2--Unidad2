from ClassViajeros import ViajeroFrecuente
import csv


class Manejador:

    def __init__(self):
        self.__lista = []

    def leer_arch(self):
        archivo = open("Viajeros.csv")
        reader = csv.reader(archivo, delimiter=";")

        for fila in reader:
            vf = fila
            viajero = ViajeroFrecuente(vf[0], vf[1], vf[2], vf[3], vf[4])
            self.__lista.append(viajero)
        archivo.close()
        return self.__lista

    def buscaviajero(self, num):
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].getnum() == num:
                return i

            i += 1

    def mostrar(self, pos):
        print(self.__lista[pos].gettodo())

    def almacenMemoria(self):
        print("Representacion del almacenamiento en memoria para la lista cargada con 4 viajeros.")
        for i in range(4):
            viajero = self.__lista[i]
            print(viajero.gettodo())