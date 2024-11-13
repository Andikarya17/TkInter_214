import tkinter as tk  # Mengimpor pustaka tkinter dengan alias 'tk' untuk membuat antarmuka GUI
from tkinter import messagebox  # Mengimpor messagebox dari tkinter untuk menampilkan pesan dialog (seperti pesan kesalahan)

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try: 
        # Mengiterasi setiap entry dalam list entries untuk mendapatkan nilai input
        for entry in entries:
            nilai = int(entry.get())  # Mengonversi nilai input dari string ke integer
            if not (0 <= nilai <= 100):  # Memeriksa apakah nilai berada dalam rentang 0-100
                raise ValueError("Nilai harus antara 0 dan 100.")  # Jika tidak, munculkan error
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")  # Tampilkan prediksi jika semua input valid
    except ValueError as ve:
        # Menampilkan pesan error jika ada nilai yang tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat objek utama dari tkinter yang akan menjadi window aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Memberikan judul pada window aplikasi
root.geometry("500x600")  # Mengatur ukuran window aplikasi
root.configure(bg="#f0f0f0")  # Mengatur warna latar belakang window

# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#f0f0f0")
judul_label.pack(pady=20)  # Menampilkan label judul dengan padding atas dan bawah

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#f0f0f0")  # Membuat frame sebagai wadah untuk input nilai
frame_input.pack(pady=10)  # Menampilkan frame dengan sedikit jarak di bagian atas dan bawah

# Membuat list untuk menyimpan kotak input nilai
entries = []
for i in range(10):  # Loop untuk membuat 10 kotak input nilai
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Menampilkan label untuk setiap mata pelajaran
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))  # Membuat kotak input untuk nilai mata pelajaran
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menempatkan kotak input di sebelah kanan label
    entries.append(entry)  # Menambahkan kotak input ke dalam list entries

# Tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#4CAF50", fg="black")
prediksi_button.pack(pady=30)  # Menampilkan tombol dengan padding atas dan bawah

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="blue", bg="#f0f0f0")
hasil_label.pack(pady=20)  # Menampilkan label kosong untuk hasil prediksi dengan padding atas dan bawah

# Memulai mainloop tkinter untuk menjalankan aplikasi
root.mainloop()
