import random
import premitive_root
import Crypto.Util.number as num


def generate_rand_prime(x, y):
    primes = [i for i in range(x, y) if premitive_root.isPrime(i)]
    n = random.choice(primes)
    return n


def generate_User_public_private_key():
    q = generate_rand_prime(2, 8000)
    alpha = premitive_root.findPrimitive(q)

    print("q :", q)
    print("alpha :", alpha)

    # first step choose X_A
    X_A = random.randint(2, q)
    print("X_A :", X_A)

    # calculate Y_A
    Y_A = (pow(alpha, X_A)) % q
    print("Y_A : ", Y_A)

    # pair of private/public key
    private_key = X_A

    public_key = [q, alpha, Y_A]

    print("private_key : ", private_key)
    print("public_key  : ", public_key)

    return [private_key, public_key]


def get_e(phi):
    e = 0
    check = True
    while (check):
        temp = random.randint(2, phi)
        if (num.GCD(temp, phi) == 1):
            check = False
            e = temp
    return e


def generate_rsa_keys():
    p = num.getPrime(100)
    q = num.getPrime(100)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = get_e(phi)
    d=  num.inverse(e,phi);
    return [n, e,d]


#key = generate_User_public_private_key()

#print("private key :", key[0])
#print("public key :", key[1])
