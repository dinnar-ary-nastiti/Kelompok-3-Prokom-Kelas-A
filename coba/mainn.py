import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from login_karyawan import login_karyawan
from login_hrd import login_hrd

def main_menu():
    for widget in main_window.winfo_children():
        widget.destroy()

    # Fungsi untuk memperbarui latar belakang
    def update_background(event):
        bg_image_resized = bg_image.resize((main_window.winfo_width(), main_window.winfo_height()))
        bg_photo = ImageTk.PhotoImage(bg_image_resized)
        bg_label.config(image=bg_photo)
        bg_label.image = bg_photo

    # Latar belakang
    bg_image = Image.open("finall/selamatdatang.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(main_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = bg_photo
    main_window.bind("<Configure>", update_background)

    # Tombol menu utama
    ttk.Button(
        main_window, text="Login Karyawan", command=lambda: login_karyawan(main_window),
        style="Custom.TButton"
    ).place(relx=0.5, rely=0.4, anchor="center")
    ttk.Button(
        main_window, text="Login HRD", command=lambda: login_hrd(main_window),
        style="Custom.TButton"
    ).place(relx=0.5, rely=0.5, anchor="center")
    ttk.Button(
        main_window, text="Keluar", command=main_window.destroy,
        style="Custom.TButton"
    ).place(relx=0.5, rely=0.6, anchor="center")

# Inisialisasi window utama
main_window = tk.Tk()
main_window.title("Absensi Karyawan PT. Maju Jaya Makmur")
main_window.geometry("1920x1080")
main_window.resizable(True, True)

# Gaya tombol
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