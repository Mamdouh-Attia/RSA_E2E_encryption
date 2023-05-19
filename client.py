import socket
import RSA

HOST = '127.0.0.1'  # localhost
PORT = 8080  # the same port number used in server code
bits=30

# generate keys
(e, n), (d, n) = RSA.generate_keys(bits)
print(f"e: {e}, n: {n}, d: {d}, n: {n}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # receive public key from server
    data = s.recv(1024)
    server_public_key = int(data.decode('utf-8').split()[0])
    print(f"Server public key: {server_public_key}")
    server_n = int(data.decode('utf-8').split()[1])
    print(f"Server n: {server_n}")

    # send public key to server
    s.sendall(f"{e} {n}".encode('utf-8'))

    while True:
        message = input('Client: ')
        if message == "":
            continue

        # encrypt message with public key from server
        message = RSA.RSA_encrypt(message, server_public_key, server_n)

        # send message
        s.sendall(str(message).encode('utf-8'))

        # receive response from server
        data = s.recv(1024)
        if not data:
            break
        data_str = data.decode('utf-8')
        data_list = data_str.split(',')
        data_ints = [int(x.strip("[]")) for x in data_list]
        # decrypt message with private key
        message = RSA.RSA_decrypt(data_ints, d, n)
        print(f"Server: {message}")