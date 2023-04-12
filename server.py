import socket
import RSA

HOST = '127.0.0.1'  # localhost
PORT = 8080  # any unreserved port number

# generate keys
(e, n), (d, n) = RSA.generate_keys()
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


# import socket
# import RSA
# HOST = '127.0.0.1'  # localhost
# PORT = 8080  # any unreserved port number
# #generate keys
# (e, n),(d,n) = RSA.generate_keys()
# print(f"e: {e}, n: {n}, d: {d}, n: {n}")
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     print(f'Connected by {addr}')
#     #send public key to client
#     conn.sendall(f"{e} {n}".encode('utf-8'))
#     data = conn.recv(1024)
#     client_public_key = data.decode('utf-8').split()[0]
#     print(f"Client public key: {client_public_key}")
#     client_n = data.decode('utf-8').split()[1]
#     print(f"Client n: {client_n}")
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             break        #decrypt message with private key
#         #convert message to list of ints
#         message = RSA.RSA_decrypt(data.decode('utf-8'), d, n)
#         message = data.decode('utf-8')
#         if message == "":
#             continue
#         print(f"Client: {message}")
#         message = input('Server: ')
#         if message == "":
#             continue
#         # encrypt message with public key from client
#         message = RSA.RSA_encrypt(message, int(client_public_key), int(client_n))
#         conn.sendall(message.encode('utf-8'))


# # echo-server.py

# import socket

# HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
# PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# #     s.bind((HOST, PORT))
# #     s.listen()
# #     conn, addr = s.accept()
# #     with conn:
# #         print(f"Connected by {addr}")
# #         while True:
# #             data = conn.recv(1024)
# #             if not data:
# #                 break
# #             conn.sendall(data)
# host = socket.gethostname()
# port = 5000  # initiate port no above 1024

# server_socket = socket.socket()  # get instance
# # look closely. The bind() function takes tuple as argument
# server_socket.bind((host, port))  # bind host address and port together

# # configure how many client the server can listen simultaneously
# server_socket.listen(2)
# conn, address = server_socket.accept()  # accept new connection
# print("Connection from: " + str(address))
# while True:
#     # receive data stream. it won't accept data packet greater than 1024 bytes
#     data = conn.recv(1024).decode()
#     if not data:
#         # if data is not received break
#         break
#     print("from connected user: " + str(data))
#     data = input(' -> ')
#     conn.send(data.encode())  # send data to the client

# conn.close()  # close the connection
