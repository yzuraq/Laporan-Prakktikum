from socket import *
import threading

def handle_client(connectionSocket):
    try:
        #input user
        #decode = 10101010 -> "pesan"
        massage = connectionSocket.recv(1024).decode()

        #nampung req tipe file dari pengguna
        #massage = GET /index.html HTTP/1.1 
        fileName = massage.split()[1]
        print(fileName)

        #membuka index.html serta menghilangkan /
        f = open("Modul9/" + fileName[1:])

        #membaca file html 
        outputData = f.read()

        #kirim respon
        connectionSocket.send(
            "HTTP/1.1 200 OK\r\n\r\n".encode()
        )

        #kirim data
        connectionSocket.sendall(outputData.encode())

    except IOError:
        connectionSocket.send(
            "HTTP/1.1 404 NOT FOUND\r\n\r\n".encode()
        )

        #kirim data
        connectionSocket.send(
            "<h1>404 NOT FOUND</h1>".encode()
        )

        ##TUTUP KONEKSI
        connectionSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 6799))
serverSocket.listen(5)#DAPAT MENERIMA SEBANYAK 5 CLIENT
print("[SYSTEM] Server is Running Away....")


while True:
    connectionSocket, add = serverSocket.accept()

    #membuat thread dan target threadnya, beserta parameternya
    thread = threading.Thread(
        target=handle_client,
        args=(connectionSocket,)
    )
    thread.start()