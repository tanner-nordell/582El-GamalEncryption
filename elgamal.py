import random

from params import p
from params import g

def keygen():
    sk = random.SystemRandom().randint(1, pow(2, 2048))
    pk = pow(g, sk, p)
    return pk, sk

def encrypt(pk,m):
    q = (p-1)/2
    r = random.SystemRandom().randint(1, q)
    c1 = pow(g, r, p)
    c2 = (pow(pk, r, p) * (m % p)) % p #this might need some tweaking
    return [c1, c2]

def decrypt (sk, c):
    m = (c[1] * pow(c[0], p-1-sk, p)) % p
    return m

