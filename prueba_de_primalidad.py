#Programa / Prueba si un número es primo o no.

def es_primo(numero):
    if numero <= 1: 
        return False
    else:
        for i in range(1,numero+1):
            if i == 1 or i == numero:
                continue
            if numero % i == 0:
                return False
        return True


def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('El número ' + str(numero) + ' es primo')
    else:
        print('El número ' + str(numero) + ' no es primo')


if __name__ == '__main__':
    run()