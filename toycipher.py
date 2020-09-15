import random
import os
sbox = [9, 11, 12, 4, 10, 1, 2, 6, 13, 7, 3, 8, 15, 14, 0, 5]
xobs = [14, 5, 6, 10, 3, 15, 7, 9, 11, 0, 4, 1, 2, 8, 13, 12]

def enc (m, key):
    t = sbox[m ^ key[0]]
    c = sbox[t ^ key[1]]
    return c

def dec (c, key):
    t = xobs[c] ^ key[1]
    m = xobs[t] ^ key[0]
    return m




#exercice 1
# famille : chiffrement symétrique, chriffrement par bloc 
#construction : reseau de subtition et permutation 
# 4 bits
#2 tours 
#taille de la clé 8 bits
# on ajout la clé avec xor , puis on passe dans la boite S

# transition ; juste passer la boite s 
# permutation ; 




#exer2

def tc_1r(m,k):
    return sbox[m^k]


def attack_tc1r(m,c):
    return xobs[c]^m


def tc(m,key):
    t= sbox[m^k[0]]
    c = sbox[t^k[1]]
    return c 

#3
#16

# ça ne marche pas , on a une dépendance 

#4
# par force brut en 512 etape , c'est faux

# 5
#
m = random.randint(0,15)
key = random.randint(0,15),random.randint(0,15)
c = enc(m,key)



for k0 in range(0,16):
    for k1 in range(0,16):
        if c == enc(m,(k0,k1)):
            print((k0,k1))
