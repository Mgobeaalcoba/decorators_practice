def main():
    print(fib(10))
    print(fib(11))  # Debe ser rápido ya que fib(10) ya fue calculado


def memorizar(func):
    memoria = {}

    def envoltura(*args):
        if args in memoria:
            print(f'Usando resultado en caché para {args}')
            return memoria[args]
        resultado = func(*args)
        memoria[args] = resultado
        return resultado

    return envoltura


@memorizar
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    main()
