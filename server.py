import socket
import RSA

HOST = '127.0.0.1'  # localhost
PORT = 8080  # any unreserved port number
bits=30
# generate keys
(e, n), (d, n) = RSA.generate_keys(bits)
print(f"e: {e}, n: {n}, d: {d}, n: {n}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f'Connected by {addr}')

    # send public key to client
    conn.sendall(f"{e} {n}".encode('utf-8'))
    #receive public key from client
    data = conn.recv(1024)
    client_public_key = int(data.decode('utf-8').split()[0])
    print(f"Client public key: {client_public_key}")
    client_n = int(data.decode('utf-8').split()[1])
    print(f"Client n: {client_n}")
     
    while True:
        data = conn.recv(1024)
        if not data:
            break
        data_str = data.decode('utf-8')
        data_list = data_str.split(',')
        data_ints = [int(x.strip("[]")) for x in data_list]
        # decrypt message with private key
        message = RSA.RSA_decrypt(data_ints, d, n)
        print(f"Client: {message}")

        message = input('Server: ')
        if message == "":
            continue

        # encrypt message with public key from client
        message = RSA.RSA_encrypt(message, client_public_key, client_n)
        # conn.sendall(message.encode('utf-8'))
        # message = RSA.RSA_encrypt(message, client_public_key, client_n)
        message_str = ','.join([str(x) for x in message])
        conn.sendall(message_str.encode('utf-8'))
