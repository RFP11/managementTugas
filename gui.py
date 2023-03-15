import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
import pygame
import os
import tkinter.messagebox as messagebox
import sqlite3
import datetime

okaeri_path = os.path.join("media", "ohayo.mp3")
wakey_path = os.path.join("media", "wakey_wakey.mp3")
word = os.path.join('media', "word.lnk")
bell = os.path.join("media", "bell.mp3")
pygame.init()
sound = pygame.mixer.Sound(okaeri_path)
sound.play()



# koneksi database
con = sqlite3.connect('tugas.db')
cursor = con.cursor()

# ambil hari dan konvert hari
today = datetime.datetime.today()
day_names = {
    'Monday': 'Senin',
    'Tuesday': 'Selasa',
    'Wednesday': 'Rabu',
    'Thursday': 'Kamis',
    'Friday': 'Jumat',
    'Saturday': 'Sabtu',
    'Sunday': 'Minggu'
}
day_name_en = today.strftime('%A')
day_name_id = day_names.get(day_name_en, 'Unknown')
class Notepad:

    def __init__(self, master):
        self.master = master
        master.title("Notepad")
        
        # Create Text widget
        self.text = tk.Text(master)
        self.text.pack(fill=tk.BOTH, expand=True)

        # Create Scrollbar widget
        self.scrollbar = tk.Scrollbar(master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Link Text widget to Scrollbar
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        # Create Menubar
        self.menu_bar = tk.Menu(master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        
        # Add commands to File menu
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)
        
        # Add File menu to Menubar
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        # Display Menubar
        self.master.config(menu=self.menu_bar)

        # Initialize filename variable
        self.filename = None

        # Bind Ctrl + S shortcut to save_file method
        self.master.bind('<Control-s>', self.save_file)

    def new_file(self):
        self.filename = None
        self.text.delete(1.0, tk.END)

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            self.text.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.text.insert(tk.END, f.read())

    def save_file(self, event=None):
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.text.get(1.0, tk.END))
        else:
            self.save_file_as()

    def save_file_as(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.text.get(1.0, tk.END))
# inisiasi gui
window = tk.Tk()
window.geometry("600x550")
window.configure(bg="white")
style = ttk.Style()
style.configure('My.TFrame', background='#f0f0f0')
poppins_font = font.Font(family="Poppins", size=9)
window.title("Management System")
window.resizable(False, False)

# frame home
input_frame = ttk.Frame(window)
input_frame.pack(padx = 10, pady=10, fill = "both", expand = True)

# frame kelompok
kelompok_frame = ttk.Frame(window)
kelompok_frame.pack(padx = 10, pady=10, fill = "both", expand = True)

# frame tambah tugas

# frame hapus tugas

#frame edit selesai

#frame tambah kelompok

#frame tambah anggota

#frame hapus kelompok

#frame hapus anggota

label_pembuka = ttk.Label(input_frame, text = "Selamat Datang", font = poppins_font)
label_pembuka.pack(pady =10)

label_pembuka = ttk.Label(kelompok_frame, text = "Selamat Datang", font = poppins_font)
label_pembuka.pack(pady =10)

time_label = tk.Label(input_frame, font=poppins_font, text="")
time_label_kelompok = tk.Label(kelompok_frame, font=poppins_font, text="")

def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label_kelompok.config(text=current_time)
    window.after(1000, update_time)
    if current_time == "07:00:00":
        bel = pygame.mixer.Sound(wakey_path)
        bel.play()
    if current_time == "10:00:00":
        bel = pygame.mixer.Sound(bell)
        bel.play()

time_label.pack(padx=10, pady = 10, fill = "x", expand=True)
time_label_kelompok.pack(padx=10, pady = 10, fill = "x", expand=True)
update_time()

def gantiTable():
    global table_tugas, table_mapel
    
    if table_tugas.winfo_ismapped():
        table_tugas.pack_forget()
        label_tabel.config(text="Jadwal Pelajaran")
        table_mapel.pack( padx=10, fill="x", expand=True)
    else:
        table_mapel.pack_forget()
        label_tabel.config(text="Tugas")
        table_tugas.pack( padx=10, fill="x", expand=True)


