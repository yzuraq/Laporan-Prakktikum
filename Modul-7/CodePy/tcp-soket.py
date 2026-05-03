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
    try:
        massage = input("> ")
        
        # check exit sebelum send
        if massage.lower() == "exit" :
            clientSocket.send(massage.encode())
            print("[SYSTEM] Keluar Dari Program")
            running = False
            break
        
        clientSocket.send(massage.encode())
        
        modifiedMassage = clientSocket.recv(2048)
        print("[SERVER] Pesan : ", modifiedMassage.decode())
    except ConnectionResetError:
        print("[ERROR] Koneksi ditutup oleh server")
        break
    except Exception as e:
        print(f"[ERROR] {e}")
        break
        
# menutup socket yang tidak dipakai
clientSocket.close()
print("[SYSTEM] socket ditutup")

