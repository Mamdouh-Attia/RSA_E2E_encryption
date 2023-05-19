from RSA import *
#test RSA_encrypt function
def test_RSA_encrypt():
    print("Testing RSA_encrypt function...")
    msg = "Hello World"
    e = 7
    n = 3233
    encrypted = RSA_encrypt(msg, e, n)
    print(f"Encrypted message: {encrypted}")
    print("Test passed!")
#test encrypt and decrypt functions together
def test_RSA_encrypt_decrypt():
    print("Testing RSA_encrypt and RSA_decrypt functions together...")
    msg = "Hello World"
    e = 7
    n = 3233
    encrypted = RSA_encrypt(msg, e, n)
    decrypted = RSA_decrypt(encrypted, e, n)
    print(f"Decrypted message: {decrypted}")
    print("Test passed!")
# test_RSA_encrypt_decrypt()


#test generate_keys function
def test_generate_keys():
    print("Testing generate_keys function...")
    public, private = generate_keys(40)
    print(f"Public key: {public}")
    print(f"Private key: {private}")
    print("Test passed!")
#validate that the keys work
def test_generate_keys_RSA_encrypt():
    print("Testing generate_keys and RSA_encrypt functions together...")
    public, private = generate_keys(40)
    msg = "Hello World"
    encrypted = RSA_encrypt(msg, public[0], public[1])
    print(f"Encrypted message: {encrypted}")
    print("Test passed!")
#test function to encrypt message
def test_RSA_encrypt():
    print("Testing RSA_encrypt function...")
    msg = "Hello World"
    e = 7
    n = 3233
    encrypted = RSA_encrypt(msg, e, n)
    print(f"Encrypted message: {encrypted}")
    print("Test passed!")
#test function to decrypt message
def test_RSA_decrypt():
    print("Testing RSA_decrypt function...")
    msg = "Hello World"
    e = 7
    n = 3233
    d = 413
    encrypted = RSA_encrypt(msg, e, n)
    decrypted = RSA_decrypt(encrypted, d, n)
    print(f"Decrypted message: {decrypted}")
    print("Test passed!")
# test_RSA_decrypt()
# test_generate_keys_RSA_encrypt()
#validate that rsa_encrypt and rsa_decrypt work together
def test_RSA_encrypt_decrypt():
    print("Testing RSA_encrypt and RSA_decrypt functions together...")
    msg = "Hello World"
    e = 7
    n = 3233
    d = 413
    encrypted = RSA_encrypt(msg, e, n)
    decrypted = RSA_decrypt(encrypted, d, n)
    print(f"Decrypted message: {decrypted}")
    print("Test passed!")
#testing generate_keys function with RSA_encrypt and RSA_decrypt functions
def test_generate_keys_RSA_encrypt_decrypt():
    print("Testing generate_keys, RSA_encrypt, and RSA_decrypt functions together...")
    public, private = (7,33),(3,33)
    # print (f"Public key: {public[0]},{public[1]}")
    msg = "Hello"
    encrypted = RSA_encrypt(msg, public[0], public[1])
    decrypted = RSA_decrypt(encrypted, private[0], private[1])
    assert msg == decrypted, "Error: Original message : "+msg+" and decrypted message: "+decrypted+" don't match"
    print("Test passed!")
# test_generate_keys()
# test_RSA_encrypt()
# test_RSA_encrypt_decrypt()
# test_generate_keys_RSA_encrypt_decrypt()
