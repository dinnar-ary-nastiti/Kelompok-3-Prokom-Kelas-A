import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from datetime import datetime
import os

# Database karyawan
employees = {
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

# Database HRD
hrd_users = {"HRD1": "12345", "HRD2": "12345"}

# File paths
FILE_NAME = "absensi_karyawan.xlsx"
if not os.path.exists(FILE_NAME):
    pd.DataFrame(columns=["Nama", "NIP", "Tanggal", "Jam", "Keterangan"]).to_excel(FILE_NAME, index=False)

# Tampilan awal
def main_menu():
    for widget in main_window.winfo_children():
        widget.destroy()

    ttk.Label(main_window, text="Selamat Datang di PT. Maju Jaya Makmur", font=("Helvetica", 18, "bold")).pack(pady=20)
    ttk.Button(main_window, text="Lanjut", command=second_menu).pack(pady=30)

# Menu kedua
def second_menu():
    for widget in main_window.winfo_children():
        widget.destroy()

    ttk.Label(main_window, text="Pilih Login", font=("Helvetica", 25, "bold")).pack(pady=25)
    ttk.Button(main_window, text="Login sebagai Karyawan", command=login_karyawan).pack(pady=10)
    ttk.Button(main_window, text="Login sebagai HRD", command=login_hrd).pack(pady=18)
    ttk.Button(main_window, text="Kembali ke Menu Awal", command=main_menu).pack(pady=18)

# Login karyawan
def login_karyawan():
    def submit_karyawan():
        nama = nama_combobox.get()
        password = password_entry.get()
        nip = employees.get(nama)

        if nip == password:
            absensi_karyawan(nama, nip)
        else:
            messagebox.showerror("Error", "Nama atau Password salah!")
    
    for widget in main_window.winfo_children():
        widget.destroy()

    ttk.Label(main_window, text="Login Karyawan", font=("Helvetica", 25, "bold")).pack(pady=25)
    ttk.Label(main_window, text="Nama").pack()
    nama_combobox = ttk.Combobox(main_window, values=list(employees.keys()), state="readonly")
    nama_combobox.pack(pady=18)
    ttk.Label(main_window, text="Password").pack()
    password_entry = ttk.Entry(main_window, show="*")
    password_entry.pack(pady=18)
    ttk.Button(main_window, text="Login", command=submit_karyawan).pack(pady=20)

# Absensi karyawan
def absensi_karyawan(nama, nip):
    now = datetime.now()
    tanggal = now.strftime("%d-%m-%Y")  # Format tanggal menjadi string
    jam = now.strftime("%H:%M:%S")
    keterangan = "Hadir" if now.hour < 20 else "Alfa"

    # Baca data Excel
    try:
        data = pd.read_excel(FILE_NAME)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat membaca data: {e}")
        return

    # Cek apakah karyawan sudah absen pada tanggal yang sama
    if not data[(data['Nama'] == nama) & (data['Tanggal'] == tanggal)].empty:
        messagebox.showerror("Error", "Anda sudah absen hari ini!")
        return

    # Tambahkan data baru ke dataframe
    new_entry = pd.DataFrame([[nama, nip, tanggal, jam, keterangan]], columns=["Nama", "NIP", "Tanggal", "Jam", "Keterangan"])
    data = pd.concat([data, new_entry], ignore_index=True)

    # Pastikan kolom "Tanggal" berupa string
    data["Tanggal"] = data["Tanggal"].astype(str)  # Format sebagai string untuk menghindari error

    # Simpan kembali ke Excel
    try:
        data.to_excel(FILE_NAME, index=False)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat menyimpan data: {e}")
        return

    # Tampilkan pesan berhasil
    messagebox.showinfo("Sukses", f"Absensi berhasil dicatat! Status: {keterangan}")
    main_menu()

# Dashboard HRD
def hrd_dashboard():
    def lihat_rekap():
        bulan = int(month_entry.get())
        data = pd.read_excel(FILE_NAME)
        data["Tanggal"] = pd.to_datetime(data["Tanggal"], format="%d-%m-%Y")
        filtered_data = data[data["Tanggal"].dt.month == bulan]

        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            filtered_data.to_excel(file_path, index=False)
            messagebox.showinfo("Sukses", "Rekap absensi berhasil disimpan!")

    def hitung_gaji():
        bulan = int(month_entry.get())
        data = pd.read_excel(FILE_NAME)
        data["Tanggal"] = pd.to_datetime(data["Tanggal"], format="%d-%m-%Y")
        filtered_data = data[data["Tanggal"].dt.month == bulan]

        gaji_karyawan = filtered_data.groupby("Nama")["Keterangan"].apply(
            lambda x: (x == "Hadir").sum() * 100000
        )

        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            gaji_karyawan.to_frame("Gaji").to_excel(file_path)
            messagebox.showinfo("Sukses", "Gaji berhasil dihitung dan disimpan!")

    for widget in main_window.winfo_children():
        widget.destroy()

    ttk.Label(main_window, text="Dashboard HRD", font=("Helvetica", 25, "bold")).pack(pady=25)
    ttk.Label(main_window, text="Masukkan Bulan (1-12)").pack()
    month_entry = ttk.Entry(main_window)
    month_entry.pack(pady=10)
    ttk.Button(main_window, text="Lihat Rekap Absensi", command=lihat_rekap).pack(pady=18)
    ttk.Button(main_window, text="Hitung Gaji", command=hitung_gaji).pack(pady=18)
    ttk.Button(main_window, text="Kembali ke Menu Awal", command=main_menu).pack(pady=20)

# Login HRD
def login_hrd():
    def submit_hrd():
        username = username_entry.get()
        password = password_entry.get()

        if hrd_users.get(username) == password:
            hrd_dashboard()  # Make sure hrd_dashboard() is defined above this function
        else:
            messagebox.showerror("Error", "Nama atau Password salah!")

    for widget in main_window.winfo_children():
        widget.destroy()

    ttk.Label(main_window, text="Login HRD", font=("Helvetica", 25, "bold")).pack(pady=25)
    ttk.Label(main_window, text="Username").pack()
    username_entry = ttk.Entry(main_window)
    username_entry.pack(pady=18)
    ttk.Label(main_window, text="Password").pack()
    password_entry = ttk.Entry(main_window, show="*")
    password_entry.pack(pady=18)
    ttk.Button(main_window, text="Login", command=submit_hrd).pack(pady=25)

# Main window
main_window = tk.Tk()
main_window.title("PT. Maju Jaya Makmur")
main_window.geometry("800x600")
bg_image = tk.PhotoImage(file="background.png")  # Ganti dengan gambar background Anda
bg_label = tk.Label(main_window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

main_menu()
main_window.mainloop()