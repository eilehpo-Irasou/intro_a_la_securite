import random
sbox = [12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2]

xobs = [sbox.index(i) for i in range(0,16)]

## function round
def round(key,msg):
    return sbox [key^msg]


## If i wanted the 6th element from sbox, on terminal i will print 10
print(sbox[6])

### I test my round function

print(round(5,2))


##function enc

def enc(key, msg):
    t = round(key[0],msg)
    c = round(key[1],t)
    return c



##
print(enc([13,2],7))


## function back_round

def back_round(key,c):
    return xobs[c]^key


def dec(key,c):
    t = back_round(key[1],c)
    m = back_round(key[0],t)
    return m

key = [7,13]
a = dec(key,13)

print(a)
