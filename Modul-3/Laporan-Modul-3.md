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

6. salin buka lagi link http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html untuk kedua kalinya lalu refresh
7. balik lagi ke wireshark, maka akan terdapat 2 paket lagi, akan tetapi ada beberapa perbedaan dari responnya.

![http5](image-7.png)
* terlihat info dari paket yang masuk tertulis - HTTP/1.1 304 Not Modified yang seharusnya - HTTP/1.1 200 OK (text/html), ini terjadi karena sebelumnya kita sudah pernah mengakses website tersebut sehingga data cache tersimpan pada browser kita sehingga server tidak perlu mengirim ulang isi filenya.

8. Lanjut buka link berikut : http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html, pastikan http, buka https
Tampilannya akan seperti berikut :

![http6](image-8.png)

9. Balik lagi kewireshark buat cek
![http7](image-9.png)

- penjelasan : Dalam kasus HTTP GET, entitas dalam
respons adalah seluruh file HTML yang diminta. Dalam kasus ini, file HTML agak panjang, dan dengan
ukuran 4500 byte terlalu besar untuk di muat dalam satu paket TCP. Di Wireshark versi terbaru,
Wireshark menunjukkan setiap segmen TCP sebagai paket terpisah, dan fakta bahwa respons HTTP
tunggal terfragmentasi (terbagi) menjadi beberapa paket TCP ditunjukkan oleh “TCP segment of a
reassembled PDU” (segmen TCP dari PDU yang dipasang kembali), di kolom Info pada Wireshark . (modul JARKOM IF Genap 2526 halamn 22)

10. Lanjut buka link berikut : http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html pastikan http, bukan https

![http8](image-10.png)
*di dalam link tersebut terdapat beberapa teks dan beberapa gambar

11. Kembali Kewireshark lagi, untuk cek

![http9](image-11.png)
*terdapat 2 paket baru, paket yang keluar dan respon dari website/paket yang masuk. namun bedanya di sini terdapat keterangan gambar dan bukan teks lagi  pada HTTP/1.1 200 OK (JPEG JFIF image), ini terjadi karena terdapat gambar pada website tersebut.

- penjelasan : Setelah membuka link tersebut browser seharusnya menampilkan file HTML pendek dengan dua gambar. Kedua gambar ini
direferensikan dalam file HTML dasar. Artinya, gambar itu sendiri tidak terdapat dalam HTML;
alih-alih hanya terdapat URL kedua gambar pada file HTML tersebut. Browser Anda harus
mengambil logo ini dari URL situs web yang disematkan pada file HTML. Logo penerbit kita
diambil dari situs web gaia.cs.umass.edu. (modul JARKOM IF Genap 2526 halaman 22).

12. Lanjut buka link berikut : http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html pastikan http, bukan https

![http10](image-12.png)
*setelah berhasil membuka link tersebut, kita akan dimintai username dan password. Ketik username dan password yang diminta
ke dalam kotak pop up (Username adalah "wireshark-students" (tanpa tanda kutip), dan password adalah "network" (tanpa tanda kutip)). jika salah memasukan username atau password, maka kita akan terus dimintai username dan password. jika berhasil maka akan menampilkan beberapa pesan berikut.

![sukses](image-14.png)

13. Terakhir buka wireshark lagi untuk mengecek

![http11](image-15.png)
*Terdapat 2 paket yang masuk, yang pertama HTTP/1.1 401 Unauthorized (text/html) ini berarti website yang kita akses memiliki proteksi yang dimana harus memasukan username dan password untuk mengakses/membukanya. yang kedua itu HTTP/1.1 200 OK (text/html) yang berarti kita berhasil mengakses webtersebut.

# Cukup Sekian Laporan Praktikum Dari Saya, Kurang dan Lebihnya Saya Mohon Maaf. Saya Ucapkan Terima Kasih

## Lampiran
![1](image-16.png)