label_pembuka2 = ttk.Label(input_frame, text = "Apa yang bisa kami bantu", font = poppins_font)
label_pembuka2.pack(padx = 10,pady= 10,fill = "x", expand = True)

def masukanTugas():
    
    masukan_tugas = tk.Toplevel()
    masukan_tugas.title('Masukan Tugas Baru')
    masukan_tugas.geometry("400x300")

    masukan_tugas_frame = ttk.Frame(masukan_tugas)
    masukan_tugas_frame.pack(padx=10, pady=10, fill="both", expand=True)

    label_pembukaan1 = ttk.Label(masukan_tugas_frame, text="Pilih Mata Pelajaran", font=poppins_font)
    label_pembukaan1.pack()

    matpel = cursor.execute("SELECT id, nama_matpel FROM mata_pelajaran").fetchall()

    selected_matpel = tk.StringVar()
    matpel_menu = ttk.OptionMenu(masukan_tugas_frame, selected_matpel, "pilih mata pelajaran", *[row[1] for row in matpel])
    matpel_menu.pack(pady=10)

    label_nama_tugas = ttk.Label(masukan_tugas_frame, text="Masukan Nama Tugas", font=poppins_font)
    label_nama_tugas.pack()

    entry_nama_val = tk.StringVar()
    entry_nama_widget = tk.Entry(masukan_tugas_frame, textvariable = entry_nama_val)
    entry_nama_widget.pack(padx=10, fill = "x", expand = True)

    label_deadline = ttk.Label(masukan_tugas_frame, text="Masukan Berapa Lama Deadlinenya", font=poppins_font)
    label_deadline.pack()

    entry_hari_val = tk.IntVar()
    entry_hari_widget = tk.Entry(masukan_tugas_frame, textvariable=entry_hari_val)
    entry_hari_widget.pack(padx=10, fill = "x", expand = True)




    def masukanTugasBaru():
        try:
            sql = 'INSERT INTO tugas (id_matpel, id_jadwal, id_jadwal_matpel, nama_tugas, startline, deadline) VALUES (?,?,?,?,?,?)'
            selected_matpel_name = selected_matpel.get()
            nama = entry_nama_val.get()
            try:
                # try to convert the user input to an integer
                int_value = int(entry_hari_val.get())
                # set the value of the IntVar to the integer value
                entry_hari_val.set(int_value)
            except ValueError:
                # if the user input is not a valid integer, display an error message
                messagebox.showerror("Error", "Input must be an integer.")
            
            angka_hari = entry_hari_val.get()
            startline = datetime.datetime.today()
            jadwal = cursor.execute('select id from jadwal where hari = ?', (day_name_id,))
            jadwal_id = jadwal.fetchone()[0]
            jadwal_matpel = cursor.execute('select id from jadwal_mapel where id_jadwal = ?', (jadwal_id,))
            jadwal_matpel_id = jadwal_matpel.fetchone()[0]
            deadline = today + datetime.timedelta(days=angka_hari)
            selected_matpel_id = None
            for row in matpel:
                if row[1] == selected_matpel_name:
                    selected_matpel_id = row[0]
                    print(selected_matpel_id)
                    break
            values = (selected_matpel_id, jadwal_id, jadwal_matpel_id, nama, startline, deadline)
            print(nama)
            print(angka_hari)
            print(deadline)
            cursor.execute(sql, values)
            con.commit()

            # update the table view with the new data
            table_tugas.delete(*table_tugas.get_children())
            tugas = cursor.execute('SELECT mata_pelajaran.nama_matpel, jadwal.hari, tugas.nama_tugas, tugas.deadline, tugas.selesai FROM mata_pelajaran, jadwal, tugas WHERE mata_pelajaran.id = tugas.id_matpel AND jadwal.id = tugas.id_jadwal and tugas.selesai = 0')
            for row in tugas:
                table_tugas.insert("", tk.END, text="", values=row)
            masukan_tugas.destroy()

        except sqlite3.Error as error:
            print(f"Error while executing SQL query: {error}")
            con.rollback()
            masukan_tugas.destroy()



    masukan_tugas_btn1 = ttk.Button(masukan_tugas_frame, text="Masukan Tugas", command = masukanTugasBaru)
    masukan_tugas_btn1.pack(padx=10, fill = "x", expand = True)
    
    

