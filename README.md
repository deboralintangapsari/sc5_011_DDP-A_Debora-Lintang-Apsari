# sc5_011_DDP-A_Debora-Lintang-Apsari

## Biodata Diri 
Nama : Debora Lintang Apsari | Prodi : Sistem Informasi (A) | NIM : 2609116011

## Penjelasan Program Singkat 
Program digunakan untuk menghitung biaya pemesanan kamar hotel berdasarkan jenis kamar dan lama menginap.

Sebuah hotel menerapkan tarif berdasarkan jenis kamar dan durasi menginap lalu membuat sebuah function yang mencatat pemesanan kamar dan menerima lama menginap dalam malam, kemudian menghitung total biaya pemesanan menggunakan tarif yang telah ditentukan.

## Penjelasan Kode & Output 
`1. Tampilan Pertama` <br>
<img width="484" height="101" alt="Screenshot 2026-09-22 220101" src="https://github.com/user-attachments/assets/9a9db347-a94e-4f90-a777-53284bb7b1fd" /> <br>
Kode diatas bertujuan untuk `mempercantik tampilan` dan menampilkan jenis kamar yang tersedia kepada user <br>

Tampilan : <br>
<img width="494" height="126" alt="image" src="https://github.com/user-attachments/assets/ec9e8ba6-72a6-4cd9-9a6b-d6d84897cd9b" />

`2. Penggunaan function, parameter, percabangan, return` <br>
<img width="482" height="158" alt="Screenshot 2026-09-22 220434" src="https://github.com/user-attachments/assets/ece7192f-2ea1-4fcd-8fe5-12e0ac6b5d68" /> <br>
Gambar diatas mengggunakan function yang bernama `biaya_pemesanan`. Function ini butuh 2 data (parameter) :
- jenis_kamar
- durasi_menginap
**Cek Kondisi Pertama** -> yaitu jenis_kamar.lower() == "standard, `lower` memiliki fungsi yaitu untuk menyamakan semu huruf dari user menjadi huruf kecil, jadi mau user ngetik STANDARD, Standard, STaNdArD, akan terbaca menjadi standar. Disitu juga tertulis or jenis_kamar.lower() == "1", maka selain memasukkan standar, user juga bisa menginput 1 saja.
**Cek Kondisi Kedua** -> sama seperti kondisi pertama
**Kondisi ketiga** -> apabila user salah menginput maka akan menghasilkan data yang tidak valid.
**List Harga** :
  - Standard : 200.000
  - Deluxe : 350.000
**Fungsi Return** -> untuk mengembalikan hasil perhitungannya nanti.<br>

`3. Tampilan User `<br>
<img width="445" height="117" alt="image" src="https://github.com/user-attachments/assets/048fa2f3-05da-42e5-a570-401119a04fea" /> <br>
Kode diatas akan meminta user untuk memasukkan tanggal, bulan, tahun check in & check out <br>
Tampilan : <br>
<img width="484" height="107" alt="image" src="https://github.com/user-attachments/assets/9d0421b6-94a3-4f97-854e-181aa9244111" /> <br>

`4. Rumus & Kode terakhir`<br>
<img width="452" height="184" alt="image" src="https://github.com/user-attachments/assets/c31c4487-13ec-4cd0-bfdf-292f22c21be3" /> <br>
Kode diatas adalah untuk menghitung berapa lama mereka menginap di hotel tersebut dengan rumus `checkout-checkin` 
Lalu untuk total adalah untuk memanggil kembali fungsi yang ada.<br>

Output : <br>
<img width="465" height="139" alt="image" src="https://github.com/user-attachments/assets/41764ff2-2ec0-42f5-8a8b-c544d024bb51" /> <br>

Sekian & Terimakasih 



