from random import randint


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b//a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def mdc(a,b):
    if b == 0:
        return a
    return mdc(b, a % b)


def mmc(a,b):
    return abs(a*b) / mdc(a,b)


def isPrime(a):
    """Verifica se o numero e primo.
    
    Arguments:
        a {int} -- Numero.
    
    Returns:
        bool -- Se o valor e ou nao e primo.
    """
    c = 0
    for n in range(1, a + 1):
        if a % n is 0:
            c += 1
    return True if c is 2 else False


def chaves():
    """Gera as chaves necessarias para criptografia.
    
    Returns:
        list -- Lista com as chaves.
            formato de saida:
            [
                [keypublic1, keypublic2], 
                [keyprivate1, keyprivate3]
            ]

    """
    while True:
        keyprivate1 = randint(0, 2000)
        if isPrime(keyprivate1):
            break
    while True:
        keyprivate2 = randint(0, 2000)
        if isPrime(keyprivate2):
            break
    keypublic1 = keyprivate1 * keyprivate2
    determinante = int(mmc((keyprivate1 - 1),(keyprivate2 - 1)))
    while True:
        keypublic2 = randint(0, determinante)
        if isPrime(keypublic2):
            break
    keyprivate3 = modinv(keypublic2, determinante)

    return [[keypublic1, keypublic2], [keyprivate3]]

def encript(msg, keypublic1, keypublic2):
    """Encriptar a mensagem com RSA.

    Description:
        Converte os caracteres para decimal via ord,
        armazena um o resultado encontrado na variavel
        cript, que e percorrida por um for, e a cada 
        volta o valor correspondendo a posicao cript[c]
        sofre um reajuste de acordo com a criptografia 
        RSA, e o valor final e retornado em hexadecimal,
        por convencao.
    
    Arguments:
        msg {str} -- Mensagem a ser encriptada.
        keypublic1 {int} -- Chave publica 1.
        keypublic2 {int} -- Chave publica 2.
    
    Returns:
        str -- Hexadecimal representando a criptografia.

    """
    # Separa os caracteres da msg, e converte para ASCII
    l1 = list(map(ord, msg))
    cript = l1.copy()
    for c in range(0, len(l1)):
        cript[c] = cript[c] ** keypublic2 % keypublic1
    return ':'.join(list(map(hex, cript)))


def decript(hex_msg, keypublic1, keyprivate3):
    """Desencriptar a mensagem.

    Description:
        A mensagem em hexadecimal 'hex_msg' e remapeada
        para decimal por meior int(base=16), o resultado
        e copiado para decript que sofre modificacoes 
        de acordo com sua posicao durante a execucao do
        'for', o resultado e remapeado para chr e retornado
        em forma concatenada.
    
    Arguments:
        hex_msg {str} -- Mensagem encriptada em Hexadecimal.
        keypublic1 {int} -- Chave publica 1
        keyprivate3 {int} -- Chave privada 3
    
    Returns:
        str -- Mensagem desencriptada.

    """
    dec_msg = list(map(lambda x: int(x, base=16), hex_msg.split(':')))
    decript = dec_msg.copy()
    for c in range(0, len(dec_msg)):
        decript[c] = decript[c] ** keyprivate3 % keypublic1
    decript = list(map(chr, decript))
    return ''.join(decript)

if __name__ == "__main__":
    # Obter chaves
    c = chaves()

    # Encriptar mensagem
    cript_msg = encript("Alguma coisa muito grande!", *c[0])
    print(cript_msg)

    # Desencriptar mensagem
    decpt_msg = decript(cript_msg, c[0][0], c[1][0])
    print(decpt_msg)