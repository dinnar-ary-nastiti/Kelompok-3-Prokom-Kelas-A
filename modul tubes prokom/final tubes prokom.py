import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from datetime import datetime

# Define the file paths
FILE_NAME = "absensi_karyawan.xlsx"
EMPLOYEE_FILE = "karyawan.xlsx"

# Database for 25 employees and their passwords
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

# Initialize the Excel file for employee attendance if it doesn't exist
if not pd.io.common.file_exists(FILE_NAME):
    pd.DataFrame(columns=["Nama", "NIP", "Tanggal", "Keterangan"]).to_excel(FILE_NAME, index=False)

if not pd.io.common.file_exists(EMPLOYEE_FILE):
    pd.DataFrame(list(employees.items()), columns=["Nama", "Password"]).to_excel(EMPLOYEE_FILE, index=False)

# Fungsi untuk login karyawan
def login_karyawan():
    def submit_karyawan():
        nama = nama_combobox.get()
        password = password_entry.get()

        if employees.get(nama) == password:
            window_karyawan.destroy()
            absensi_window(nama)  # Panggil fungsi absensi_window setelah login sukses
        else:
            messagebox.showerror("Error", "Nama atau Password salah!")

    window_karyawan = tk.Toplevel(main_window)
    window_karyawan.title("Login Karyawan")
    window_karyawan.geometry("1280x649")  # Set window size

    # Background untuk Karyawan
    window_karyawan.configure(bg="#E6F7FF")  # Light blue background
    
    # Set elegant font
    font_style = ("Helvetica", 12, "bold")

    ttk.Label(window_karyawan, text="Nama Karyawan", background="#E6F7FF", font=font_style).grid(row=0, column=0, padx=20, pady=20, sticky="w")
    
    nama_combobox = ttk.Combobox(window_karyawan, values=list(employees.keys()), state="readonly", font=("Helvetica", 12))
    nama_combobox.grid(row=0, column=1, padx=20, pady=20)

    ttk.Label(window_karyawan, text="Password", background="#E6F7FF", font=font_style).grid(row=1, column=0, padx=20, pady=20, sticky="w")
    password_entry = ttk.Entry(window_karyawan, show="*", font=("Helvetica", 12))
    password_entry.grid(row=1, column=1, padx=20, pady=20)

    ttk.Button(window_karyawan, text="Login", command=submit_karyawan, style="TButton").grid(row=2, column=0, columnspan=2, pady=20)

# Fungsi untuk login HRD
def login_hrd():
    def submit_hrd():
        nama = nama_entry.get()
        password = password_entry.get()

        if password == "5678" and nama in ["HRD1", "HRD2"]:
            window_hrd.destroy()
            hrd_window()  # Panggil jendela HRD
        else:
            messagebox.showerror("Error", "Nama atau Password salah!")

    window_hrd = tk.Toplevel(main_window)
    window_hrd.title("Login HRD")
    window_hrd.geometry("1280x649")

    # Background untuk HRD
    window_hrd.configure(bg="#FFF5E6")  # Light orange background

    font_style = ("Helvetica", 12, "bold")

    ttk.Label(window_hrd, text="Nama", background="#FFF5E6", font=font_style).grid(row=0, column=0, padx=20, pady=20, sticky="w")
    nama_entry = ttk.Entry(window_hrd, font=("Helvetica", 12))
    nama_entry.grid(row=0, column=1, padx=20, pady=20)

    ttk.Label(window_hrd, text="Password", background="#FFF5E6", font=font_style).grid(row=1, column=0, padx=20, pady=20, sticky="w")
    password_entry = ttk.Entry(window_hrd, show="*", font=("Helvetica", 12))
    password_entry.grid(row=1, column=1, padx=20, pady=20)

    ttk.Button(window_hrd, text="Login", command=submit_hrd, style="TButton").grid(row=2, column=0, columnspan=2, pady=20)

# Fungsi untuk jendela absensi karyawan
def absensi_window(nama):
    def absensi_terbaru():
        # Cek apakah file absensi ada
        data = pd.read_excel(FILE_NAME)
        now = datetime.now().strftime("%Y-%m-%d")
        keterangan = keterangan_combobox.get()

        # Cek jika karyawan sudah absen
        if not data[(data['Nama'] == nama) & (data['Tanggal'] == now)].empty:
            messagebox.showwarning("Peringatan", "Anda sudah absen hari ini.")
            return

        # Simpan data absensi baru
        new_data = pd.DataFrame([[nama, employees[nama], now, keterangan]], columns=["Nama", "NIP", "Tanggal", "Keterangan"])
        data = pd.concat([data, new_data], ignore_index=True)
        data.to_excel(FILE_NAME, index=False)
        messagebox.showinfo("Sukses", "Absensi berhasil dicatat!")

    window_absensi = tk.Toplevel(main_window)
    window_absensi.title("Absensi Karyawan")
    window_absensi.geometry("1280x649")

    # Background untuk Absensi Karyawan
    window_absensi.configure(bg="#E6F7FF")  # Light blue background

    font_style = ("Helvetica", 12, "bold")

    ttk.Label(window_absensi, text=f"Selamat datang, {nama}", background="#E6F7FF", font=font_style).grid(row=0, column=0, padx=20, pady=20, columnspan=2)

    ttk.Label(window_absensi, text="Keterangan Absensi", background="#E6F7FF", font=font_style).grid(row=1, column=0, padx=20, pady=20, sticky="w")
    keterangan_combobox = ttk.Combobox(window_absensi, values=["Hadir", "Sakit", "Izin", "Alfa"], state="readonly", font=("Helvetica", 12))
    keterangan_combobox.grid(row=1, column=1, padx=20, pady=20)

    ttk.Button(window_absensi, text="Absen", command=absensi_terbaru).grid(row=2, column=0, columnspan=2, pady=20)

