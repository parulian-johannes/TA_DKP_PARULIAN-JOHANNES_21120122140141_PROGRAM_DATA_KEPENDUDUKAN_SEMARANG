from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry

# Object Oriented Programming 1: Membuat class Penduduk
class Penduduk:
    def __init__(self, nama, NIK, tempat_lahir,tanggal_lahir, alamat, agama, pekerjaan, status):
        self.nama = nama
        self.NIK = NIK
        self.tempat_lahir = tempat_lahir
        self.tanggal_lahir = tanggal_lahir
        self.alamat = alamat
        self.agama = agama
        self.pekerjaan = pekerjaan
        self.status = status

class Kependudukan:
    def __init__(self):
        self.penduduk = []

    def tambah_penduduk(self, nama, NIK, tempat_lahir, tanggal_lahir, alamat,  agama, pekerjaan, status):
      penduduk_baru = Penduduk(nama, NIK, tempat_lahir, tanggal_lahir, alamat, agama, pekerjaan, status)
      self.penduduk.append(penduduk_baru)

    def cari_penduduk(self, nama):
        for penduduk in self.penduduk:
            if penduduk.nama == nama:
                return penduduk
        return None

    def tampilkan_data(self):
        print("Data Kependudukan Semarang:")
        for i, penduduk in enumerate(self.penduduk):
            print(f"No: {i+1}")
            print(f"Nama: {penduduk.nama}")
            print(f"NIK: {penduduk.NIK}")
            print(f"Tempat_Lahir: {penduduk.tempat_lahir}")
            print(f"tanggal_Lahir: {penduduk.tanggal_lahir}")
            print(f"Alamat: {penduduk.alamat}")
            print(f"Agama: {penduduk.agama}")
            print(f"Pekerjaan: {penduduk.pekerjaan}")
            print(f"Status: {penduduk.status}")
            print()

