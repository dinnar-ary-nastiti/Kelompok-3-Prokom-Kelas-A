import tkinter as tk

# Fungsi untuk menambahkan frame dengan border dan judul
def create_titled_frame(parent, title):
    frame = tk.Frame(parent, bg="lightgray", bd=2, relief="ridge", padx=10, pady=10)
    label = tk.Label(frame, text=title, font=("Helvetica", 16, "bold"), bg="lightgray")
    label.pack(side="top", fill="x", pady=5)
    return frame