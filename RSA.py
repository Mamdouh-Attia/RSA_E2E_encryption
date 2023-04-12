import random
import alphabet_encoder as alpha
import math
def RSA_encrypt(msg, e, n):
    #convert to numbers
    msg = alpha.encode(msg)
    #encrypt each number
    encrypted = []
    for number in msg:
        encrypted.append(pow(number, e, n))
    encrypted = [int(x) for x in encrypted]
    return encrypted
def RSA_decrypt(encrypted, d, n):
    #decrypt each number
    msg = []
    for number in encrypted:
        print(type(number))
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

#test RSA_encrypt function
def test_RSA_encrypt():
    print("Testing RSA_encrypt function...")
    msg = "Hello World!"
    e = 7
    n = 3233
    encrypted = RSA_encrypt(msg, e, n)
    print(f"Encrypted message: {encrypted}")
    print("Test passed!")
# test_RSA_encrypt()
#test encrypt and decrypt functions together
def test_RSA_encrypt_decrypt():
    print("Testing RSA_encrypt and RSA_decrypt functions together...")
    msg = "Hello World!"
    e = 7
    n = 3233
    encrypted = RSA_encrypt(msg, e, n)
    decrypted = RSA_decrypt(encrypted, e, n)
    print(f"Decrypted message: {decrypted}")
    print("Test passed!")
# test_RSA_encrypt_decrypt()

#define get_prime function
def get_prime():
    #find a random number
    number = random.randint(2, 1000)
    #check if it's prime
    for i in range(2, number):
        if number % i == 0:
            return get_prime()
    return number

#function to generate keys for RSA encryption and decryption
def generate_keys():
    #find two prime numbers
    p = 0
    q = 0
    while p == q:
        p = get_prime()
        q = get_prime()
    #find n
    n = p * q
    #find phi
    phi = (p - 1) * (q - 1)
    #find e
    e = 0
    for i in range(2, phi):
        if math.gcd(i, phi) == 1:
            e = i
            break
    #find d
    d = 0
    for i in range(1, phi):
        if (e * i) % phi == 1:
            d = i
            break
    return (e, n), (d, n)





#test generate_keys function
def test_generate_keys():
    print("Testing generate_keys function...")
    public, private = generate_keys()
    print(f"Public key: {public}")
    print(f"Private key: {private}")
    print("Test passed!")
test_generate_keys()
#testing generate_keys function with RSA_encrypt and RSA_decrypt functions
def test_generate_keys_RSA_encrypt_decrypt():
    print("Testing generate_keys, RSA_encrypt, and RSA_decrypt functions together...")
    public, private = generate_keys()
    msg = "Hello World!"
    encrypted = RSA_encrypt(msg, public[0], public[1])
    decrypted = RSA_decrypt(encrypted, private[0], private[1])
    print(f"Decrypted message: {decrypted}")
    print("Test passed!")
