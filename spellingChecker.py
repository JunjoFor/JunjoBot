

def spellingChecker(message):
    resultado = message.replace('subnormal', 'gilipollas').replace('imbecil', 'gilipollas').replace('retrasado', 'gilipollas').replace('tonto', 'gilipollas')
    return resultado


def eliminarTildes(message):
    resultado = message.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ü', 'u').replace('ä', 'a')
    return resultado
