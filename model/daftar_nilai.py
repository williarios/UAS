from view.input_nilai import *

dataMahasiswa = {}      # ini dictionary yg berisi item2

def tambah_data():
    nim = input_nim()
    namaMahasiswa = input_nama()        # item nama
    nilaiTugas = input_nilai_tugas()    # item nilaiTugas
    nilaiUts = input_nilai_uts()         # item nilaiUts
    nilaiUas = input_nilai_uas()         # item nilaiUas
    nilaiAkhir = int((nilaiTugas + nilaiUts + nilaiUas)/3)   # item nilaiAkhir
    dataMahasiswa[nim] = namaMahasiswa, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir  # key dari dictionarynya nim
    print("\nData " + nim + " Berhasil Ditambahkan!")
    return dataMahasiswa

def ubah_data():
    nim = input("Masukkan NIM          : ")
    if nim in dataMahasiswa.keys():         # mengecek data sesuai dengan key nim
        nama = input_nama()
        nilaiTugas = input_nilai_tugas()
        nilaiUts = input_nilai_uts()
        nilaiUas = input_nilai_uas()
        nilaiAkhir = int((nilaiTugas + nilaiUts + nilaiUas)/3)
        dataMahasiswa[nim] = nama, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
        print("\nData " + nim + " Berhasil Di Update!")
    else:
        print("Data " + nim + " tidak ditemukan!")


def hapus_data():
    nim = input("Masukan NIM : ")
    if nim in dataMahasiswa.keys():
        del dataMahasiswa[nim]
        print("Data ",nim, " Telah dihapus!")
    else:
        print("Data Mahasiswa Tidak Ada".format(nim))