import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from datetime import datetime
import pandas as pd
import os
from menu import main_menu, main_window

# Path file karyawan
KARYAWAN_FILE = "Karyawan.xlsx"

# Fungsi untuk membaca data karyawan dari file Excel
def load_karyawan():
    try:
        data = pd.read_excel(KARYAWAN_FILE)
        if "Nama" not in data.columns or "NIP" not in data.columns:
            raise ValueError("File Excel tidak memiliki kolom 'Nama' dan 'NIP'")
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Gagal membaca file karyawan: {e}")
        return pd.DataFrame()

# File Path untuk absensi
NAMA_FILE = "Absensi_Karyawan.xlsx"

# Inisialisasi file jika belum ada
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
        
        # Validasi nama dan password (NIP)
        if nama in karyawan_data["Nama"].values:
            nip_terdaftar = karyawan_data.loc[karyawan_data["Nama"] == nama, "NIP"].values[0]
            if password == nip_terdaftar:
                karyawan_absen(nama, password)  # Panggil fungsi absensi dengan nama dan NIP
            else:
                messagebox.showerror("Error", "Nama atau Password salah!")
        else:
            messagebox.showerror("Error", "Nama tidak ditemukan!")

    for widget in main_window.winfo_children():
        widget.destroy()
        
    # Background
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

    # Load data karyawan dari Excel
    karyawan_data = load_karyawan()
    if karyawan_data.empty:
        return

    ttk.Label(main_window, text="Nama", font=("Helvetica", 18, "bold")).place(relx=0.4, rely=0.3, anchor="center")
    nama_combobox = ttk.Combobox(main_window, values=karyawan_data["Nama"].tolist(), state="readonly", width=25)
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
    