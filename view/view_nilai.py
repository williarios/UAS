from model.daftar_nilai import *

def cetak_daftar_nilai():
    if dataMahasiswa.items():
        print("\n                         DAFTAR NILAI MAHASISWA                       ")
        print("========================================================================")
        print("| No |     NIM     |    Nama    | Tugas |  UTS  |  UAS  |  Nilai Akhir |")
        print("========================================================================")
        i = 0
        for x in dataMahasiswa.items():
            i += 1
            print("| {6:1} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:10} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
        print("========================================================================")
    else:
        print("\n                         DAFTAR NILAI MAHASISWA                       ")
        print("========================================================================")
        print("| No |    NIM      |    Nama    | Tugas |  UTS  |  UAS  |  Nilai Akhir |")
        print("========================================================================")
        print("|                                                                      |")
        print("========================================================================")


def cetak_hasil_pencarian():
    nim = input("Masukkan NIM        : ")
    if nim in dataMahasiswa.keys():
        print("\n                      DAFTAR NILAI MAHASISWA                      ")
        print("====================================================================")
        print("|     NIM     |    Nama    | Tugas |  UTS  |  UAS  |  Nilai Akhir  |")
        print("====================================================================")
        print("| {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6}  |".format(nim, dataMahasiswa[nim][0], dataMahasiswa[nim][1], dataMahasiswa[nim][2], dataMahasiswa[nim][3], dataMahasiswa[nim][4]))
        print("====================================================================")
    else:
        print("Datanya {0} Tidak Ada ".format(nim))