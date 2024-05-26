def main():
    # Prueba tu decorador
    multiplicar(3, 4)


def registrar(func):
    def envoltura(*args, **kwargs):
        print(f'Llamando a {func.__name__} con argumentos {args} y kwargs {kwargs}')
        resultado = func(*args, **kwargs)
        print(f'{func.__name__} retornó {resultado}')
        return resultado

    return envoltura


@registrar
def multiplicar(x, y):
    return x * y


if __name__ == '__main__':
    main()
