import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from datetime import datetime
import os

# Database Karyawan PT. Maju Jaya Makmur
karyawan = {
    "Aisyah Dewani Putri": "MJM001",
    "Anastasya Gerarda Siahaan": "MJM002",
    "Astriana Safira Maharsi": "MJM003",
    "Daniswara Maria Rosalin": "MJM004",
    "Dinnar Ary Nastiti": "MJM005",
    "Fadzli Fiyannuba": "MJM006",
    "Fidini Tsabita": "MJM007",
    "Fitri Izzati": "MJM008",
    "Galuh Chandra Maulida": "MJM009",
    "Gym Fadhil Hiyatullah": "MJM010",
    "Ida Fatkhur Rohmah": "MJM011",
    "Julia Nastu Ayuningtyas": "MJM012",
    "Kautsar Ramadhan Budianto": "MJM013",
    "Kayyis Rusydi Firdaus": "MJM014",
    "Leirisa Yajna Kirana Fagan": "MJM015",
    "Lelicia Maria Emilia Gomes Soares": "MJM016",
    "Lovela Cantika Wardhana": "MJM017",
    "Luthfia Amanda Rohmah": "MJM018",
    "Mar'atus Sholekhah": "MJM019",
    "Muhammad Farhan Ahda Fadhila": "MJM020",
    "Qanita Ulya": "MJM021",
    "Rafeyfa Asyla Suryawan": "MJM022",
    "Rafi Andhika Dwi Permana": "MJM023",
    "Ratna Rahma Sabrina": "MJM024",
    "Ryan Hafidz Setiawan": "MJM025",
}

# Database HRD PT. Maju Jaya Makmur
hrd = {
    "HRD 1": "1234",
    "HRD 2": "5678",
}

# File Path
NAMA_FILE = "Absensi_Karyawan_Bulan_XX.xlsx"
if not os.path.exists(NAMA_FILE):
    pd.DataFrame(columns=['Nama', 'NIP', 'Tanggal', 'Jam', 'Keterangan']).to_excel(NAMA_FILE, index=False)

# Fungsi untuk memastikan format file absensi sesuai
def validasi_file_absensi():
    try:
        data = pd.read_excel(NAMA_FILE)
        required_columns = {'Nama', 'NIP', 'Tanggal', 'Jam', 'Keterangan'}
        if not required_columns.issubset(data.columns):
            raise ValueError("Format kolom file absensi tidak sesuai.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi masalah pada file absensi: {e}")
        return False
    return True

# Tampilan Desktop Awal
def main_menu():
    for widget in main_window.winfo_children():
        widget.destroy()

    ttk.Label(main_window, text='Selamat Datang di PT. Maju Jaya Makmur', font=('Helvetica', 23, 'bold')).pack(pady=25)
    ttk.Button(main_window, text='Lanjut', command=second_menu).pack(pady=35)

# Menu Login
def second_menu():
    for widget in main_window.winfo_children():
        widget.destroy()

    ttk.Label(main_window, text='Pilih Login', font=('Helvetica', 30, 'bold')).pack(pady=30)
    ttk.Button(main_window, text='Login sebagai Karyawan', command=login_karyawan).pack(pady=15)
    ttk.Button(main_window, text='Login sebagai HRD', command=login_hrd).pack(pady=23)
    ttk.Button(main_window, text='Kembali ke Menu Awal', command=main_menu).pack(pady=23)

# Login Karyawan
def login_karyawan():
    def submit_karyawan():
        nama = nama_combobox.get()
        password = password_entry.get()
        nip = karyawan.get(nama)

        if nip == password:
            absensi_karyawan(nama, nip)
        else:
            messagebox.showerror('Error', 'Nama atau Password Salah!')

    for widget in main_window.winfo_children():
        widget.destroy()

    ttk.Label(main_window, text='Login Karyawan', font=('Helvetica', 30, 'bold')).pack(pady=30)
    ttk.Label(main_window, text='Nama').pack()
    nama_combobox = ttk.Combobox(main_window, values=list(karyawan.keys()), state='readonly')
    nama_combobox.pack(pady=23)
    ttk.Label(main_window, text='Password').pack()
    password_entry = ttk.Entry(main_window, show='*')
    password_entry.pack(pady=23)
    ttk.Button(main_window, text='Login', command=submit_karyawan).pack(pady=25)

