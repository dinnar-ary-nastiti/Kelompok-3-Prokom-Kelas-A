import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from bismillah.full import main_menu

# Inisialisasi window utama
main_window = tk.Tk()
main_window.title("Absensi Karyawan PT. Maju Jaya Makmur")
main_window.geometry("1920x1080")
main_window.resizable(True, True)

# Bind untuk memperbarui latar belakang saat ukuran berubah
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

# Style Tombol
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
main_menu(main_window)

main_window.mainloop()