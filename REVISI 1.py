import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os
from datetime import datetime

# Konstanta
GAJI_PER_JAM = 15000
JAM_KERJA_PER_HARI = 8
MAKS_HARI_KERJA = 22
PASSWORD_KARYAWAN = "1234"
PASSWORD_HRD = "5678"

# File absensi harian dan rekap
FILE_ABSEN = "absensi_harian.xlsx"
FILE_REKAP = "rekap_karyawan.xlsx"

# Membuat file absensi jika belum ada
def buat_file_absen():
    if not os.path.exists(FILE_ABSEN):
        df = pd.DataFrame(columns=["Tanggal", "Nama", "NIP", "Status"])
        df.to_excel(FILE_ABSEN, index=False)

buat_file_absen()

# Fungsi untuk menambahkan data ke file absensi
def tambah_data_absen(tanggal, nama, nip, status):
    df = pd.read_excel(FILE_ABSEN)
    df = pd.concat([
        df,
        pd.DataFrame({
            "Tanggal": [tanggal],
            "Nama": [nama],
            "NIP": [nip],
            "Status": [status]
        })
    ], ignore_index=True)
    df.to_excel(FILE_ABSEN, index=False)

# Fungsi untuk menghitung gaji
def hitung_gaji(data):
    hasil_gaji = []
    data_grouped = data.groupby(["Nama", "NIP"])["Status"].apply(list).reset_index()

    for _, row in data_grouped.iterrows():
        nama = row["Nama"]
        nip = row["NIP"]
        status_list = row["Status"]

        hadir = status_list.count("Sehat")
        total_gaji = hadir * JAM_KERJA_PER_HARI * GAJI_PER_JAM
        hasil_gaji.append({
            "Nama": nama,
            "NIP": nip,
            "Hadir": hadir,
            "Total Gaji": total_gaji
        })

    return pd.DataFrame(hasil_gaji)

# Fungsi untuk merekap absensi bulanan
def rekap_absensi_bulanan():
    data = pd.read_excel(FILE_ABSEN)
    if data.empty:
        messagebox.showwarning("Peringatan", "Tidak ada data absensi untuk direkap.")
        return

    rekap = data.groupby(["Nama", "NIP"]).agg({
        "Tanggal": lambda x: ", ".join(sorted(x)),
        "Status": lambda x: ", ".join(x)
    }).reset_index()

    rekap.to_excel(FILE_REKAP, index=False)
    messagebox.showinfo("Sukses", f"Rekap data karyawan telah disimpan ke '{FILE_REKAP}'.")

# Fungsi untuk login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if password == PASSWORD_KARYAWAN:
        root.destroy()
        karyawan_window(username)
    elif password == PASSWORD_HRD:
        root.destroy()
        hrd_window()
    else:
        messagebox.showerror("Login Gagal", "Nama pengguna atau kata sandi salah.")

# Jendela untuk karyawan
def karyawan_window(username):
    def submit_absensi():
        nama = username
        nip = entry_nip.get()
        status = status_var.get()
        tanggal = datetime.now().strftime("%Y-%m-%d")

        tambah_data_absen(tanggal, nama, nip, status)
        messagebox.showinfo("Sukses", "Terimakasih, absen berhasil.")
        karyawan.destroy()

    karyawan = tk.Tk()
    karyawan.title("Absensi Harian Karyawan")

    tk.Label(karyawan, text="Nama: " + username).pack(pady=5)

    tk.Label(karyawan, text="NIP:").pack()
    entry_nip = tk.Entry(karyawan)
    entry_nip.pack()

    tk.Label(karyawan, text="Status Kehadiran:").pack()
    status_var = tk.StringVar(value="Sehat")
    tk.Radiobutton(karyawan, text="Sehat", variable=status_var, value="Sehat").pack()
    tk.Radiobutton(karyawan, text="Sakit", variable=status_var, value="Sakit").pack()
    tk.Radiobutton(karyawan, text="Izin", variable=status_var, value="Izin").pack()
    tk.Radiobutton(karyawan, text="Cuti", variable=status_var, value="Cuti").pack()

    tk.Button(karyawan, text="Submit", command=submit_absensi).pack(pady=10)
    karyawan.mainloop()

# Jendela untuk HRD
def hrd_window():
    def lihat_absensi():
        if not os.path.exists(FILE_REKAP):
            rekap_absensi_bulanan()
        data = pd.read_excel(FILE_REKAP)
        messagebox.showinfo("Data Rekap Karyawan", data.to_string(index=False))

    def hitung_gaji_karyawan():
        if not os.path.exists(FILE_REKAP):
            rekap_absensi_bulanan()
        data = pd.read_excel(FILE_REKAP)
        hasil_gaji = hitung_gaji(pd.read_excel(FILE_ABSEN))
        hasil_gaji.to_excel("hasil_gaji_karyawan.xlsx", index=False)
        messagebox.showinfo("Sukses", "Gaji berhasil dihitung dan disimpan ke 'hasil_gaji_karyawan.xlsx'.")

    hrd = tk.Tk()
    hrd.title("HRD Panel")

    tk.Button(hrd, text="Rekap Absensi Bulanan", command=rekap_absensi_bulanan).pack(pady=10)
    tk.Button(hrd, text="Lihat Data Rekap", command=lihat_absensi).pack(pady=10)
    tk.Button(hrd, text="Hitung Gaji Karyawan", command=hitung_gaji_karyawan).pack(pady=10)
    hrd.mainloop()

# Jendela Login
root = tk.Tk()
root.title("Login")

# Form login
tk.Label(root, text="Nama Pengguna:").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