# GUI Programming: Menggunakan modul tkinter untuk GUI
class AplikasiGUI:
    def __init__(self):
        self.entry_NIK = None

    def hapus_karakter(self):
     self = self.entry_NIK.get()
     
    def __init__(self, kependudukan):
        self.kependudukan = kependudukan

        self.window = Tk()
        self.window.configure(bg="blue")
        self.window.title("Data Kependudukan Semarang")
        self.window.geometry("400x350")

        # Load and set the background image
        self.background_image = ImageTk.PhotoImage(Image.open("Lawang_Sewu_in_Semarang_City.jpg"))
        self.background_label = Label(self.window, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.image_logo = ImageTk.PhotoImage(Image.open("Foto2.png"))
        self.image_logo = ImageTk.PhotoImage(Image.open("Foto2.png").resize((200, 200)))
        self.image_label = Label(self.window, image=self.image_logo)
        self.image_label.place(relx=0.5, rely=0.40, anchor="center")
        
        # Menampilkan gambar menggunakan Label
        self.label = Label(self.window, text="Selamat Datang Di Data Kependudukan Semarang", font=("Arial", 12))
        self.label.place(relx=0.5, rely=0.75, anchor="center")

        self.button1 = Button(self.window, text="CARI", command=self.buka_jendela_tambah, font=("Arial", 10))
        self.button1.place(relx=0.25, rely=0.85, anchor="center")

        self.button2 = Button(self.window, text="TAMBAH PENDUDUK", command=self.buka_jendela_tambah2, font=("Arial", 10))
        self.button2.place(relx=0.7, rely=0.85, anchor="center")
        
    def buka_jendela_tambah(self):
        jendela_tambah = Toplevel(self.window)
        jendela_tambah.title("PENCARIAN PENDUDUK")
        jendela_tambah.geometry("300x200")

        label_nama = Label(jendela_tambah, text="Nama:")
        label_nama.pack()

        entry_nama = Entry(jendela_tambah)
        entry_nama.pack()

        button_cari = Button(jendela_tambah, text="Cari", command=lambda: self.cari_penduduk(jendela_tambah, entry_nama.get()))
        button_cari.pack()

    def buka_jendela_tambah2(self):
       jendela_tambah = Toplevel(self.window)
       jendela_tambah.title("TAMBAHKAN PENDUDUK")
       jendela_tambah.geometry("400x600")

       label_nama = Label(jendela_tambah, text="Nama:")
       label_nama.pack()

       self.entry_nama = Entry(jendela_tambah)
       self.entry_nama.pack()

       label_NIK = Label(jendela_tambah, text="NIK:")
       label_NIK.pack()

       self.entry_NIK = Entry(jendela_tambah)
       self.entry_NIK.pack()
       self.entry_NIK.bind("<Key>", lambda e: self.hanya_angka(e))
       self.entry_NIK.bind("<BackSpace>", self.hapus_karakter)

       label_tempatlahir = Label(jendela_tambah, text="Tempat Lahir:")
       label_tempatlahir.pack()

       self.entry_tempatlahir = Entry(jendela_tambah)
       self.entry_tempatlahir.pack()

       label_tanggal_lahir = Label(jendela_tambah, text="Tanggal Lahir:")
       label_tanggal_lahir.pack()

       self.entry_tanggal_lahir = DateEntry(jendela_tambah, date_pattern='dd/mm/yyyy')
       self.entry_tanggal_lahir.pack()

       label_alamat = Label(jendela_tambah, text="Alamat:")
       label_alamat.pack()

       self.entry_alamat = Entry(jendela_tambah)
       self.entry_alamat.pack()

       label_agama = Label(jendela_tambah, text="Agama:")
       label_agama.pack()

       agama_options = ['Islam', 'Kristen', 'Katolik', 'Hindu', 'Buddha', 'Konghucu']
       self.combobox_agama = Combobox(jendela_tambah, values=agama_options, state="readonly")
       self.combobox_agama.pack()

       label_pekerjaan = Label(jendela_tambah, text="Pekerjaan:")
       label_pekerjaan.pack()

       self.entry_pekerjaan= Entry(jendela_tambah)
       self.entry_pekerjaan.pack()

       label_status = Label(jendela_tambah, text="Status:")
       label_status.pack()

       status_options = ['Menikah', 'Belum Menikah']
       self.combobox_status = Combobox(jendela_tambah, values=status_options, state="readonly")
       self.combobox_status.pack()

       button_simpan = Button(jendela_tambah, text="Tambahkan", command=lambda: self.simpan_penduduk(jendela_tambah, self.entry_nama.get(), self.entry_NIK.get(), self.entry_tempatlahir.get(), self.entry_tanggal_lahir.get(), self.entry_alamat.get(), self.combobox_agama.get(), self.entry_pekerjaan.get(), self.combobox_status.get()))
       button_simpan.pack()

    def hanya_angka(self, event):
     if event.char.isdigit() and len(self.entry_NIK.get()) < 16:
        return None
     else:
        return "break"

    def hapus_karakter(self, event):
     if len(self.entry_NIK.get()) >= 16:
        return "break"
     else:
        return None

    def cari_penduduk(self, jendela, nama):
     if nama:
        penduduk = self.kependudukan.cari_penduduk(nama)
        if penduduk is not None:
            messagebox.showinfo("Informasi Penduduk", f"Biodata Penduduk:\n\nNama: {penduduk.nama}\nNIK: {penduduk.NIK}\nTempat lahir: {penduduk.tempat_lahir}\nTanggal lahir: {penduduk.tanggal_lahir}\nAlamat: {penduduk.alamat}\nAgama: {penduduk.agama}\nPekerjaan: {penduduk.pekerjaan}\nStatus: {penduduk.status}")
        else:
            messagebox.showinfo("Informasi Penduduk", "Penduduk tidak ditemukan.")
     else:
            messagebox.showerror("Kesalahan", "Masukkan keyword pencarian.")

    def simpan_penduduk(self, jendela ,nama, NIK, tempat_lahir, tanggal_lahir, alamat, agama, pekerjaan, status):
       self.kependudukan.tambah_penduduk(nama, NIK, tempat_lahir, tanggal_lahir, alamat, agama, pekerjaan, status)
       if nama and NIK and tempat_lahir and tanggal_lahir and alamat and agama and pekerjaan and status:
        messagebox.showinfo("Informasi Penduduk", "Penduduk berhasil ditambahkan")
       else:
        messagebox.showerror("Kesalahan", "Semua form harus diisi.")
        
       jendela.destroy()


    def destroy(self):
        self.window.destroy()
    
    def run(self):
        self.window.mainloop()

# Inisialisasi objek Kependudukan
kependudukan = Kependudukan()

# Inisialisasi objek AplikasiGUI
aplikasi = AplikasiGUI(kependudukan)

# Menjalankan aplikasi
aplikasi.run()