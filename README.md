# Kelas A, Kelompok 3, Daftar Anggota Team:
1. I0324005, Dinnar Ary Nastiti, dinnar-ary-nastiti
2. I0324014, Kayyis Rusydi Firdaus, Kayyis484
3. I0324033, Amaradhika Putri Agustina, AmaradhikaPutriAgustina
   
## Penghitungan Gaji Karyawan Sesuai Jam kerja dalam kurun Waktu Satu Bulan   
Dalam era digital saat ini, efisiensi dan akurasi menjadihal penting dalam pengelolaan sumber daya manusia, terutama dalam sistem penggajian suatu perusahaan. Program ini dirancang untuk menghitung gaji karyawan secara otomatis berdasarkan data kehadiran. Karyawan diwajibkan melakukan absensi setiap hari kerja, dan data absensi tersebut akan tersimpan dalam database yang mencakup nama karyawan serta status kehadirannya. Sistem ini secara otomatis menghitung gaji berdasarkan data kehadiran karyawan, dengan penyesuaian gaji hanya dihitung berdasarkan jumlah hari hadir, sehingga karyawan yang tidak hadir, baik karena sakit, izin, maupun alfa tidak akan menerima bayaran untuk hari tersebut. Dengan sistem ini, HRD dapat dengan mudah memantau absensi dan mengelola penggajian dengan lebih efisien, sekaligus mendorong keteraturan kehadiran yang lebih baik di suatu perusahaan.

# Fitur 
1. Login berdasarkan peran (Karyawan / HRD)
2. Validasi Data (Nama & Password)
3. Absensi Karyawan (Hadir / Alfa)
4. Perhitungan gaji
5. Pengelolaan dan ekspor data dalam bentuk Excel
6. Hasil Rekapan Absensi dalam format tabel
7. Hasil Rekapan Gaji dalam format tabel
8. Menambah karyawan dan password berupa NIP

# Library
1. tkinter
2. pandas
3. os
4. datetime
5. pillow
6. Openpyxl

# Sitemap
![Diagram Tanpa Judul-Halaman-3 drawio (1)](https://github.com/user-attachments/assets/0520fcfc-d00a-4292-8af8-346c8cfcac6f)


# Diagram Alir
![Diagram Tanpa Judul-Halaman-2 drawio (2)](https://github.com/user-attachments/assets/df9b6d5d-c958-4431-9caf-f52eda813b5d)
.





Program dimulai dengan menu awal yang di mana pengguna diminta untuk memilih peran sebagai Karyawan, HRD, atau keluar. Jika pengguna memilih Karyawan, mereka diminta memasukkan Nama dan Password. Jika Nama atau Password yang dimasukkan tidak valid, sistem memberikan pesan "Nama atau Password salah!", dan Karyawan diarahkan kembali untuk mencoba lagi. Jika valid, sistem mengecek waktu absensi. Jika absensi dilakukan sebelum atau pada jam 10.00 WIB, status absensi ditandai sebagai Hadir; jika lebih dari jam yang telah di tentukan, status ditandai sebagai Alfa.

Jika pengguna memilih peran HRD, mereka diminta memasukkan  Nama dan Password. Jika password salah, muncul pesan "Nama atau Password salah!" dan HRD diarahkan untuk mencoba kembali. Jika Nama dan password benar, HRD akan diberikan akses ke menu yang berisi opsi Lihat Data Gaji, Lihat Absensi, Tambah Karyawan dan Kembali ke Menu Utama.
Selanjutnya, data absensi yang telah dilakukan karyawan akan diolah dan data tersebut dapat diekspor dalam format Excel. Jika HRD memilih untuk melihat data gaji, sistem menghitung gaji berdasarkan formula : 
Jumlah Gaji = Jumlah hadir x 8 × Rp15.000 (per 1 jam)
dan hasilnya dapat dilihat oleh HRD di halaman yang sama.
Kemudian jika HRD memilih menu Tambah Karyawan maka HRD bisa menambah nama karyawan baru dan password berupa NIP

Setelah proses ini selesai, sistem akan mengembalikan pengguna ke menu utama. Setiap langkah yang selesai diakhiri dengan kembalinya sistem ke menu utama, sehingga pengguna dapat memilih tindakan lainnya atau menyelesaikan sesi.
