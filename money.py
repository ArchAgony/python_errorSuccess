import tkinter as tk
from tkinter import messagebox

def show_message():
    # Menampilkan pesan error dengan ikon tanda silang (X)
    messagebox.showerror("Error.", "Success!")

# Membuat jendela utama
root = tk.Tk()
root.title("Error Message Example")
root.geometry("200x100")

# Membuat tombol untuk memicu pesan
button = tk.Button(root, text="OK", command=show_message)
button.pack(expand=True)

# Menjalankan aplikasi
root.mainloop()
