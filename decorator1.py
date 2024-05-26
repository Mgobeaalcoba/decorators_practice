import time


def main():
    # Llamamos a la función decorada
    resultado = suma(3, 5)
    print(f'Resultado de la suma: {resultado}')


def medir_tiempo(func: callable) -> callable:
    print(f'Función a decorar: {func.__name__}')

    def envoltura(*args, **kwargs):
        print(f'args: {args}')
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f'La función {func.__name__} tardó {fin - inicio:.4f} segundos en ejecutarse.')
        return resultado

    print(f'Función decorada: {envoltura.__name__}')
    return envoltura


@medir_tiempo
def suma(a, b):
    time.sleep(1)  # Simulamos una operación costosa
    return a + b


if __name__ == '__main__':
    main()