# Absensi Karyawan
def absensi_karyawan(nama, nip):
    if not validasi_file_absensi():
        return

    now = datetime.now()
    tanggal = now.strftime('%d-%m-%y')
    jam = now.strftime('%H:%M:%S')
    keterangan = 'Hadir' if now.hour < 10 else 'Alfa'

    try:
        data = pd.read_excel(NAMA_FILE)
        if not data[(data['Nama'] == nama) & (data['Tanggal'] == tanggal)].empty:
            messagebox.showerror('Error', 'Anda sudah absen hari ini!')
            return

        new_entry = pd.DataFrame([[nama, nip, tanggal, jam, keterangan]],
                                 columns=['Nama', 'NIP', 'Tanggal', 'Jam', 'Keterangan'])
        data = pd.concat([data, new_entry], ignore_index=True)
        data.to_excel(NAMA_FILE, index=False)

        messagebox.showinfo('Sukses', f'Absensi berhasil dicatat! Status: {keterangan}')
        main_menu()
    except Exception as e:
        messagebox.showerror('Error', f'Terjadi kesalahan: {e}')

# Dashboard HRD
def hrd_dashboard():
    def lihat_rekap():
        try:
            bulan = int(month_entry.get())
            data = pd.read_excel(NAMA_FILE)
            data['Tanggal'] = pd.to_datetime(data['Tanggal'], format='%d-%m-%y')
            filtered_data = data[data['Tanggal'].dt.month == bulan]

            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                     filetypes=[("Excel files", "*.xlsx")])
            if file_path:
                filtered_data.to_excel(file_path, index=False)
                messagebox.showinfo('Sukses', 'Rekap absensi berhasil disimpan!')
        except Exception as e:
            messagebox.showerror('Error', f'Terjadi kesalahan: {e}')

    def hitung_gaji():
        try:
            bulan = int(month_entry.get())
            data = pd.read_excel(NAMA_FILE)
            data['Tanggal'] = pd.to_datetime(data['Tanggal'], format='%d-%m-%y')
            filtered_data = data[data['Tanggal'].dt.month == bulan]

            if filtered_data.empty:
                messagebox.showerror('Error', 'Tidak ada data untuk bulan tersebut!')
                return

            gaji_karyawan = filtered_data.groupby('Nama')['Keterangan'].apply(
                lambda x: (x == 'Hadir').sum() * 120000)

            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                     filetypes=[("Excel files", "*.xlsx")])
            if file_path:
                gaji_karyawan.to_frame('Gaji').to_excel(file_path)
                messagebox.showinfo('Sukses', 'Gaji berhasil dihitung dan disimpan!')
        except Exception as e:
            messagebox.showerror('Error', f'Terjadi kesalahan: {e}')

    for widget in main_window.winfo_children():
        widget.destroy()

    ttk.Label(main_window, text='Dashboard HRD', font=('Helvetica', 25, 'bold')).pack(pady=30)
    ttk.Label(main_window, text='Masukkan Bulan (1-12)').pack()
    month_entry = ttk.Entry(main_window)
    month_entry.pack(pady=15)
    ttk.Button(main_window, text='Lihat Rekap Absensi', command=lihat_rekap).pack(pady=23)
    ttk.Button(main_window, text='Hitung Gaji', command=hitung_gaji).pack(pady=23)
    ttk.Button(main_window, text='Kembali ke Menu Awal', command=main_menu).pack(pady=25)

# Login HRD
def login_hrd():
    def submit_hrd():
        username = username_entry.get()
        password = password_entry.get()

        if hrd.get(username) == password:
            hrd_dashboard()
        else:
            messagebox.showerror('Error', 'Nama atau Password salah!')

    for widget in main_window.winfo_children():
        widget.destroy()

    ttk.Label(main_window, text='Login HRD', font=('Helvetica', 25, 'bold')).pack(pady=30)
    ttk.Label(main_window, text='Username').pack()
    username_entry = ttk.Entry(main_window)
    username_entry.pack(pady=23)
    ttk.Label(main_window, text='Password').pack()
    password_entry = ttk.Entry(main_window, show='*')
    password_entry.pack(pady=23)
    ttk.Button(main_window, text='Login', command=submit_hrd).pack(pady=30)

# Main Window
main_window = tk.Tk()
main_window.title('PT. Maju Jaya Makmur')
main_window.geometry('800x500')

if os.path.exists('background.png'):
    bg_image = tk.PhotoImage(file='background.png')
    bg_label = tk.Label(main_window, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

main_menu()
main_window.mainloop()