
puta = False


def spellingChecker(message):
    resultado = message.replace('subnormal', 'gilipollas').replace('imbecil', 'gilipollas').replace('retrasado', 'gilipollas')
    return resultado


def eliminarTildes(message):
    resultado = message.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    return resultado