# Fungsi untuk dashboard HRD (dengan opsi tambahan)
def hrd_window():
    def lihat_data():
        data = pd.read_excel(FILE_NAME)
        bulan = bulan_entry.get()
        if bulan.isdigit() and 1 <= int(bulan) <= 12:
            data["Tanggal"] = pd.to_datetime(data["Tanggal"], dayfirst=True, errors='coerce')
            filtered_data = data[data["Tanggal"].dt.month == int(bulan)]
            result_data = filtered_data[["Nama", "Tanggal", "Keterangan"]]
            result_data = result_data.sort_values(by="Tanggal")
            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
            if file_path:
                result_data.to_excel(file_path, index=False)
                messagebox.showinfo("Sukses", "Data absensi berhasil disimpan!")
        else:
            messagebox.showerror("Error", "Bulan tidak valid!")

    def hitung_gaji():
        bulan = bulan_entry.get()
        if bulan.isdigit() and 1 <= int(bulan) <= 12:
            data = pd.read_excel(FILE_NAME)
            data["Tanggal"] = pd.to_datetime(data["Tanggal"], dayfirst=True, errors='coerce')
            filtered_data = data[data["Tanggal"].dt.month == int(bulan)]
            gaji_karyawan = {}

            for _, row in filtered_data.iterrows():
                if row["Nama"] not in gaji_karyawan:
                    gaji_karyawan[row["Nama"]] = 0

                if row["Keterangan"] == "Hadir":
                    gaji_karyawan[row["Nama"]] += 100000
                elif row["Keterangan"] == "Sakit":
                    gaji_karyawan[row["Nama"]] += 50000
                elif row["Keterangan"] == "Izin":
                    gaji_karyawan[row["Nama"]] += 30000
                elif row["Keterangan"] == "Alfa":
                    gaji_karyawan[row["Nama"]] += 0

            result_data = pd.DataFrame(list(gaji_karyawan.items()), columns=["Nama", "Gaji"])
            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
            if file_path:
                result_data.to_excel(file_path, index=False)
                messagebox.showinfo("Sukses", "Gaji karyawan berhasil dihitung!")
        else:
            messagebox.showerror("Error", "Bulan tidak valid!")

    window_hrd = tk.Toplevel(main_window)
    window_hrd.title("HRD Dashboard")
    window_hrd.geometry("1280x649")

    # Background untuk HRD
    window_hrd.configure(bg="#FFF5E6")  # Light orange background

    font_style = ("Helvetica", 12, "bold")

    ttk.Label(window_hrd, text="Masukkan Bulan (1-12)", background="#FFF5E6", font=font_style).grid(row=0, column=0, padx=20, pady=20, sticky="w")
    bulan_entry = ttk.Entry(window_hrd, font=("Helvetica", 12))
    bulan_entry.grid(row=0, column=1, padx=20, pady=20)

    ttk.Button(window_hrd, text="Lihat Data Absensi", command=lihat_data).grid(row=1, column=0, columnspan=2, pady=20)
    ttk.Button(window_hrd, text="Hitung Gaji Karyawan", command=hitung_gaji).grid(row=2, column=0, columnspan=2, pady=20)

# Main window
main_window = tk.Tk()
main_window.title("Sistem Absensi Karyawan PT. Maju Jaya")
main_window.geometry("1280x649")  # Ukuran jendela

# Background untuk Main Window
main_window.configure(bg="#E6F7FF")  # Light blue background
bg_image = tk.PhotoImage(file="background.png")  
bg_label = tk.Label(main_window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

font_style = ("Helvetica", 14, "bold")

# Tambahkan text box judul
judul_label = tk.Label(
    main_window, 
    text="ABSENSI PT. MAJU JAYA MAKMUR", 
    font=("Helvetica", 24, "bold"), 
    bg="#E6F7FF", 
    fg="#000080"  # Warna teks biru gelap
)
judul_label.pack(pady=20)  # Menempatkan judul dengan jarak vertikal (padding)


# Background untuk Main Window
main_window.configure(bg="#E6F7FF")  # Light blue background
bg_image = tk.PhotoImage(file="background.png")  
bg_label = tk.Label(main_window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

font_style = ("Helvetica", 14, "bold")

# Menambahkan tombol login untuk karyawan dan HRD
ttk.Button(main_window, text="Login Karyawan", command=login_karyawan).pack(pady=20)
ttk.Button(main_window, text="Login HRD", command=login_hrd).pack(pady=20)

main_window.mainloop()