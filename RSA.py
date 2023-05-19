import random
import alphabet_encoder as alpha
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def miller_rabin(n, k=50):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_random_prime(bits):
    min_value = (2**(bits-1))//2
    max_value = (2**bits-1)//2
    while True:
        num = random.randint(min_value, max_value)
        if is_prime(num):
            return num
        elif miller_rabin(num):
            return num

#generate keys taking number of bits of n as input and returns public and private keys
def generate_keys(bits):
    #generate two prime numbers
    p =generate_random_prime(bits//2)
    q =generate_random_prime(bits//2)
    #calculate n
    n = p * q
    #calculate phi
    phi = (p - 1) * (q - 1)
    #calculate e
    e = 0
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    #calculate d
    d = extended_gcd(e, phi)[1]
    if d < 0:
        d = (d % phi + phi) % phi
    # print("e",e,"d",d,"n",n,"phi",phi)
    return (e, n), (d, n)
#Calculate extended euclidean algorithm to get multiplicative inverse of e
def extended_gcd(a,b):
    if b==0:
        # d=ax+by
        d,x,y=a,1,0
    else:
        (d,p,q)=extended_gcd(b,a%b)
        x=q
        y=p-q* (a//b)
    return (d,x,y)
def RSA_encrypt(msg, e, n):
    #convert to numbers
    msg = alpha.encode(msg)
    #encrypt each number
    encrypted = []
    for number in msg:
        encrypted.append(pow(number, e, n))
    return encrypted


def RSA_decrypt(encrypted, d, n):
    #decrypt each number
    msg = []
    #treat every number in encrypted corresponds to a list of 5 characters after decoding
    for number in encrypted:
        msg.append(pow(number, d, n))
    #convert back to letters
    return alpha.decode(msg)

def do7a_test():
        #generate keys
    bits=30
    p = generate_random_prime(bits)
    q = generate_random_prime(bits)
    # p = 9513367
    # q = 8192201
    public, private = generate_keys(bits)
    # public, private = (),()
    print("Public: ", public)
    print("Private: ", private)
    #encrypt a message
    msg = "password is : ktatis batatis"
    encrypted = RSA_encrypt(msg, public[0], public[1])
    print("Encrypted: ", encrypted)
    #decrypt the message
    decrypted = RSA_decrypt(encrypted, private[0], private[1])
    print("Decrypted:", decrypted)
# do7a_test()