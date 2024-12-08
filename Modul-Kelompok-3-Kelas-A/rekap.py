import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from datetime import datetime
import pandas as pd
import os
from main_menu import main_menu, main_window

# Database HRD PT. Kadira
hrd = {
    "Dinnar": "1234",
    "Kayyis": "5678",
    "Rara": "0000"
}

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

# Fungsi untuk login HRD
def login_hrd():
    def submit_hrd():
        nama = nama_combobox.get()
        password = password_entry.get()
        if hrd.get(nama) == password:
            hrd_dashboard()
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

    bg_image = Image.open("loginhrd.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(main_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = bg_photo

    main_window.bind("<Configure>", update_background)

    # ttk.Label(main_window, text="Login HRD", font=("Helvetica", 25, "bold")).pack(pady=30)
    ttk.Label(main_window, text="Nama").place(relx=0.4, rely=0.3, anchor="center")
    nama_combobox = ttk.Combobox(main_window, values=list(hrd.keys()), state="readonly")
    nama_combobox.place(relx=0.5, rely=0.3, anchor="center")
    ttk.Label(main_window, text="Password").place(relx=0.4, rely=0.4, anchor="center")
    password_entry = ttk.Entry(main_window, show="*")
    password_entry.place(relx=0.5, rely=0.4, anchor="center")
    ttk.Button(main_window, text="Login", command=submit_hrd).place(relx=0.5, rely=0.5, anchor="center")
    ttk.Button(main_window, text="Kembali ke Menu Awal", command=main_menu).place(relx=0.5, rely=0.6, anchor="center")

# Dashboard HRD
def hrd_dashboard():    
    for widget in main_window.winfo_children():
        widget.destroy()

# Menambahkan latar belakang yang adjustable
    def update_background(event):
        bg_image_resized = bg_image.resize((main_window.winfo_width(), main_window.winfo_height()))
        bg_photo = ImageTk.PhotoImage(bg_image_resized)
        bg_label.config(image=bg_photo)
        bg_label.image = bg_photo

    bg_image = Image.open("hrddashboard.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(main_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = bg_photo

    main_window.bind("<Configure>", update_background)
    
    # ttk.Label(main_window, text="Dashboard HRD", font=("Helvetica", 25, "bold")).pack(pady=30)
    ttk.Button(main_window, text="Lihat Rekap Absensi", command=tampilkan_rekap_absensi).place(relx=0.5, rely=0.4, anchor="center")
    ttk.Button(main_window, text="Lihat Rekap Gaji", command=tampilkan_rekap_gaji).place(relx=0.5, rely=0.5, anchor="center")
    ttk.Button(main_window, text="Kembali ke Menu Awal", command=main_menu).place(relx=0.5, rely=0.6, anchor="center")

# Fungsi untuk menampilkan rekap absensi
def tampilkan_rekap_absensi():
    for widget in main_window.winfo_children():
        widget.destroy()
        
        # Menambahkan latar belakang yang adjustable
    def update_background(event):
        bg_image_resized = bg_image.resize((main_window.winfo_width(), main_window.winfo_height()))
        bg_photo = ImageTk.PhotoImage(bg_image_resized)
        bg_label.config(image=bg_photo)
        bg_label.image = bg_photo

    bg_image = Image.open("rekapabsensi.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(main_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = bg_photo

    main_window.bind("<Configure>", update_background)

    try:
        data = pd.read_excel(NAMA_FILE)
        if data.empty:
            messagebox.showinfo("Info", "Data absensi kosong!")
            return

        ttk.Label(main_window, font=("Helvetica", 80, "bold")).place(relx=0, rely=0, anchor="center")

        table_frame = ttk.Frame(main_window)
        table_frame.pack(fill=tk.BOTH, expand=True)

        tree = ttk.Treeview(table_frame, columns=("Nama", "NIP", "Tanggal", "Jam", "Keterangan"), show="headings")
        tree.heading("Nama", text="Nama")
        tree.heading("NIP", text="NIP")
        tree.heading("Tanggal", text="Tanggal")
        tree.heading("Jam", text="Jam")
        tree.heading("Keterangan", text="Keterangan")
        tree.pack(fill=tk.BOTH, expand=True)

        for index, row in data.iterrows():
            tree.insert("", tk.END, values=row.tolist())
            
        ttk.Button(main_window, text="Kembali", command=hrd_dashboard).place(relx=0.5, rely=0.9, anchor="center")

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Fungsi untuk menampilkan rekap gaji
def tampilkan_rekap_gaji():
    for widget in main_window.winfo_children():
        widget.destroy()
        
    # Menambahkan latar belakang yang adjustable
    def update_background(event):
        bg_image_resized = bg_image.resize((main_window.winfo_width(), main_window.winfo_height()))
        bg_photo = ImageTk.PhotoImage(bg_image_resized)
        bg_label.config(image=bg_photo)
        bg_label.image = bg_photo

    bg_image = Image.open("rekapgaji.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(main_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = bg_photo

    main_window.bind("<Configure>", update_background)

    try:
        data = pd.read_excel(NAMA_FILE)
        if data.empty:
            messagebox.showinfo("Info", "Data absensi kosong!")
            return

        data["Tanggal"] = pd.to_datetime(data["Tanggal"], format="%d-%m-%Y", errors="coerce")
        gaji_karyawan = data.groupby("Nama")["Keterangan"].apply(lambda x: (x == "Hadir").sum() * 120000)

        ttk.Label(main_window, font=("Helvetica", 80, "bold")).place(relx=0, rely=0, anchor="center")
        

        table_frame = ttk.Frame(main_window)
        table_frame.pack(fill=tk.BOTH, expand=True)

        tree = ttk.Treeview(table_frame, columns=("Nama", "Gaji"), show="headings")
        tree.heading("Nama", text="Nama")
        tree.heading("Gaji", text="Gaji")
        tree.pack(fill=tk.BOTH, expand=True)
        
        ttk.Button(main_window, text="Kembali", command=hrd_dashboard).place(relx=0.5, rely=0.9, anchor="center")
        

        for nama, gaji in gaji_karyawan.items():
            tree.insert("", tk.END, values=(nama, f"Rp {gaji:,}"))


    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")