from random import choice

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


def isPrime(n):
    """Verifica se o numero e primo.
    
    Arguments:
        a {int} -- Numero.
    
    Returns:
        bool -- Se o valor e ou nao e primo.
    """
    if any(n % p == 0 and n != p for p in [2, 3, 5, 7]):
        return False

    return False if n == 1 else True


def getPrimeRange(limite):
    return list(filter(isPrime, range(limite+1)))


def chaves():
    """Gera as chaves necessarias para criptografia.
    
    Returns:
        list -- Lista com as chaves.
            formato de saida:
            [
                [public_key1, public_key2], 
                [private_key1, private_key3]
            ]

    """
    primos = getPrimeRange(2000)
    private_key1, private_key2 = choice(primos), choice(primos)
    public_key1 = private_key1 * private_key2
    determinante = int(mmc((private_key1 - 1),(private_key2 - 1)))
    public_key2 = choice(getPrimeRange(determinante))
    private_key3 = modinv(public_key2, determinante)

    return [[public_key1, public_key2], [public_key1, private_key3]]

def encript(msg, key1, key2):
    """Encriptar a mensagem com RSA.

    Arguments:
        msg {str} -- Mensagem a ser encriptada.
        key1 {int} -- Chave publica 1.
        key2 {int} -- Chave publica 2.
    
    Returns:
        str -- Hexadecimal representando a criptografia.

    """
    # Separa os caracteres da msg, e converte para ASCII
    l1 = list(map(ord, msg))
    cript = l1.copy()
    for c in range(0, len(l1)):
        cript[c] = cript[c] ** key2 % key1
    return ':'.join(list(map(hex, cript)))


def decript(hex_msg, key1, key2):
    """Desencriptar a mensagem.

    Arguments:
        hex_msg {str} -- Mensagem encriptada em Hexadecimal.
        key1 {int} -- Chave privada 1
        key2 {int} -- Chave privada 2
    
    Returns:
        str -- Mensagem desencriptada.

    """
    dec_msg = list(map(lambda x: int(x, base=16), hex_msg.split(':')))
    decript = dec_msg.copy()
    for c in range(0, len(dec_msg)):
        decript[c] = decript[c] ** key2 % key1
    decript = list(map(chr, decript))
    return ''.join(decript)

if __name__ == "__main__":
    # print(getPrimeRange(100000))
    print(chaves())