import socket
import RSA

HOST = '127.0.0.1'  # localhost
PORT = 8080  # the same port number used in server code

# generate keys
(e, n), (d, n) = RSA.generate_keys()
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

# import socket
# import RSA
# HOST = '127.0.0.1'  # localhost
# PORT = 8080  # the same port number used in server code
# #generate keys
# (e, n),(d,n) = RSA.generate_keys()
# print(f"e: {e}, n: {n}, d: {d}, n: {n}")
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     #receive public key from server
#     data = s.recv(1024)
#     #send public key to server
#     s.sendall(f"{e} {n}".encode('utf-8'))
#     while True:
#         message = input('Client: ')
#         if message == "":
#             continue
#         #encrypt message with public key from server
#         #fix this
#         message = RSA.RSA_encrypt(message, int(data.decode('utf-8').split()[0]), int(data.decode('utf-8').split()[1]))
#         message_str = ' '.join(map(str, message))
#         s.sendall(message_str.encode('utf-8'))
#         # s.sendall(message.encode('utf-8'))
#         data = s.recv(1024)
#         if not data:
#             break
#         #decrypt message with private key
#         message = RSA.RSA_decrypt(data.decode('utf-8'), e, n)
#         message = data.decode('utf-8')
#         if message == "":
#             continue
#         print(f"Server: {message}")



# # # echo-client.py

# import socket

# # HOST = "127.0.0.1"  # The server's hostname or IP address
# # PORT = 65432  # The port used by the server

# # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# #     s.connect((HOST, PORT))
# #     s.sendall(b"Hello, world")
# #     data = s.recv(1024)

# # print(f"Received {data!r}")

# host = socket.gethostname()  # as both code is running on same pc
# port = 5000  # socket server port number

# client_socket = socket.socket()  # instantiate
# client_socket.connect((host, port))  # connect to the server

# message = input(" -> ")  # take input

# while message.lower().strip() != 'bye':
#     client_socket.send(message.encode())  # send message
#     data = client_socket.recv(1024).decode()  # receive response

#     print('Received from server: ' + data)  # show in terminal

#     message = input(" -> ")  # again take input

# client_socket.close()  # close the connection
# #python program to chat between server and client using sockets
# def server_program():
#     # get the hostname
#     host = socket.gethostname()
#     port = 5000  # initiate port no above 1024

#     server_socket = socket.socket()  # get instance
#     # look closely. The bind() function takes tuple as argument
#     server_socket.bind((host, port))  # bind host address and port together

#     # configure how many client the server can listen simultaneously
#     server_socket.listen(2)
#     conn, address = server_socket.accept()  # accept new connection
#     print("Connection from: " + str(address))
#     while True:
#         # receive data stream. it won't accept data packet greater than 1024 bytes
#         data = conn.recv(1024).decode()
#         if not data:
#             # if data is not received break
#             break
#         print("from connected user: " + str(data))
#         data = input(' -> ')
#         conn.send(data.encode())  # send data to the client

#     conn.close()  # close the connection

# def client_program():
#     host = socket.gethostname()  # as both code is running on same pc
#     port = 5000  # socket server port number

#     client_socket = socket.socket()  # instantiate
#     client_socket.connect((host, port))  # connect to the server

#     message = input(" -> ")  # take input

#     while message.lower().strip() != 'bye':
#         client_socket.send(message.encode())  # send message
#         data = client_socket.recv(1024).decode()  # receive response

#         print('Received from server: ' + data)  # show in terminal

#         message = input(" -> ")  # again take input

#     client_socket.close()  # close the connection