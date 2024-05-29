users = {}

# Fungsi untuk registrasi
def register():
    print("=============================================================")
    print("                         Registrasi                          ")
    print("=============================================================")
    username = input("Masukkan username : ")
    if username in users:
        print("Username sudah ada. Silakan pilih username lain.")
        return False
    password = input("Masukkan password : ")
    users[username] = password
    print("Registrasi berhasil!")
    return True

# Fungsi untuk login
def login():
    print("=============================================================")
    print("                             Login                           ")
    print("=============================================================")
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")
    if username in users and users[username] == password:
        print("Login berhasil!")
        return True
    else:
        print("Username atau password salah.")
        return False

# Fungsi untuk menambah data gudang
def tambah_data_gudang(gudang):
    nama_barang = input("Masukkan Nama Barang           : ")
    kode_barang = input("Masukkan Kode Barang           : ")
    jumlah_barang = int(input("Masukkan Jumlah Barang         : "))

    for barang in gudang:
        if barang['kode'] == kode_barang:
            if barang['nama'] == nama_barang:
                barang['jumlah'] += jumlah_barang
                print(f"Jumlah barang '{nama_barang}' dengan kode '{kode_barang}' telah diperbarui menjadi {barang['jumlah']}.")
            else:
                print(f"Kode barang '{kode_barang}' sudah ada dengan nama barang yang berbeda.")
            break
    else:
        # Jika barang belum ada, tambahkan sebagai barang baru
        gudang.append({'nama': nama_barang, 'kode': kode_barang, 'jumlah': jumlah_barang})
        print(f"Barang '{nama_barang}' dengan kode '{kode_barang}' telah ditambahkan ke gudang.")

    # Urutkan gudang berdasarkan kode barang
    gudang.sort(key=lambda x: x['kode'])

# Fungsi untuk menghapus data gudang
def hapus_data_gudang(gudang):
    kode_barang = input("Masukkan Kode Barang yang akan dihapus : ")

    for barang in gudang:
        if barang['kode'] == kode_barang:
            gudang.remove(barang)
            print(f"Barang dengan kode '{kode_barang}' telah dihapus dari gudang.")
            break
    else:
        print(f"Barang dengan kode '{kode_barang}' tidak ditemukan di gudang.")

# Fungsi untuk mencari data gudang
def cari_data_gudang(gudang):
    kode_barang = input("Masukkan Kode Barang yang dicari : ")

    for barang in gudang:
        if barang['kode'] == kode_barang:
            print(f"Barang ditemukan : Nama: {barang['nama']}, Kode : {barang['kode']}, Jumlah : {barang['jumlah']}")
            break
    else:
        print(f"Barang dengan kode '{kode_barang}' tidak ditemukan di gudang.")

# Fungsi untuk melihat data gudang
def lihat_data_gudang(gudang):
    if gudang:
        print("Data Gudang : ")
        for barang in gudang:
            print(f"Nama : {barang['nama']}, Kode : {barang['kode']}, Jumlah : {barang['jumlah']}")
    else:
        print("Gudang kosong.")

# Fungsi utama untuk menjalankan program
def main():
    gudang = []
    authenticated = False

    while not authenticated:
        print("=============================================================")
        print("                     Program Data Barang                     ")
        print("1. Login")
        print("2. Register")
        print("=============================================================")
        pilihan = input("Pilih : ")

        if pilihan == '1':
            authenticated = login()
        elif pilihan == '2':
            if register():
                continue 
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    while True:
        print("=============================================================")
        print("Menu Gudang :")
        print("1. Tambah Data Gudang")
        print("2. Hapus Data Gudang")
        print("3. Cari Data Gudang")
        print("4. Lihat Data Gudang")
        print("5. Log out")
        print("=============================================================")
        pilihan = input("Pilih : ")

        if pilihan == '1':
            tambah_data_gudang(gudang)
        elif pilihan == '2':
            hapus_data_gudang(gudang)
        elif pilihan == '3':
            cari_data_gudang(gudang)
        elif pilihan == '4':
            lihat_data_gudang(gudang)
        elif pilihan == '5':
            print("Anda telah log out.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
