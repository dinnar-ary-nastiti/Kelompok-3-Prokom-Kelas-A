import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pandas as pd
from menu import main_menu, main_window

NAMA_FILE = "Absensi_Karyawan.xlsx"

# Database HRD PT. Kadira
hrd = {
    "Dinnar": "1234",
    "Kayyis": "5678",
    "Rara": "0000"
}

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

    bg_image = Image.open("login_hrd.py")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(main_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = bg_photo

    main_window.bind("<Configure>", update_background)

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

    bg_image = Image.open("dashboardhrd.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(main_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = bg_photo

    main_window.bind("<Configure>", update_background)
    
    # Tombol dashboard
    ttk.Button(main_window, text="Lihat Rekap Absensi", command=tampilkan_rekap_absensi).place(relx=0.5, rely=0.4, anchor="center")
    ttk.Button(main_window, text="Lihat Rekap Gaji", command=tampilkan_rekap_gaji).place(relx=0.5, rely=0.5, anchor="center")
    ttk.Button(main_window, text="Tambah Karyawan", command=tambah_karyawan).place(relx=0.5, rely=0.6, anchor="center")
    ttk.Button(main_window, text="Kembali ke Menu Awal", command=main_menu).place(relx=0.5, rely=0.7, anchor="center")

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

# Fungsi untuk menambah karyawan baru
def tambah_karyawan():
    for widget in main_window.winfo_children():
        widget.destroy()
        
    # Menambahkan latar belakang yang adjustable
    def update_background(event):
        bg_image_resized = bg_image.resize((main_window.winfo_width(), main_window.winfo_height()))
        bg_photo = ImageTk.PhotoImage(bg_image_resized)
        bg_label.config(image=bg_photo)
        bg_label.image = bg_photo

    bg_image = Image.open("tambahkaryawan.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(main_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = bg_photo

    main_window.bind("<Configure>", update_background)

    
    # Label dan Entry untuk Nama
    ttk.Label(main_window, text="Nama", font=("Helvetica", 18)).place(relx=0.4, rely=0.3, anchor="center")
    global nama_entry
    nama_entry = ttk.Entry(main_window)
    nama_entry.place(relx=0.5, rely=0.3, anchor="center")
    
    # Label dan Entry untuk NIP
    ttk.Label(main_window, text="NIP", font=("Helvetica", 18)).place(relx=0.4, rely=0.4, anchor="center")
    global nip_entry
    nip_entry = ttk.Entry(main_window)
    nip_entry.place(relx=0.5, rely=0.4, anchor="center")
    
    # Tombol Simpan
    ttk.Button(main_window, text="Simpan", command=simpan_karyawan).place(relx=0.5, rely=0.5, anchor="center")
    
    # Tombol Kembali
    ttk.Button(main_window, text="Kembali", command=hrd_dashboard).place(relx=0.5, rely=0.6, anchor="center")

def simpan_karyawan():
    nama = nama_entry.get()
    nip = nip_entry.get()

    if not nama or not nip:
        messagebox.showerror("Error", "Nama dan NIP tidak boleh kosong!")
        return

    try:
        # Definisikan baris baru yang akan ditambahkan
        new_row = pd.DataFrame([{"Nama": nama, "NIP": nip}])

        # Coba baca file Excel jika ada, jika tidak buat DataFrame baru
        try:
            data = pd.read_excel("karyawan.xlsx")
            if data.empty:  # Jika file kosong
                data = pd.DataFrame(columns=["Nama", "NIP"])
        except (FileNotFoundError, ValueError):
            data = pd.DataFrame(columns=["Nama", "NIP"])

        # Tambahkan baris baru ke dalam DataFrame
        data = pd.concat([data, new_row], ignore_index=True)

        # Simpan kembali ke file Excel
        data.to_excel("karyawan.xlsx", index=False)
        messagebox.showinfo("Sukses", "Karyawan berhasil ditambahkan!")
        hrd_dashboard()
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")