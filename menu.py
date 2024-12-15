import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import pandas as pd
import os
from PIL import Image, ImageTk

# Database HRD PT. Kadira
hrd = {
    "Dinnar": "1234",
    "Kayyis": "5678",
    "Rara": "0000"
}

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


    ttk.Button(main_window, text="Simpan", command=simpan_karyawan).pack(pady=10)
    ttk.Button(main_window, text="Kembali", command=hrd_dashboard).pack(pady=5)


# Fungsi untuk memperbarui latar belakang
def update_background(event):
    bg_image = Image.open("selamatdatangrev.png")
    bg_image = bg_image.resize((main_window.winfo_width(), main_window.winfo_height()))
    bg_image = ImageTk.PhotoImage(bg_image)

    update_background(image=bg_image)
    update_background = bg_image  


# Fungsi untuk menu awal
def main_menu():
    for widget in main_window.winfo_children():
        widget.destroy()

    # Menambahkan latar belakang yang adjustable
    def update_background(event):
        bg_image_resized = bg_image.resize((main_window.winfo_width(), main_window.winfo_height()))
        bg_photo = ImageTk.PhotoImage(bg_image_resized)
        bg_label.config(image=bg_photo)
        bg_label.image = bg_photo

    bg_image = Image.open("selamatdatangrev.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(main_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = bg_photo

    main_window.bind("<Configure>", update_background)

    # Tombol-tombol dengan posisi relx, rely, dan warna
    ttk.Button(
        main_window, text="Login Karyawan", command=login_karyawan,
        style="Custom.TButton"
    ).place(relx=0.5, rely=0.4, anchor="center")
    ttk.Button(
        main_window, text="Login HRD", command=login_hrd,
        style="Custom.TButton"
    ).place(relx=0.5, rely=0.5, anchor="center")
    ttk.Button(
        main_window, text="Keluar", command=main_window.destroy,
        style="Custom.TButton"
    ).place(relx=0.5, rely=0.6, anchor="center")

    
# Fungsi untuk memperbarui latar belakang
def update_background(event):
    bg_image = Image.open("loginkaryawan.png")
    bg_image = bg_image.resize((main_window.winfo_width(), login_karyawan.winfo_height()))
    bg_image = ImageTk.PhotoImage(bg_image)

    update_background.config (image=bg_image)
    update_background = bg_image

# Inisialisasi window utama
main_window = tk.Tk()
main_window.title("Absensi Karyawan PT. Kadira")
main_window.geometry("1920x1080")
main_window.resizable(True, True)

# Bind untuk memperbarui latar belakang saat ukuran berubah
main_window.bind("<Configure>", update_background)

style = ttk.Style()
style.configure(
    "Custom.TButton",
    font=("Helvetica", 12, "bold"),
    foreground="black",
    background="#9fd5ec",
    padding=10,
    borderwidth=1,
)
style.map(
    "Custom.TButton",
    background=[("active", "#9fd5ec")],
    foreground=[("active", "black")],
)

# Menampilkan menu utama
main_menu()
main_window.mainloop()