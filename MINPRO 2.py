from prettytable import PrettyTable

# list-list didalam PrettyTable-nya
Kendaraan = PrettyTable(["ID Kendaraan", "Jenis Kendaraan", "Nama Kendaraan", "Harga Sewa per Hari (Rp.)"]) # header table
Kendaraan.add_row([1, "Mobil", "Alphard", 5500000])
Kendaraan.add_row([2, "Mobil", "Fortuner", 1600000])
Kendaraan.add_row([3, "Mobil", "Innova Reborn", 600000])
Kendaraan.add_row([4, "Mobil", "Neo Avanza", 450000])
Kendaraan.add_row([5, "Mobil", "Xpander", 400000])
Kendaraan.add_row([6, "Mobil", "Avanza", 300000])
Kendaraan.add_row([7, "Mobil", "Sigra", 300000])
Kendaraan.add_row([8, "Motor", "HONDA PCX 160", 100000])
Kendaraan.add_row([9, "Motor", "Yamaha Nmax 155", 95000])
Kendaraan.add_row([10, "Motor", "Yamaha Aerox", 85000])
Kendaraan.add_row([11, "Motor", "Honda Vario 125", 75000])
Kendaraan.add_row([12, "Motor", "Yamaha Gear", 65000])
Kendaraan.add_row([13, "Motor", "Honda Scoopy", 60000])
Kendaraan.add_row([14, "Motor", "Yamaha Mio S", 50000])

# Fungsi menambahkan kendaraan (create)
def create():
    nomorTabel = len(Kendaraan.rows) + 1  # ID baru
    namaBarang = input("Masukkan jenis kendaraan baru = ")
    namakendaraan = input("Masukkan Nama Kendaraan baru = ")
    HargaSewa = input("Masukkan harga sewa perhari = ")
    
    # Menambahkan baris baru ke tabel
    Kendaraan.add_row([nomorTabel, namaBarang, namakendaraan, int(HargaSewa)])
    print("Data telah ditambahkan")
    menuAdmin()

# Fungsi melihat kendaraan (read)
def read():
    print(Kendaraan)

# Fungsi update kendaraan (update)
def update():
    print(Kendaraan)
    IDLama = int(input("Masukkan ID Kendaraan yang ingin diubah = "))
    
    # Cari ID yang ada di tabel
    found = False
    for row in Kendaraan._rows:
        if row[0] == IDLama:
            found = True 
            Kendaraan.del_row(Kendaraan._rows.index(row))
            namaBarang = input("Masukkan jenis kendaraan baru = ")
            namakendaraan = input("Masukkan Nama Kendaraan baru = ")
            HargaSewa = input("Masukkan harga sewa per hari = ")
            Kendaraan.add_row([IDLama, namaBarang, namakendaraan, int(HargaSewa)])
            print("Data telah diperbarui")
            break

    if not found:
        print("Kendaraan dengan ID tersebut tidak ditemukan")

    menuAdmin()

# Fungsi menghapus kendaraan (delete)
def delete():
    print(Kendaraan)
    KendaraanHapus = int(input("Masukkan ID Kendaraan yang ingin dihapus = "))
    
    # Cari ID yang ada di tabel
    found = False
    for row in Kendaraan._rows:
        if row[0] == KendaraanHapus:
            found = True
            Kendaraan.del_row(Kendaraan._rows.index(row))
            print(f"Data ID {KendaraanHapus} telah dihapus")
            break
    
    if not found:
        print("Kendaraan dengan ID tersebut tidak ditemukan")

    menuAdmin()

# Fungsi menu untuk admin
def menuAdmin():
    print("\n1. Tambahkan Kendaraan")
    print("2. Tampilkan Daftar Kendaraan")
    print("3. Update Data Kendaraan")
    print("4. Hapus Data Kendaraan")
    print("5. Keluar")
    while True:
        try:
            pilihmenu = int(input("Masukkan Kode Angka Menu = "))
            if pilihmenu == 1:
                create()
            elif pilihmenu == 2:
                read()
            elif pilihmenu == 3:
                update()
            elif pilihmenu == 4:
                delete()
            elif pilihmenu == 5:
                print("Program Berakhir")
                break
            else:
                print("Kode Angka Tidak Valid, Silahkan Coba Lagi")
        except ValueError:
            print("Masukkan angka yang valid.")

# Fungsi menu untuk penyewa
def menuPenyewa():
    sewaKendaraan = int(input("Masukkan ID Kendaraan = ")) 
    found = False
    for row in Kendaraan._rows:
        if row[0] == sewaKendaraan:
            found = True
            print(f"Kendaraan {row[2]} berhasil disewa!")
            Kendaraan.del_row(Kendaraan._rows.index(row))
    if not found:
        print("ID kendaraan tidak ditemukan")

# Fungsi login admin
def loginadmin():
    print("Login Dulu Ya :>")
    while True:
        username = input("Masukkan username = ")
        password = input("Masukkan password = ")

        # Username dan password ATMINT 
        if (username == "reffi1" and password == "reffi23121996"):
            print("Login berhasil")
            menuAdmin()
            break
        else:
            print("Username atau password salah. Coba lagi.")

def main():
    while True:
        print("\nAyo Dilihat Dulu Harga Sewanya :)")
        print("1. Lihat Kendaraan")
        print("2. Sewa Kendaraan")
        print("3. Keluar")
        opsi = input("Pilih opsi = ")
        if opsi == "1":
            read()
        elif opsi =="2":
            read()
            menuPenyewa()
            lanjut = input("Mau sewa lagi? (y/n) ")
            if lanjut == "y":
                menuPenyewa()
            else:
                print("Terima kasih telah menyewa di RENTAL SANTAI")
                break
        elif opsi == "3":
            break

        else:
            print("Input tidak valid.")


# Fungsi role penyewa/admin
def role():
    login = input("Anda adalah penyewa/admin = ").lower()
    if login == "penyewa":
        namaPenyewa = input("Nama = ")
        print(f"Selamat datang {namaPenyewa} di RENTAL SANTAI!")
        main()
    elif login == "admin":
        loginadmin()  
    else:
        print("Role tidak dikenal, coba lagi.")
        role()

role()
