Otomasi Jaringan - Disable Interface yang Berstatus DOWN
Skrip Python ini berfungsi untuk mengotomatisasi pengecekan dan penonaktifan (disable) interface jaringan yang berstatus DOWN, kecuali interface yang sedang digunakan untuk koneksi internet.
Tujuan utamanya adalah menjaga kebersihan konfigurasi jaringan dan mencegah gangguan dari interface tidak aktif yang tidak diperlukan.

 Fitur Utama:
- Deteksi interface aktif yang digunakan untuk koneksi internet secara otomatis (dengan ip route get 8.8.8.8).
- Daftar semua interface jaringan menggunakan perintah ip -o link show.
- Identifikasi interface yang berstatus DOWN.
- Menonaktifkan (disable) interface DOWN menggunakan perintah sudo ip link set <interface> down.
- Mengecualikan interface yang sedang aktif agar koneksi internet tidak terganggu.
  
 Cara Kerja Program
Program menjalankan perintah untuk mengetahui interface yang digunakan ke 8.8.8.8 (Google DNS).
Semua interface yang terdeteksi dari sistem akan dimasukkan ke dalam daftar.
Interface dengan status DOWN akan diidentifikasi.
Setiap interface yang DOWN dan bukan interface aktif akan di-disable menggunakan sudo ip link set <iface> down.

 Persyaratan
Pastikan kamu menjalankan skrip ini di sistem berbasis Linux (Ubuntu, Debian, dsb.) dan memiliki hak akses sudo.

 Dependensi:
Python 3.8.2
Utilitas jaringan iproute2 (biasanya sudah terinstal secara default)

 Cara Menjalankan
Jalankan skrip menggunakan Python:
python3 disable_down_interfaces.py

 Contoh Output
devasc@labvm:~$ sudo python3 disable_unused_interfaces.py
Interface aktif (digunakan internet): enp0s3
Melewati interface enp0s3 (digunakan untuk internet).
devasc@labvm:~$ ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:e9:3d:e6 brd ff:ff:ff:ff:ff:ff
3: dummy0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/ether c6:c9:87:bb:c0:be brd ff:ff:ff:ff:ff:ff

