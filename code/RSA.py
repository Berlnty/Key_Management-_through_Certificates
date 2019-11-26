import random
from math import gcd
import binascii
import Crypto.Util.number as num

def get_e(phi):
    e = 0
    check = True
    while (check):
        temp = random.randint(2, phi)
        if (gcd(temp, phi) == 1):
            check = False
            e = temp
    return e


def Key_generation(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = get_e(phi)

    d = num.inverse(e, phi)  # private key

    return n, e, d


def encrypt(message, d, n):

    hex_data = binascii.hexlify(message.encode())
    plain_text = int(hex_data, 16)
    if plain_text > n:
        raise Exception('plain text too large for key')

    encrypted_text = pow(plain_text, d, n)
    return encrypted_text


def decrypt(encrypted_text, n, e):
    decrypted_text = pow(encrypted_text, e, n)
    message = binascii.unhexlify(hex(decrypted_text)[2:]).decode('ISO-8859-1')
    return message


'''
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

'''