from sys import exit
__version__ = f'Vers: Alpha {0.1}'
__licence__ = str(   "\t\t\tApache License\n"
                "\t\t  Version 2.0, January 2004\n"
                "\t\thttp://www.apache.org/licenses/\n")

__copyright__ = 'Copyright 2026 RgeditV1'

__arguments__ = {'--version'    : __version__,
                 '--licence'    :__licence__,
                 '--copyright'  :__copyright__}


def parsedOptions(args: list):
    '''CONTROLA LAS OPCIONES POR LINEA DE COMANDO'''
    argv_list = [a for a in args]
    for arg in argv_list:
        if arg in __arguments__:
            show = __arguments__.get(arg)
            print(show)
        else:
            raise KeyError(f'No Existe el argumento {arg}')
    return exit()

