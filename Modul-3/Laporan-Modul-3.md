## Laporan Prakktikum Jaringan Komputer Modul 3 Terkait HTTP
- Nama          : I Made Sudiarte
- NIM           : 103072400044
- Kelas         : IF-04-05

# Tujuan Praktikum
- Mahasiswa dapat menginvestigasi cara kerja protokol HTTP menggunakan Wireshark.

# Percobaan

# Melakukan Capturing Wifi 2 Pada Wireshark

Tampilan Awal

![WIFI2](image.png)

1 Langkah awal yang kita lakukan adalah filter tampilan capturing dengan mengetik "http" pada kolom filter lalu enter

tampilanya akan seperti gambar di bawah 

![filter](image-1.png)

2 Selanjutnya Kita membuka tautan berikut : http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html pada browser dan pastikan linknya http bukan https, jika sudah maka tampilanya akan seperti gambar di bawah 

![http1](image-2.png)

3. Masuk ke Wiresharknya, cek lalu lintas capturing yang sudah difilter tadi, maka akan terdapat 2 lalu linta jaringan dengan protokol http, karena kita sudah membuka link di atas.

![alt text](image-5.png)

- penjelasan : Terdapat Packet keluar dari laptop (IP lokal 192.168.18.182) menuju server (IP 128.119.245.12) dengan protokol HTTP. Contohnya: GET request untuk file /wireshark-labs/HTTP-wireshark-file1.html. Packet masuk, ini balasan dari server ke laptop. Contohnya: HTTP/1.1 304 Not Modified yang berarti file sudah ada di cache, jadi server tidak mengirim ulang isi file. di bagian bawah pada gambar kita dapat melihat pesaan yang terdapat pada website yang kita buka

4. Selanjutnya buka link berikut : http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html, pastikan http bukan https

website akan menampilkan seperti berikut 

![http3](image-4.png)

5. selanjutnya balik lagi ke wireshark

![alt text](image-6.png)

* terdapat 2 paket baru, paket yang keluar dan respon dari website/paket yang masuk.

