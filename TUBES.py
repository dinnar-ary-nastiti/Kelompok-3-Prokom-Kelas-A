import pandas as pd

# Konstanta
GAJI_PER_JAM = 15000
JAM_KERJA_PER_HARI = 8
MAKS_HARI_KERJA = 22

# Fungsi untuk menghitung gaji berdasarkan jumlah hari hadir
def hitung_gaji(hadir, gaji_perjam, jam_kerja_perhari):
    total_jam_kerja = hadir * jam_kerja_perhari
    total_gaji = total_jam_kerja * gaji_perjam
    return total_gaji

# Fungsi untuk menambahkan file data absensi karyawan
def tambah_file_data():
    file_path = input("Masukkan path file Excel (contoh: D:\\projecta\\Data Absen Karyawan.xlsx): ")
    try:
        data = pd.read_excel(file_path)
        print("Data berhasil dimuat.")
        return data
    except FileNotFoundError:
        print("Error: File tidak ditemukan.")
        return None
    except ImportError:
        print("Error: Modul 'openpyxl' belum terinstal. Silakan instal dengan 'pip install openpyxl'.")
        return None

# Fungsi untuk menghitung dan menampilkan gaji karyawan
def hitung_dan_tampilkan_gaji(data):
    if data is None or data.empty:
        print("Data karyawan tidak ditemukan. Silakan tambahkan data terlebih dahulu.")
        return
    
    hasil_gaji = []
    for index, row in data.iterrows():
        try:
            hadir = MAKS_HARI_KERJA - (row['Sakit'] + row['Izin'] + row['Cuti'])
            
            # Pengecekan hari hadir menggunakan if-else
            if hadir > MAKS_HARI_KERJA:
                hadir = MAKS_HARI_KERJA  # Batas maksimal hari kerja
                print(f"Data karyawan '{row['Nama Karyawan']}' melebihi batas hari kerja, disesuaikan menjadi {MAKS_HARI_KERJA} hari.")
            elif hadir < 0:
                hadir = 0  # Jika hadir negatif, gaji diatur ke 0
                print(f"Data karyawan '{row['Nama Karyawan']}' tidak valid, hari hadir negatif. Hadir diset ke 0 hari.")
            
            total_gaji = hitung_gaji(hadir, GAJI_PER_JAM, JAM_KERJA_PER_HARI)
            hasil_gaji.append({
                'Nama': row['Nama Karyawan'],
                'Hari Hadir': hadir,
                'Total Gaji': total_gaji
            })
        except KeyError as e:
            print(f"Kolom '{e}' tidak ditemukan dalam data.")
            return

    # Konversi hasil ke DataFrame untuk tampilan yang rapi
    gaji_df = pd.DataFrame(hasil_gaji)
    gaji_df.insert(0, 'Nomor', range(1, 1 + len(gaji_df)))
    print("\nHasil Penghitungan Gaji Karyawan:")
    print(gaji_df)

# Fungsi untuk melihat data karyawan
def lihat_data_karyawan(data):
    if data is None or data.empty:
        print("Data karyawan tidak ditemukan. Silakan tambahkan data terlebih dahulu.")
    else:
        print("\nData Karyawan:")
        print(data)

# Fungsi utama dengan menu
def main():
    data = None
    while True:
        print("\nMenu:")
        print("1. Tambah File Data Absensi")
        print("2. Lihat Data Karyawan")
        print("3. Hitung dan Tampilkan Gaji Karyawan")
        print("4. Keluar")
        
        pilihan = input("Pilih opsi (1-4): ")
        
        if pilihan == '1':
            data = tambah_file_data()
        elif pilihan == '2':
            lihat_data_karyawan(data)
        elif pilihan == '3':
            hitung_dan_tampilkan_gaji(data)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")

# Jalankan fungsi utama
if __name__ == "__main__":
    main()
