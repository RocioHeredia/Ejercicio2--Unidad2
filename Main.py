from Manejador import Manejador


def menu():
    print('Opciones')
    print('a- Consultar Cantidad de Millas.')
    print('b- Acumular Millas.')
    print('c- Canjear Millas.')
    print('d- Salir')


def FuncionOpciones(opc, lis, posi):
    while opc <= 'c':
        if lis:
            if opc == 'a':
                print('Cantidad de millas acumuladas: {}'.format(p[posi].cantidadTotaldeMillas()))

            elif opc == 'b':
                a = int(input('Ingrese millas para acumularlas con las demas: '))
                p[posi].acumularMillas(a)
                print('Millas acumuladas: {}'.format(p[posi].cantidadTotaldeMillas()))
            elif opc == 'c':
                can = int(input('Ingrese millas para canjearlas con las demas: '))
                p[posi].canjearMillas(can)
                print('Millas acumuladas despues del canje: {}'.format(p[posi].cantidadTotaldeMillas()))

        opc = input('Ingrese otra opcion:')


if __name__ == '__main__':
    m = Manejador()
    p = m.leer_arch()
    num = int(input('Ingrese numero del viajero:'))
    while num != 0:
        pos = m.buscaviajero(num)
        if pos is not None:
            menu()
            op = input('Ingrese su opcion:')
            FuncionOpciones(op, p, pos)
        else:
            print('viajero no encontrado')
        num = int(input('Ingrese numero del viajero:'))
    m.almacenMemoria()