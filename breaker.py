import time
from matplotlib import pyplot as plt
from RSA import *
import random

#breking RSA with known plaintext and ciphertext
def break_RSA_known_plaintext(n, e, c, m):
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

def test_break_RSA_known_plaintext():
    #generate keys
    public, private = generate_keys(30)
    #encrypt
    m = "hi s7"
    c = RSA_encrypt(m, public[0], public[1])
    #calculate time to break RSA with known plaintext and ciphertext
    start = time.time()
    #break
    broken =  break_RSA_known_plaintext(public[1], public[0], c, m)
    end = time.time()
    assert break_RSA_known_plaintext(public[1], public[0], c, m) == m
    print("Excellent! You broke RSA with known plaintext and ciphertext! broken = ", broken, " time = ", end - start)
test_break_RSA_known_plaintext()

#plot time to break RSA with known plaintext and ciphertext against key size
def plot_break_RSA_known_plaintext():
    #loop through key sizes
    for key_size in range(15, 35):
        #generate keys
        public, private = generate_keys(key_size)
        #encrypt
        m = "hi s7"
        c = RSA_encrypt(m, public[0], public[1])
        #break
        start = time.time()
        break_RSA_known_plaintext(public[1], public[0], c, m)
        end = time.time()
        print("Broken! key size = ", key_size, "  |   time = ", end - start)
        #plot
        plt.plot(key_size, end - start, 'r-')
    plt.show()
plot_break_RSA_known_plaintext()
