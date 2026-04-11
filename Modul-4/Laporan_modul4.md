# Modul 4 DNS
## Tujuan Praktikum 
1. Mahasiswa dapat menginvestigasi cara kerja DNS menggunakan Wireshark

## A. Pengantar
Sistem Nama Domain (DNS) adalah komponen protokol standar internet yang bertanggung jawab untuk mengubah nama domain yang mudah dipahami manusia menjadi alamat Internet Protocol (IP) yang digunakan komputer untuk mengidentifikasi satu sama lain di jaringan.

## B. Nslookup
nslookup memungkinkan host yang menjalankan perintah untuk
bertanya mengenai suatu server DNS dan mendapatkan informasi DNS dari server tersebut. Server
DNS yang ditanyakan dapat berupa server DNS root, server DNS domain tingkat atas, server DNS
otoritatif, atau server DNS perantara. Untuk menyelesaikan perintah ini, nslookup mengirimkan
permintaan DNS ke server DNS yang ditentukan host, menerima balasan DNS dari server DNS yang
sama, dan menampilkan hasilnya.

    ![nslookupmit.edu](image.png)
* perintah di atas digunakan untuk meminta alamat ip dari website yang dituju/www.mit.edu



## Lakukan beberapa hal berikut (dan amati hasilnya):
1. Jalankan nslookup untuk mendapatkan alamat IP dari server web di Asia. Berapa alamat IP server tersebut?

    ![soal1Nslookup](image-1.png)
* dari hasil nslookpu untuk server pendidikan di jepang, didapat alamat ip 210.152.243.234

2. Jalankan nslookup agar dapat mengetahui server DNS otoritatif untuk universitas di Eropa.

    ![soal2Nslookup](image-2.png)
*dari hasil nslookup -type=NS ox.ac.uk (University of Oxford) terlihat ada 3 namaserver utama dan 3 authoritative server tambahan yang jika dijumlahkan jadi terdapat 6 dns.

3. Jalankan nslookup untuk mencari tahu informasi mengenai server email dari Yahoo! 
    ![nslookup soal3](image-3.png)

Mail melalui salah satu server yang didapatkan di pertanyaan nomor 2. Apa alamat IP-nya?

    ![3](image-4.png)
* dari hasil di atas kita mendapatkan beberapa ip, yakni : ![ip](image-5.png)

## C. Ipconfig
Ipconfig dapat digunakan untuk menampilkan informasi mengenai TCP/IP Anda saat ini, termasuk alamat IP Anda, alamat server DNS, jenis adaptor, dan sebagainya. Sebagai contoh, Anda dapat memperoleh semua informasi tentang host Anda hanya dengan memasukkan: ipconfig \all
    ![ipconfig](image-6.png)
