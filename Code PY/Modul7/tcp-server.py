from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

#MENG BIND SERVER
serverSocket.bind(
    ('', serverPort)
)

#server siap menerima koneksi
serverSocket.listen(1)
print("[SYSTEM] Server TCP siap digunakan!")

running = True

while running:
    #menyetujui koneksi dari client
    conectionSocket, add = serverSocket.accept()

    while True:
        #pesan yang diterima = 10101010
        massage = conectionSocket.recv(2048).decode()

        if not massage :
            break
        
        #cek apakah pesan = exit
        if massage.lower == "exit":
            print("[SYSTEM] Client ingin keluar")
            running = False
        #memodif menjadi caplock
        modifierMassage = massage.upper()
        print("[SERVER] diterima : ", modifierMassage)

        #kirim ke client
        conectionSocket.send(
            modifierMassage.encode()
        )

    conectionSocket.close()

serverSocket.close()