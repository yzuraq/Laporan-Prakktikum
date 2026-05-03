# Socket = penjumlahan, pembagian, pengurangan, perkalian
from socket import * 

serverName = "localhost"
serverPort = 12000

# AF_INET = ipv4 | Sock_stream = tcp
clientSocket = socket(AF_INET, SOCK_STREAM)

#hubungan

clientSocket.connect(
    (serverName, serverPort)
)

print("[SYSTEM] Masukan Pesan")

running = True

while running :
    massage = input("> ")

    clientSocket.send(massage.encode())
    
    if massage.lower() == "exit" :
        print("[SYSTEM] Keluar Dari Program")
        running = False
        break
    modifiedMassage = clientSocket.recv(2048)
    print("[SERVER] Pesan : ", modifiedMassage)
# menutup socket yang tidak dipakai
clientSocket.close()
print("[SYSTEM] socket ditutup")

