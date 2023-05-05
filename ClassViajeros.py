class ViajeroFrecuente:

    def __init__(self, num=0, dni='', nom='', ape='', milla=0):
        self.__num_viajero = int(num)
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ape
        self.__millas_acum = int(milla)

    def cantidadTotaldeMillas(self):
        return self.__millas_acum

    def acumularMillas(self, milla_re):
        self.__millas_acum += milla_re

    def canjearMillas(self, can):
        if self.__millas_acum >= can:
            self.__millas_acum -= can
        else:
            print('Error en la operación')

        return self.__millas_acum

    def getnum(self):
        return self.__num_viajero

    def gettodo(self):
        return self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum
