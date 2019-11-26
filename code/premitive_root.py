from math import sqrt


# Returns True if n is prime
def isPrime( n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def power( x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1  # y = y/2
        x = (x * x) % p

    #print(res)
    return res

def findPrimefactors(s, n) :

# Pr the number of 2s that divide n
  while (n % 2 == 0) :
    #print(2)
    s.add(2)
    n = n // 2

# n must be odd at this po. So we can
# skip one element (Note i = i +2)
  for i in range(3, int(sqrt(n)), 2):

# While i divides n, pr i and divide n
     while (n % i == 0) :
        #print(i)
        s.add(i)
        n = n // i

# This condition is to handle the case
# when n is a prime number greater than 2
  if (n > 2) :
       #print(n)
       s.add(n)

# Function to find smallest primitive
# root of n
def findPrimitive(n) :
    s = set()
    if (isPrime(n) == False):
        return -1

    phi = n - 1
    findPrimefactors(s, phi)
    for r in range(2, phi + 1):
        flag = False
        for it in s:
            if (power(r, phi // it, n) == 1):
                flag = True
                break

        if (flag == False):
            return r

    return -1

#n = 761
#print("Smallest primitive root of", n, "is", findPrimitive(n))
