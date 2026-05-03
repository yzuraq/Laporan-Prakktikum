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
    try:
        #menyetujui koneksi dari client
        conectionSocket, add = serverSocket.accept()
        print(f"[SYSTEM] Client terhubung dari {add}")

        while True:
            try:
                #pesan yang diterima = 10101010
                massage = conectionSocket.recv(2048)

                if not massage :
                    print("Client disconnect")
                    break
                massage = massage.decode()
                #cek apakah pesan = exit
                if massage.lower() == "exit":
                    print("[SYSTEM] Client ingin keluar")
                    running = False
                #memodif menjadi caplock
                modifierMassage = massage.upper()
                print("[SERVER] diterima : ", modifierMassage)

                #kirim ke client
                conectionSocket.send(
                    modifierMassage.encode()
                )
            except ConnectionAbortedError:
                print("[ERROR] Koneksi dihentikan oleh client")
                break
            except Exception as e:
                print(f"[ERROR] {e}")
                break

        conectionSocket.close()
    except Exception as e:
        print(f"[ERROR] Gagal menerima koneksi: {e}")
        continue

serverSocket.close()