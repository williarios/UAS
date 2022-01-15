from view.view_nilai import *

while True:
    print("1.Tambah   2.Ubah   3.Cari   4.Hapus   5.Lihat   0.Keluar")
    menu = input("Pilih Menu : ")

    if menu == "1":
        tambah_data()
        cetak_daftar_nilai()

    elif menu == "2":
        ubah_data()
        cetak_daftar_nilai()

    elif menu == "3":
        cetak_hasil_pencarian()

    elif menu == "4":
        hapus_data()
        cetak_daftar_nilai()

    elif menu == "5":
        cetak_daftar_nilai()

    elif menu == "0":
        break

    else:
        print("Pilihan menu tidak tersedia")