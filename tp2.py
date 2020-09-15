
from Crypto.Util.number import getPrime, inverse
import os,sys, math

## chaque element de la paire
## va donner deux nombres premiers aleatoirement
## d clé privée
## e et n clé publique

## q2
## n/2

def gen_rsa_keypair(bits):
    #3
    p = getPrime(bits//2)
    q = getPrime(bits//2)
    n = p*q
    phi_n = (p-1)*(q-1)
    #4
    e = 65537
    assert(math.gcd(e,phi_n) == 1)
    d = inverse (e, phi_n)
    return ( (e,n), (d,n) )
## (e,n) clé publique
## (d,n) clé privée

a =gen_rsa_keypair(64)
print(a)