masukan_tugas_btn = ttk.Button(input_frame, text="Masukan Tugas", command = masukanTugas)
masukan_tugas_btn.pack(padx=10, fill = "x", expand = True)

def editTugas():
    edit_tugas = tk.Toplevel()
    edit_tugas.title('Edit Tugas')
    edit_tugas.geometry("400x300")

    edit_tugas_frame = ttk.Frame(edit_tugas)
    edit_tugas_frame.pack(padx=10, pady=10, fill="both", expand=True)


    label_pilih = ttk.Label(edit_tugas_frame, text="Pilih Tugas yang sudah selesai", font=poppins_font)
    label_pilih.pack(padx=10, pady=10)

    listTugas = cursor.execute('SELECT id, nama_tugas FROM tugas where selesai = 0').fetchall()

    selected_tugas = tk.StringVar()
    tugas_menu = ttk.OptionMenu(edit_tugas_frame, selected_tugas, "Pilih Tugas", *[row[1] for row in listTugas])
    tugas_menu.pack(pady=10)

    def updateTugas():
        sql = 'UPDATE tugas SET selesai = 1 WHERE id = ?'
        print('hi')
        try:
            print('halo')
            selected_tugas_name = selected_tugas.get()
            for row in listTugas:
                if row[1] == selected_tugas_name:
                    selected_tugas_id = row[0]
                    print(selected_tugas_id)
                    break
            cursor.execute(sql, (selected_tugas_id,))

            con.commit()
            edit_tugas.destroy()

            table_tugas.delete(*table_tugas.get_children())
            tugas = cursor.execute('SELECT mata_pelajaran.nama_matpel, jadwal.hari, tugas.nama_tugas, tugas.deadline, tugas.selesai FROM mata_pelajaran, jadwal, tugas WHERE mata_pelajaran.id = tugas.id_matpel AND jadwal.id = tugas.id_jadwal and tugas.selesai = 0 ORDER BY tugas.deadline ASC')
            for row in tugas:
                table_tugas.insert("", tk.END, text="", values=row)
            edit_tugas.destroy()
        except sqlite3.Error as error:
            print(f"Error while executing SQL query: {error}")
            con.rollback()
            edit_tugas.destroy()


    edit_tugas_btn = ttk.Button(edit_tugas_frame, text = "Oke", command=updateTugas)
    edit_tugas_btn.pack(padx=10, fill = "x", expand = True)
    


edit_tugas_btn = ttk.Button(input_frame, text="Edit Tugas Selesai", command = editTugas)
edit_tugas_btn.pack(padx=10, fill = "x", expand = True)

ganti_table = ttk.Button(input_frame, text="Switch Table", command = gantiTable)
ganti_table.pack(padx=10, fill = "x", expand = True)

def msWord():
    os.startfile(word)

open_word = ttk.Button(input_frame, text="Buka MS WORD", command = msWord)
open_word.pack(padx=10, fill = "x", expand = True)

def notepad():
    note = tk.Tk()
    Notepad(note)
    

notepad_btn= ttk.Button(input_frame, text="Notepad", command = notepad)
notepad_btn.pack(padx=10, fill = "x", expand = True)

def hapusTugas():
    edit_tugas = tk.Toplevel()
    edit_tugas.title('Hapus Tugas')
    edit_tugas.geometry("400x300")

    edit_tugas_frame = ttk.Frame(edit_tugas)
    edit_tugas_frame.pack(padx=10, pady=10, fill="both", expand=True)


    label_pilih = ttk.Label(edit_tugas_frame, text="Pilih Tugas yang akan dihapus", font=poppins_font)
    label_pilih.pack(padx=10, pady=10)

    listTugas = cursor.execute('SELECT id, nama_tugas FROM tugas').fetchall()

    selected_tugas = tk.StringVar()
    tugas_menu = ttk.OptionMenu(edit_tugas_frame, selected_tugas, "Pilih Tugas", *[row[1] for row in listTugas])
    tugas_menu.pack(pady=10)

    def updateTugas():
        sql = 'DELETE FROM tugas WHERE id = ?'
        print('hi')
        try:
            print('halo')
            selected_tugas_name = selected_tugas.get()
            for row in listTugas:
                if row[1] == selected_tugas_name:
                    selected_tugas_id = row[0]
                    print(selected_tugas_id)
                    break
            cursor.execute(sql, (selected_tugas_id,))

            con.commit()
            edit_tugas.destroy()
            edit_tugas.destroy()
        except sqlite3.Error as error:
            print(f"Error while executing SQL query: {error}")
            con.rollback()
            edit_tugas.destroy()


    edit_tugas_btn = ttk.Button(edit_tugas_frame, text = "Oke", command=updateTugas)
    edit_tugas_btn.pack(padx=10, fill = "x", expand = True)
