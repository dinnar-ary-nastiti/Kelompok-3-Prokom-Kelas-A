import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from datetime import datetime
import pandas as pd
import os
from main_menu import main_menu, main_window


# Database karyawan
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

NAMA_FILE = "Absensi_Karyawan.xlsx"

if not os.path.exists(NAMA_FILE):
    pd.DataFrame(columns=['Nama', 'NIP', 'Tanggal', 'Jam', 'Keterangan']).to_excel(NAMA_FILE, index=False)

# Fungsi untuk validasi file absensi
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

# Fungsi untuk login karyawan
def login_karyawan():
    def submit_karyawan():
        nama = nama_combobox.get()
        password = password_entry.get()
        if karyawan.get(nama) == password:
            karyawan_absen(nama, karyawan[nama])
        else:
            messagebox.showerror("Error", "Nama atau Password salah!")

    for widget in main_window.winfo_children():
        widget.destroy()
        
    # Menambahkan latar belakang yang adjustable
    def update_background(event):
        bg_image_resized = bg_image.resize((main_window.winfo_width(), main_window.winfo_height()))
        bg_photo = ImageTk.PhotoImage(bg_image_resized)
        bg_label.config(image=bg_photo)
        bg_label.image = bg_photo

    bg_image = Image.open("loginkaryawan.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(main_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = bg_photo

    main_window.bind("<Configure>", update_background)

    # ttk.Label(main_window, text="Login Karyawan", font=("Helvetica", 25, "bold")).pack(pady=30)
    ttk.Label(main_window, text="Nama", font=("Helvetica", 18, "bold")).place(relx=0.4, rely=0.3, anchor="center")
    nama_combobox = ttk.Combobox(main_window, values=list(karyawan.keys()), state="readonly")
    nama_combobox.place(relx=0.5, rely=0.3, anchor="center")
    ttk.Label(main_window, text="Password", font=("Helvetica", 18, "bold")).place(relx=0.4, rely=0.4, anchor="center")
    password_entry = ttk.Entry(main_window, show="*")
    password_entry.place(relx=0.5, rely=0.4, anchor="center")
    ttk.Button(main_window, text="Login", command=submit_karyawan).place(relx=0.5, rely=0.5, anchor="center")
    ttk.Button(main_window, text="Kembali ke Menu Awal", command=main_menu).place(relx=0.5, rely=0.55, anchor="center")

# Fungsi untuk mencatat absensi karyawan
def karyawan_absen(nama, nip):
    for widget in main_window.winfo_children():
        widget.destroy()

    current_time = datetime.now()
    deadline = current_time.replace(hour=10, minute=0, second=0)

    keterangan = "Hadir" if current_time <= deadline else "Alfa"

    try:
        data = pd.read_excel(NAMA_FILE)
        new_row = {"Nama": nama, "NIP": nip, "Tanggal": current_time.strftime("%d-%m-%Y"), 
                   "Jam": current_time.strftime("%H:%M:%S"), "Keterangan": keterangan}
        data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
        data.to_excel(NAMA_FILE, index=False)
        messagebox.showinfo("Info", f"Absensi berhasil! Anda {keterangan}.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat menyimpan absensi: {e}")
    
    # Menambahkan latar belakang yang adjustable
    def update_background(event):
        bg_image_resized = bg_image.resize((main_window.winfo_width(), main_window.winfo_height()))
        bg_photo = ImageTk.PhotoImage(bg_image_resized)
        bg_label.config(image=bg_photo)
        bg_label.image = bg_photo

    bg_image = Image.open("terimakasih.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(main_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = bg_photo

    main_window.bind("<Configure>", update_background)
    
    ttk.Label(main_window, text=f"Terima kasih, {nama}!", font=("Helvetica", 25, "bold")).place(relx=0.5, rely=0.4, anchor="center")
    ttk.Label(main_window, text=f"Status Anda hari ini: {keterangan}", font=("Helvetica", 18)).place(relx=0.5, rely=0.5, anchor="center")
    ttk.Button(main_window, text="Kembali ke Menu Awal", command=main_menu).place(relx=0.5, rely=0.6, anchor="center")