import alphabet_encoder as alpha
import math
import random

def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    """Generate a prime number between min_value and max_value"""
    while True:
        num = random.randint(min_value, max_value)
        if is_prime(num):
            return num

def generate_keys(p, q):
    """Generate RSA public and private keys"""
    n = p * q
    phi = (p-1) * (q-1)
    e = 2
    while math.gcd(e, phi) != 1:
        e += 1
    d = pow(e, -1, phi)
    return (e, n), (d, n)

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
    for number in encrypted:
        msg.append(pow(number, d, n))
    #convert back to letters
    return alpha.decode(msg)

def break_RSA(n, e, c):
    #find p and q
    p = 0
    q = 0
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            p = i
            q = n // i
            break
    #find phi
    phi = (p - 1) * (q - 1)
    #find d
    d = 0
    for i in range(1, phi):
        if (e * i) % phi == 1:
            d = i
            break
    #decrypt
    return RSA_decrypt(c, d, n)

# Generate RSA public and private keys
p = generate_prime(1000, 10000)
q = generate_prime(1000, 10000)
public_key, private_key = generate_keys(p, q)
print("Public key:", public_key,"private_key:", private_key)

# Encrypt a message using the public key
message = "hello world"
encrypted = RSA_encrypt(message, public_key[0], public_key[1])

# Decrypt the message using the private key
decrypted = RSA_decrypt(encrypted, private_key[0], private_key[1])
print(decrypted)