hapus_tugas_btn = ttk.Button(input_frame, text="Hapus Tugas", command = hapusTugas)
hapus_tugas_btn.pack(padx=10, fill = "x", expand = True)

def kelompok():
    input_frame.pack_forget()
    kelompok_frame.pack(padx = 10, fill = "both", expand = True)
    kelompok_frame.tkraise()

kelompok_page = ttk.Button(input_frame, text="Kelompok", command = kelompok)
kelompok_page.pack(padx=10, fill = "x", expand = True)


# Pages Kelompok

# gui
def backHome():
    kelompok_frame.pack_forget()
    input_frame.pack(padx = 10, fill = "both", expand = True)
    input_frame.tkraise()

back_page = ttk.Button(kelompok_frame, text="Home", command = backHome)
back_page.pack( padx = 10,fill = "x", expand = True)

def buatKelompok():
    buat_kelompok = tk.Toplevel()
    buat_kelompok.title('Buat Kelompok Baru')
    buat_kelompok.geometry("400x300")

    buat_kelompok_frame = ttk.Frame(buat_kelompok)
    buat_kelompok_frame.pack(pady=10, fill="both", expand=True)

    matpel1 = cursor.execute("SELECT id, nama_matpel FROM mata_pelajaran").fetchall()

    selected_matpel1 = tk.StringVar()
    matpel_menu = ttk.OptionMenu(buat_kelompok_frame, selected_matpel1, "Pilih Mata Pelajaran", *[row[1] for row in matpel1])
    matpel_menu.pack()

    label_pilih = ttk.Label(buat_kelompok_frame, text="Konteks", font=poppins_font)
    label_pilih.pack(padx=10)

    entry_konteks_val = tk.StringVar()
    entry_konteks_widget = tk.Entry(buat_kelompok_frame, textvariable=entry_konteks_val)
    entry_konteks_widget.pack(padx=10, fill = "x", expand = True)

    def konfirmasi():
        sql = 'insert into kelompok (id_matpel, konteks, created) values (?,?,?)'
        dateSet = datetime.datetime.now()
        date = dateSet.strftime('%Y-%m-%d')
        selected_matpel_name1 = selected_matpel1.get()
        for row in matpel1:
            if row[1] == selected_matpel_name1:
                selected_matpel_id1 = row[0]
                print(selected_matpel_id1)
                break
        konteks = entry_konteks_val.get()
        values = (selected_matpel_id1, konteks, date)
        try:
            cursor.execute(sql, values)
            con.commit()
            print("Kelompok berhasil dibuat!")
            table_kelompok.delete(*table_tugas.get_children())
            data_kelompok = cursor.execute('select kelompok.id, kelompok.konteks, kelompok.created, mata_pelajaran.nama_matpel from kelompok, mata_pelajaran where kelompok.id_matpel = mata_pelajaran.id')
            for row in data_kelompok:
                table_kelompok.insert("", tk.END, text="", values=row)
            buat_kelompok.destroy()
        except sqlite3.Error as error:
            print(f"Error while executing SQL query: {error}")
            con.rollback()
            buat_kelompok.destroy()


    buat_kelompok_btn = ttk.Button(buat_kelompok_frame, text="Konfirmasi", command = konfirmasi)
    buat_kelompok_btn.pack(padx=10, fill = "x", expand = True)


buat_kelompok_btn = ttk.Button(kelompok_frame, text="Buat Kelompok Baru", command = buatKelompok)
buat_kelompok_btn.pack(padx=10, fill = "x", expand = True)

