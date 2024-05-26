def main():
    # Prueba tu decorador
    ver_datos(usuario='admin')
    ver_datos(usuario='invitado')


def verificar_acceso(func):
    def envoltura(*args, **kwargs):
        usuario = kwargs.get('usuario')
        if usuario == 'admin':
            return func(*args, **kwargs)
        else:
            print('Acceso denegado.')
            return None

    return envoltura


@verificar_acceso
def ver_datos(usuario=None):
    print('Mostrando datos confidenciales.')


if __name__ == '__main__':
    main()
