# MINPRO-2 CRUD
## Muhammad Reffi Fadillah | 2409116034 | Sistem Informasi A
Mini project 2 DDP  

#Flowchart
![image](https://github.com/user-attachments/assets/80a12db9-b31f-4e19-b08f-bcb1e67b0633)


##program 
Dalam program ini, saya menggunakan function, looping, percabangan if else elif, dan PrettyTable
### Utama
Bagian utama untuk mengkonfirmasi apakah pengguna masuk sebagai penyew atau sebagai admin. Jika masuk sebagai penyewa, maka harus memasukkan nama penyewa. Menggunakan percabangan, dan pemanggilan fungsi
```
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
```
##List Kendaraan / list produk
Disini saya menggunakan prettytable dan list untuk membuat daftar produk
```
from prettytable import PrettyTable

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
```

##Menu Penyewa + transaksi
Jika berhasil masuk sebagai penyewa, maka akan ditampilkan menu khusus penyewa. Pengguna dapat mengakses menu "Lihat Kendaraan, "Sewa Kendaraan", dan "Keluar". Program dapat dihentikan dengan memilih opsi ketiga pada menu, atau saat penyewa tidak ingin melanjutkan proses penyewaan kendaraan. Penggunaan fungsi dalam program bertujuan untuk memudahkan pengelolaan kode dan memperjelas struktur program. Selain itu, penggunaan loop memastikan bahwa program tidak berhenti meskipun ada input yang tidak valid, sehingga pengguna dapat terus menginput ulang data yang benar tanpa harus memulai program dari awal.
```
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
```

##Menu Admin
Setelah berhasil masuk sebagai admin, akan ditampilkan menu khusus admin dengan wewenang untuk menambah (Create), menampilkan (Read), mengubah (Update), dan menghapus data kendaraan (Delete). Dengan menggunakan while loop, disediakan opsi untuk keluar agar admin dapat mengakhiri program. Setiap opsi di menu memanggil fungsi yang sesuai, kecuali untuk opsi keluar program.
```
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
```

###Menambah Data Kendaraan (Create)
Jika admin memilih opsi.1 maka admin dapat menambahkan jenis,nama, dan harga sewa perhari kendaraan baru
```
def create():
    nomorTabel = len(Kendaraan.rows) + 1  # ID baru
    namaBarang = input("Masukkan jenis kendaraan baru = ")
    namakendaraan = input("Masukkan Nama Kendaraan baru = ")
    HargaSewa = input("Masukkan harga sewa perhari = ")
    
    # Menambahkan baris baru ke tabel
    Kendaraan.add_row([nomorTabel, namaBarang, namakendaraan, int(HargaSewa)])
    print("Data telah ditambahkan")
    menuAdmin()
```

###Menampilakan Data Kendaraan (Read)
Jika admin emmilih opsi.2 maka admin dapat melihat langsung daftar kendaraan, jika daftar kendaraan telah diubah anda juga dapat melihatnya di opsi 2 ini.
```
def read():
    print(Kendaraan)
```

###Mengubah Data Kendaraan (Update)
Jika admin memilih opsi.3 maka admin dapat mengubah data kendaraan dengan memasukkan id kendaraan pada list kendaraan untuk mengidentifikasi kendaraan yang ingin diubah
```
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
```

###Menghapus Data Kendaraan (Delete)
Jika admin memilih opsi.4 maka admin dapat menghapus data kendaraan dengan memasukkan id kendaraan pada list kendaraan untuk mengidentifikasi kendaraan yang ingin dihapus
```
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
```

###Keluar (opsi tambahan)
Opsi ini merupakan tambahan bagi admin untuk keluar dari program. Jika admin memilih opsi 5, program akan langsung dihentikan.
```
elif pilihmenu == 5:
                print("Program Berakhir")
                break
            else:
                print("Kode Angka Tidak Valid, Silahkan Coba Lagi")
        except ValueError:
            print("Masukkan angka yang valid.")
```

###OUTPUT
##Sebagai Pembeli
![image](https://github.com/user-attachments/assets/c287cef3-832d-4ff5-8ccf-263c66dd6918)
![image](https://github.com/user-attachments/assets/22b65d86-6a52-4144-b381-d471eb22cd32)




##Sebagai Admin
![image](https://github.com/user-attachments/assets/e7565966-a788-4de8-b3fd-f21a64bb9bbc)
![image](https://github.com/user-attachments/assets/1e4de02f-58e6-46d0-bf21-4e3c3360931f)
![image](https://github.com/user-attachments/assets/db885f9d-b585-4238-a1ad-a150787577a4)
![image](https://github.com/user-attachments/assets/fbbf7da7-a51a-42a1-9e39-f2a23d7c1cf3)
![image](https://github.com/user-attachments/assets/c918df64-d3e2-4b20-b4d3-70134725853b)









 