def hapusKelompok():
    hapus_kelompok = tk.Toplevel()
    hapus_kelompok.title('Hapus Kelompok Baru')
    hapus_kelompok.geometry("400x300")

    hapus_kelompok_frame = ttk.Frame(hapus_kelompok)
    hapus_kelompok_frame.pack(padx=10, fill="both", expand=True)

    kelompok3 = cursor.execute('select id, konteks from kelompok').fetchall()

    selected_kelompok = tk.StringVar()
    kelompok_menu = ttk.OptionMenu(hapus_kelompok_frame, selected_kelompok, "Pilih Kelompok", *[row[1] for row in kelompok3])
    kelompok_menu.pack()

    def hapus():
        sql = 'delete from kelompok where id =?'
        selected_kelompok_name = selected_kelompok.get()
        for row in kelompok3:
            if row[1] == selected_kelompok_name:
                selected_kelompok_id = row[0]
                print(selected_kelompok_id)
                break
        values = (selected_kelompok_id,)
        try:
            cursor.execute(sql, values)
            con.commit()
            print("Kelompok berhasil dihapus!")
            table_kelompok.delete(*table_tugas.get_children())
            data_kelompok = cursor.execute('select kelompok.id, kelompok.konteks, kelompok.created, mata_pelajaran.nama_matpel from kelompok, mata_pelajaran where kelompok.id_matpel = mata_pelajaran.id')
            for row in data_kelompok:
                table_kelompok.insert("", tk.END, text="", values=row)
            hapus_kelompok.destroy()
        except sqlite3.Error as error:
            print(f"Error while executing SQL query: {error}")
            con.rollback()
            hapus_kelompok.destroy()

    hapus_kelompok_btn_konfirmasi = ttk.Button(hapus_kelompok_frame, text="Konfirmasi", command = hapus)
    hapus_kelompok_btn_konfirmasi.pack(padx=10, fill = "x", expand = True)

hapus_kelompok_btn = ttk.Button(kelompok_frame, text="Hapus Kelompok", command = hapusKelompok)
hapus_kelompok_btn.pack(padx=10, fill = "x", expand = True)




def anggota():
    anggota_root = tk.Toplevel()
    anggota_root.title("Anggota")
    anggota_root.geometry("500x400")

    anggota_frame = ttk.Frame(anggota_root)
    anggota_frame.pack(padx= 10, fill = "both", expand = True)

    
    label_pilih = ttk.Label(anggota_frame, text="Kelompok", font=poppins_font)
    label_pilih.pack(padx=10)
    
    kelompok3 = cursor.execute('select id, konteks from kelompok').fetchall()
    selected_kelompok = tk.StringVar()
    kelompok_menu = ttk.OptionMenu(anggota_frame, selected_kelompok, "Pilih Kelompok", *[row[1] for row in kelompok3])
    kelompok_menu.pack()

    anggota = ttk.Treeview(anggota_frame)
    anggota["columns"] = ("Nama")
    anggota.column("#0", width=0, stretch=tk.NO)
    anggota.pack(fill='x', expand=True)

    def lihatAnggota():
    # Get the ID of the selected kelompok
        selected_kelompok_name = selected_kelompok.get()
        for row in kelompok3:
            if row[1] == selected_kelompok_name:
                selected_kelompok_id1 = row[0]
                print(selected_kelompok_id1)
                
                break
        
        # Clear existing tree items
        anggota.delete(*anggota.get_children())
        anggota.insert("", tk.END, text="", values=selected_kelompok_name)
        # Retrieve anggota data for the selected kelompok
        sql = 'select nama from anggota where id_kelompok = ?'
        rows = cursor.execute(sql, (selected_kelompok_id1,)).fetchall()
        # Insert the anggota data into the treeview
        for row in rows:
            anggota.insert("", tk.END, text="", values=row)

    lihat_anggota = tk.Button(anggota_frame, text="Lihat Anggota", command=lihatAnggota)
    lihat_anggota.pack(padx = 10, fill ="x", expand = True)


    def tambahAnggota():
        tambah_anggota_page = tk.Toplevel()
        tambah_anggota_page.title('Tambah Anggota')
        tambah_anggota_page.geometry("400x300")

        tambah_tugas_frame = ttk.Frame(tambah_anggota_page)
        tambah_tugas_frame.pack(padx=10, fill="both", expand=True)

        kelompok3 = cursor.execute('select id, konteks from kelompok').fetchall()

        selected_kelompok = tk.StringVar()
        kelompok_menu = ttk.OptionMenu(tambah_tugas_frame, selected_kelompok, "Pilih Kelompok", *[row[1] for row in kelompok3])
        kelompok_menu.pack()

        label_pilih = ttk.Label(tambah_tugas_frame, text="Nama", font=poppins_font)
        label_pilih.pack(padx=10)

        entry_nama_val = tk.StringVar()
        entry_nama_widget = tk.Entry(tambah_tugas_frame, textvariable=entry_nama_val)
        entry_nama_widget.pack(padx=10, fill = "x", expand = True)

        def tambahkanAnggota():
            sql = 'insert into anggota (id_kelompok, nama) values(?,?)'
            selected_kelompok_name = selected_kelompok.get()
            nama = entry_nama_val.get()
            for row in kelompok3:
                if row[1] == selected_kelompok_name:
                    selected_kelompok_id = row[0]
                    print(selected_kelompok_id)
                    break
            values = (selected_kelompok_id, nama,)
            try:
                cursor.execute(sql, values)
                con.commit()
                print("Anggota berhasil ditambahkan!")
                anggota.delete(*anggota.get_children())
                anggota.insert("", tk.END, text="", values=selected_kelompok_name)
                # Retrieve anggota data for the selected kelompok
                sql = 'select nama from anggota where id_kelompok = ?'
                rows = cursor.execute(sql, (selected_kelompok_id,)).fetchall()
                # Insert the anggota data into the treeview
                for row in rows:
                    anggota.insert("", tk.END, text="", values=row)            
                    tambah_anggota_page.destroy()
            except sqlite3.Error as error:
                print(f"Error while executing SQL query: {error}")
                con.rollback()
                tambah_anggota_page.destroy()

        hapus_kelompok_btn_konfirmasi = ttk.Button(tambah_tugas_frame, text="Konfirmasi", command = tambahkanAnggota)
        hapus_kelompok_btn_konfirmasi.pack(padx=10, fill = "x", expand = True)

    tambah_anggota_btn = ttk.Button(anggota_frame, text="Tambah Anggota", command = tambahAnggota)
    tambah_anggota_btn.pack(padx=10, fill = "x", expand = True)

    

