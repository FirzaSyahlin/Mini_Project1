aplikasi = []

while True:
    print("SISTEM PENDATAAN APLIKASI DI HP")
    print("1. Tambah Aplikasi")
    print("2. Lihat Aplikasi")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama aplikasi: ")
        aplikasi.append(nama)
        print("Data aplikasi berhasil ditambahkan.")

    elif pilihan == "2":
        print("Daftar Aplikasi:")
        for nama in aplikasi:
            print(nama)

    elif pilihan == "3":
        print("Program selesai.")
        break