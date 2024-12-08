import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import pandas as pd
import os
from PIL import Image, ImageTk

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

# Database HRD PT. Kadira
hrd = {
    "Dinnar": "1234",
    "Kayyis": "5678",
    "Rara": "0000"
}

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

    bg_image = Image.open("rekapgaji1.png")
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

# def start_app():
#     main_window = tk.Tk()
#     main_window.title("Absensi Karyawan PT. Maju Jaya Makmur")
#     main_window.geometry("1920x1080")
#     main_window.resizable(True, True)

#     style = ttk.Style()
#     style.configure(
#         "Custom.TButton",
#         font=("Helvetica", 12, "bold"),
#         foreground="black",
#         background="#9fd5ec",
#         padding=10,
#         borderwidth=1,
#     )
#     style.map(
#         "Custom.TButton",
#         background=[("active", "#9fd5ec")],
#         foreground=[("active", "black")],
#     )

#     main_menu(main_window)
#     main_window.mainloop()

# Menampilkan menu utama
main_menu()
main_window.mainloop()