anggota_btn = ttk.Button(kelompok_frame, text="Kelompok", command = anggota)
anggota_btn.pack(padx=10, fill = "x", expand = True)

def tambahTugasKelompok():
    tugas_kelompok = tk.Toplevel()
    tugas_kelompok.title('Tambah Tugas Kelompok')
    tugas_kelompok.geometry("900x300")
    tugas_kelompok.resizable(False, False)

    tugas_kelompok_frame = ttk.Frame(tugas_kelompok)
    tugas_kelompok_frame.pack(padx=10, fill="both", expand=True)

    sql = '''select kelompok.konteks, mata_pelajaran.nama_matpel, tugas_kelompok.nama_tugas, tugas_kelompok.selesai from tugas_kelompok, kelompok, mata_pelajaran where tugas_kelompok.id_kelompok = kelompok.id and kelompok.id_matpel = mata_pelajaran.id and tugas_kelompok.selesai = 0'''

    cursor.execute(sql)
    result = cursor.fetchall()

    label_pilih = ttk.Label(tugas_kelompok_frame, text="Tugas Kelompok", font=poppins_font)
    label_pilih.pack(padx=10)

    tree = ttk.Treeview(tugas_kelompok_frame)
    tree.pack(fill='x', expand=True)

    columns = ('Konteks', 'Mata Pelajaran', 'Nama Tugas', 'Selesai')
    tree['columns'] = columns
    tree.heading('#0', text='ID')
    tree.column('#0', width=0, stretch=tk.NO)
    for col in columns:
        tree.heading(col, text=col)

    # Add the data to the Treeview
    for i, row in enumerate(result):
        tree.insert(parent='', index='end', iid=i, text=i, values=row)

    def tambah():
        tambah_page = tk.Toplevel()
        tambah_page.title('Tambah Tugas Kelompok')
        tambah_page.geometry("400x300")
        tambah_page_frame = ttk.Frame(tambah_page)
        tambah_page_frame.pack(padx=10, fill="both", expand=True)

    tugas_kelompok_btn_tambah = ttk.Button(tugas_kelompok_frame, text="Tambah Tugas Kelompok", command = tambah)
    tugas_kelompok_btn_tambah.pack(padx=10, fill = "x", expand = True)
    

tugas_kelompok_btn = ttk.Button(kelompok_frame, text="Tugas Kelompok", command = tambahTugasKelompok)
tugas_kelompok_btn.pack(padx=10, fill = "x", expand = True)

label_tabel = ttk.Label(input_frame, text = "Tugas", font = poppins_font)
label_tabel.pack(padx = 10, fill = "x", expand = True)

# table tugas
table_tugas = ttk.Treeview(input_frame)
table_tugas["columns"] = ("Mata Pelajaran", "Hari", "Nama Tugas", "Deadline", "Selesai")

table_tugas.column("#0", width=0, stretch=tk.NO)
table_tugas.column("Mata Pelajaran", width=100)
table_tugas.column("Hari", width=100)
table_tugas.column("Nama Tugas", width=100)
table_tugas.column("Deadline", width=100)
table_tugas.column("Selesai", width=100)

table_tugas.heading("#0", text="")
table_tugas.heading("Mata Pelajaran", text="Mata Pelajaran")
table_tugas.heading("Hari", text="Hari")
table_tugas.heading("Nama Tugas", text="Nama Tugas")
table_tugas.heading("Deadline", text="Deadline")
table_tugas.heading("Selesai", text="Selesai")

tugas = cursor.execute('SELECT mata_pelajaran.nama_matpel, jadwal.hari, tugas.nama_tugas, tugas.deadline, tugas.selesai FROM mata_pelajaran, jadwal, tugas WHERE mata_pelajaran.id = tugas.id_matpel AND jadwal.id = tugas.id_jadwal and tugas.selesai = 0')

for row in tugas:
    table_tugas.insert("", tk.END, text="", values=row)
table_tugas.pack(padx=10, fill ="x", expand=True)

# table jadwal
table_mapel = ttk.Treeview(input_frame)
table_mapel["columns"] = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat")

table_mapel.column("#0", width=0, stretch=tk.NO)
table_mapel.column("Senin", width=100)
table_mapel.column("Selasa", width=100)
table_mapel.column("Rabu", width=100)
table_mapel.column("Kamis", width=100)
table_mapel.column("Jumat", width=100)

table_mapel.heading("#0", text ="")
table_mapel.heading("Senin", text= "Senin")
table_mapel.heading("Selasa", text= "Selasa")
table_mapel.heading("Rabu", text= "Rabu")
table_mapel.heading("Kamis", text= "Kamis")
table_mapel.heading("Jumat", text= "Jumat")

table_mapel.insert("", tk.END, text="1", values=("Inggris", "PKK", "PKN", "Sunda", "Sunda"))
table_mapel.insert("", tk.END, text="2", values=("PAI", "Indonesia", "Sejarah", "Indonesia", "Sejarah"))
table_mapel.insert("", tk.END, text="3", values=("PKN", "BK", "Olahraga", "Matematika", "PKK"))
table_mapel.insert("", tk.END, text="4", values=(" ", " ", "PAI", "Inggris", "Matematika"))

table_mapel.pack_forget()


#treeview kelompok
table_kelompok = ttk.Treeview(kelompok_frame)
table_kelompok["columns"] = ("Id", "Konteks", "Dibuat", "Mata Pelajaran")
table_kelompok.column("#0", width=0, stretch=tk.NO)
table_kelompok.column("Id", width=100)
table_kelompok.column("Konteks", width=100)
table_kelompok.column("Dibuat", width=100)
table_kelompok.column("Mata Pelajaran", width=100)

table_kelompok.heading("#0", text="")
table_kelompok.heading("Id", text="Id")
table_kelompok.heading("Konteks", text="Konteks")
table_kelompok.heading("Dibuat", text="Dibuat")
table_kelompok.heading("Mata Pelajaran", text="Mata Pelajaran")

data_kelompok = cursor.execute('select kelompok.id, kelompok.konteks, kelompok.created, mata_pelajaran.nama_matpel from kelompok, mata_pelajaran where kelompok.id_matpel = mata_pelajaran.id')

for row in data_kelompok:
    table_kelompok.insert("", tk.END, text="", values=row)

table_kelompok.pack(padx=10, fill="x", expand=True)

window.mainloop()