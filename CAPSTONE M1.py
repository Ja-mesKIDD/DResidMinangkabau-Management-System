##CAPSTONE MODULE 1##
import random as rd
import datetime as dt
from tabulate import tabulate as tb
import os

#DAFTAR MENU#
pilihanMenu = {
    "menu_utama":{
        1 : "Tipe & Harga Kamar",
        2 : "Data Penghuni Kos - Kosan",
        3 : "Hapus Data Penghuni",
        4 : "Pembayaran Kamar Kosan",
        5 : "Penggantian Data",
        0 : "Keluar Program"
    },
    "SubMenu" :{
        1 : "Penghuni Lama",
        2 : "Penghuni Baru",
    },
    "SubMenu2" : {
        1 : "Masukkan Data Penghuni Baru",
        2 : "Pembayaran Sewa Kamar Kos Penghuni Lama",
    },
    "SubMenu3" : {
        1 : "Edit Nama Penghuni",
        2 : "Tipe Kamar"
    }
}

#DATA KAMAR#
RoomData= {
    "Tipe Kamar" :{
        0 : "Kamar Bronze",
        1 : "Kamar Gold",
    },
    "Harga Kamar" : {
        0 : 1600000,
        1 : 1800000,
    },
    "Diskon" :{
        0 : 0.1,
        1 : 0.2, 
    },
    "Lantai":{
        0 : [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        1 : [201, 202, 203, 204, 205, 206, 207, 208, 209, 210]
    },
}

#DATA PENGHUNI#
DataPelanggan ={
        0 : {
        "Nama" : "Nicholas",
        "Terakhir Bayar": "2023-10-09",
        "Tipe Kamar" : "Kamar Bronze",
        "Nomor Kamar" : 104,
        "Durasi Sewa" : 2},
        1 : {
        "Nama" : "Faheed",
        "Terakhir Bayar": "2023-05-03",
        "Tipe Kamar" : "Kamar Bronze",
        "Nomor Kamar" : 106,
        "Durasi Sewa" : 6},
        2 :{
        "Nama" : "Sidgi",
        "Terakhir Bayar": "2023-10-19",
        "Tipe Kamar" : "Kamar Gold",
        "Nomor Kamar" : 202,
        "Durasi Sewa" : 3},
        3 :{
        "Nama" : "Batistuta",
        "Terakhir Bayar": "2023-06-03",
        "Tipe Kamar" : "Kamar Gold",
        "Nomor Kamar" : 209,
        "Durasi Sewa" : 12},
    }

#FUNGSI MENCETAK KAMAR YANG TERISI#
def KamarIsi():
    listPelanggan = []
    for i in range(len(DataPelanggan)+1):
        if i in DataPelanggan.keys():
            dur = sisa(i)
            if dur>0:
                terlambat = dur
            elif dur <=0:
                terlambat = 0
            listPelanggan.append([DataPelanggan[i]["Nomor Kamar"],DataPelanggan[i]["Nama"],DataPelanggan[i]["Tipe Kamar"],
                                DataPelanggan[i]["Terakhir Bayar"],(f"{DataPelanggan[i]["Durasi Sewa"]} bulan"),(f"{terlambat} hari")])
        else:
            i+=1
            continue
        heads = ["Nomor Kamar","Nama", "Tipe Kamar","Terakhir Bayar", "Durasi Sewa","Durasi Denda"]
    print(tb(listPelanggan, headers=heads, tablefmt="fancy_grid", stralign="center"))

#FUNGSI MENCETAK KAMAR YANG TERSEDIA#
def KamarKosong():
    isi = []
    for i in range(len(DataPelanggan)):
        isi.append(DataPelanggan[i]["Nomor Kamar"])
    p,q =RoomData["Lantai"].values()
    global kosong1
    global kosong2
    kosong1 = []
    kosong2 = []
    for i in range(len(p)):
        if p[i] not in isi:
            kosong1.append(p[i])
    for j in range(len(q)):
        if q[j] not in isi:
            kosong2.append(q[j])
    return kosong1, kosong2

#FUNGSI UNTUK MENCETAK TABEL KAMAR KOSONG#
def cetakKamar(nomorKamar):
    if nomorKamar is kosong1:
        cetaktipe = [RoomData["Tipe Kamar"][0]] * len(nomorKamar)
        cetakharga = [RoomData["Harga Kamar"][0]] * len(nomorKamar)
    elif nomorKamar is kosong2:
        cetaktipe = [RoomData["Tipe Kamar"][1]] * len(nomorKamar)
        cetakharga = [RoomData["Harga Kamar"][1]] * len(nomorKamar)
    table = list(zip(cetaktipe, nomorKamar, cetakharga))
    print(tb(table, headers=["Tipe Kamar", "Nomor Kamar", "Harga"], tablefmt="fancy_grid"))
    print()

#FUNGSI MENGHAPUS DATA PENGHUNI#
def HapusData(x):
    for i in range(len(DataPelanggan)):
        if x == DataPelanggan[i]["Nomor Kamar"]:
            DataPelanggan.pop(i)
    KamarIsi()

#FUNGSI MEMASUKKAN DATA PENGHUNI BARU#
def DataBaru(x,y,z):
    id = len(DataPelanggan)
    lt1,lt2 = KamarKosong()
    if y == "Kamar Bronze":
        nk = rd.choice(lt1)
    elif y == "Kamar Gold":
        nk = rd.choice(lt2)
    DataPelanggan[id]= {
        "Nama" : x,
        "Terakhir Bayar": dt.datetime.strftime(dt.date.today(), "%Y-%m-%d"),
        "Tipe Kamar" : y,
        "Nomor Kamar" : nk,
        "Durasi Sewa" : z}
    return DataPelanggan

#FUNGSI PINDAH KAMAR#
def pindah(j,k,l):
    IDPindah = cekID(j,"Nomor Kamar")
    dendaPindah = hitungdenda(IDPindah)
    sewaPindah = hitungsewa(k,l)
    TBPindah = dendaPindah + sewaPindah
    DataPelanggan[IDPindah]["Tipe Kamar"] = tipePindah
    lt1,lt2 = KamarKosong()
    if l == "Kamar Bronze":
        nomorPindah = rd.choice(lt1)
    elif l == "Kamar Gold":
        nomorPindah = rd.choice(lt2)
    DataPelanggan[IDPindah]["Nomor Kamar"] = nomorPindah
    DataPelanggan[IDPindah]["Durasi Sewa"] += durPindah
    return TBPindah

#FUNGSI CEK ID PENGHUNI#
def cekID(cari, konci):
    idkunci = [key for key, data in DataPelanggan.items() if data[konci] == cari]
    idHuni = idkunci[0]
    return idHuni

#FUNGSI CEK SISA SEWA#
def sisa(x):
    z = DataPelanggan[x]["Durasi Sewa"] *30
    y = int((dt.date.today() - dt.datetime.strptime(DataPelanggan[x]["Terakhir Bayar"], "%Y-%m-%d").date()).days)
    durasi = y-z
    return durasi

#FUNGSI MENGHITUNG DENDA#
def hitungdenda(x):
    dur = sisa(x)
    if dur > 0:
        if DataPelanggan[x]["Tipe Kamar"] == "Kamar Bronze":
            denda = (dur)*(RoomData["Harga Kamar"][0]*0.05)
            print(f"Denda keterlambatan anda sebesar {denda}")
        elif DataPelanggan[x]["Tipe Kamar"] == "Kamar Gold":
            denda = (dur)*(RoomData["Harga Kamar"][1]*0.05)
            print(f"Denda keterlambatan anda sebesar {denda}")
    elif dur<=0:
        denda = 0
    return denda

#FUNGSI UNTUK MENGHITUNG SEWA#    
def hitungsewa(x,y):
    sewa = 0
    while True:
        if y == "Kamar Bronze":
            if x < 6:
                sewa = (x*RoomData["Harga Kamar"][0])
                break
            elif x == 6 or x%12 !=0 and x%6==0:
                sewa = (x*RoomData["Harga Kamar"][0])
                diskon = sewa*RoomData["Diskon"][0]
                sewa = sewa-diskon
                print(f"\nSelamat, anda mendapatkan diskon sebesar {diskon}\n")
                break
            elif x%12 == 0:
                sewa = (x*RoomData["Harga Kamar"][0])
                diskon = sewa*RoomData["Diskon"][1]
                sewa = sewa - diskon
                print(f"\nSelamat, anda mendapatkan diskon sebesar {diskon}\n")
                break
            elif x > 6 and x < 12:
                z = x%6
                sewa = (6*RoomData["Harga Kamar"][0])
                diskon = sewa*RoomData["Diskon"][0]
                sewa = sewa - diskon +(z*RoomData["Harga Kamar"][0])
                print(f"\nSelamat, anda mendapatkan diskon sebesar {diskon}\n")
                break
            elif x>12 and x%12!=0 and x%6!=0:
                z = x%12
                sewa = ((x/12)*RoomData["Harga Kamar"][0])
                diskon = sewa*RoomData["Diskon"][1]
                sewa = sewa - diskon +(z*RoomData["Harga Kamar"][0])
                print(f"\nSelamat anda mendapatkan diskon sebesar {diskon}\n")
                break
        elif y == "Kamar Gold":
            if x < 6:
                sewa = (x*RoomData["Harga Kamar"][0])
                break
            elif x == 6 or x%12 !=0 and x%6==0:
                sewa = (x*RoomData["Harga Kamar"][0])
                diskon = sewa*RoomData["Diskon"][0]
                sewa = sewa-diskon
                print(f"\nSelamat, anda mendapatkan diskon sebesar {diskon}\n")
                break
            elif x%12 == 0:
                sewa = (x*RoomData["Harga Kamar"][0])
                diskon = sewa*RoomData["Diskon"][1]
                sewa = sewa - diskon
                print(f"\nSelamat, anda mendapatkan diskon sebesar {diskon}\n")
                break
            elif x > 6 and x < 12:
                z = x%6
                sewa = (6*RoomData["Harga Kamar"][0])
                diskon = sewa*RoomData["Diskon"][0]
                sewa = sewa - diskon +(z*RoomData["Harga Kamar"][0])
                print(f"\nSelamat, anda mendapatkan diskon sebesar {diskon}\n")
                break
            elif x>12 and x%12!=0 and x%6!=0:
                z = x%12
                sewa = ((x/12)*RoomData["Harga Kamar"][0])
                diskon = sewa*RoomData["Diskon"][1]
                sewa = sewa - diskon +(z*RoomData["Harga Kamar"][0])
                print(f"\nSelamat anda mendapatkan diskon sebesar {diskon}\n")
                break
    return sewa

#FUNGSI TRANSAKSI#
def Transaksi(x,y,z):
    IDh = cekID(x,y)
    bayarDenda = hitungdenda(IDh)
    bayarSewa = hitungsewa(z,DataPelanggan[IDh]["Tipe Kamar"])
    jumlahBayar = round((bayarSewa + bayarDenda),2)
    DataPelanggan[IDh]["Durasi Sewa"] += z
    return jumlahBayar

#FUNGSI UNTUK KEMBALI KE MENU UTAMA#
def keluar():
    while True:
        subMenuInput = int(input("Input 0 untuk kembali ke menu utama: "))
        if subMenuInput == 0:
            clearScreenView()
            break
        else:
            continue


# FUNGSI UNTUK CLEAR TERMINAL#
def clearScreenView() :
    if os.name == 'posix' : # for macos / linux
        os.system('clear')
    if os.name == 'nt' : # for windows
        os.system('cls')


#PROGRAM DIMULAI DARI SINI#
clearScreenView()

while True:
    try:
        print("\nSELAMAT DATANG DI SISTEM DATA D\'RESIDENCE MINANGKABAU\n")
        for i in pilihanMenu["menu_utama"]:
            print(f"{i}. {pilihanMenu["menu_utama"][i]}")
        menuInput = input("Masukkan menu yang ingin diakses: ")
        while True:
                try:                
                    if menuInput.isnumeric():
                        menuInput = int(menuInput)
                        break
                except:
                    print("Masukkan pilihan menu dalam bentuk angka.")
        if menuInput == 1:
                print("\n Berikut daftar kamar yang tersedia beserta harganya: \n")
                KamarKosong()
                cetakKamar(kosong1)
                cetakKamar(kosong2)
                keluar()
        elif menuInput == 2:
            print("\n Berikut data penghuni Kosan D\'Residence Minangkabau: ")
            KamarIsi()
            keluar()
        elif menuInput == 3:
            KamarIsi()
            while True:
                try:    
                    hapusHuni = int(input("Masukkan nomor kamar penghuni yang keluar: "))
                    HapusData(hapusHuni)
                    keluar()
                    break
                except:
                    print("Masukkan nomor kamar dalam bentuk ANGKA.")
        elif menuInput == 4 :
            for i in pilihanMenu["SubMenu"]:
                print(f"{i}. {pilihanMenu["SubMenu"][i]}")
            while True:
                subInput = int(input("Masukkan menu yang ingin diakses: "))
                if subInput == 1:
                    print(pilihanMenu["SubMenu2"][2])
                    while True:
                        try:    
                            KamarIsi()
                            kamarHuni = int(input("Masukkan nomor kamar: "))
                            lamaBayar = int(input("Masukkan durasi sewa yang ingin dibayar: "))
                            while True:
                                nilaiBayar = Transaksi(kamarHuni,"Nomor Kamar",lamaBayar)
                                print(f"Jumlah yang harus dibayar sebesar: {nilaiBayar}\n")
                                UangBayar = int(input("Masukkan Jumlah Uang Anda :")) 
                                Kembalian = UangBayar - nilaiBayar
                                if Kembalian < 0:
                                    Kembalian = Kembalian * -1
                                    print(f"\nTransaksi anda BATAL, kekurangan uang sebesar {Kembalian}")
                                elif Kembalian == 0:
                                    print("\nUang anda pas \nTERIMAKASIH TELAH MEMBAYAR SEWA KOSAN ANDA\n")
                                    break
                                else:
                                    print(f"\nKembalian anda sebesar {Kembalian} \nTERIMAKASIH TELAH MEMBAYAR SEWA KOSAN ANDA\n")
                                    break
                        except:
                            print("Kamar tersebut tidak ada penghuni.")
                            continue        
                        keluar()
                        break
                    break        
                elif subInput ==2:
                    print(pilihanMenu["SubMenu2"][1])
                    while True:
                        try:
                            namaBaru = input("Masukkan nama calon penghuni baru: ")
                            KamarKosong()
                            subMenuInput = input("Ingin melihat tipe kamar yang tersedia? (Y/N): ").upper()
                            if subMenuInput == "Y":
                                cetakKamar(kosong1)
                                cetakKamar(kosong2)
                            for i in RoomData["Tipe Kamar"]:
                                print(f"{i}. {RoomData["Tipe Kamar"][i]}")                            
                            pilihtipe = int(input("Masukkan tipe kamar yang disewa: "))
                            if pilihtipe == 0:
                                tipeBaru = RoomData["Tipe Kamar"][0]
                            elif pilihtipe == 1:
                                tipeBaru = RoomData["Tipe Kamar"][1]
                            lamaBaru = int(input("Masukkan lama durasi sewa: "))
                            DataBaru(namaBaru,tipeBaru,lamaBaru)
                            KamarIsi()
                            IDBaru = cekID(namaBaru,"Nama")
                            kamarBaru = DataPelanggan[IDBaru]["Nomor Kamar"]
                            subMenuInput2 = input("Lanjutkan ke Pembayaran? (Y/N): ").upper()
                            if subMenuInput2 == "Y":    
                                while True:
                                    nilaiBayar = Transaksi(kamarBaru,"Nomor Kamar",lamaBaru)
                                    print(f"\nJumlah yang harus dibayar sebesar: {nilaiBayar}\n")
                                    UangBayar = int(input("Masukkan Jumlah Uang Anda :")) 
                                    Kembalian = UangBayar - nilaiBayar
                                    if Kembalian < 0:
                                        Kembalian = Kembalian * -1
                                        print(f"\nTransaksi anda BATAL, kekurangan uang sebesar {Kembalian}")
                                    elif Kembalian == 0:
                                        print("\nUang anda pas \nTERIMAKASIH TELAH BERGABUNG BERSAMA D\'RESIDENCE MINANGKABAU\n")
                                        break
                                    else:
                                        print(f"\nKembalian anda sebesar {Kembalian} \nTERIMAKASIH TELAH BERGABUNG BERSAMA D\'RESIDENCE MINANGKABAU\n")
                                        break
                            elif subMenuInput2 == "N":
                                break
                            keluar()
                            break
                        except:
                            print("Masukkan inputan yang benar.")
                            continue
                break
        elif menuInput == 5:
            for i in pilihanMenu["SubMenu3"]:
                print(f"{i}. {pilihanMenu["SubMenu3"][i]}")
            while True:
                subMenuInput3 = int(input("Masukkan menu yang ingin diakses: "))
                if subMenuInput3 == 1:
                    while True:
                        try:
                            KamarIsi()
                            nomorGanti = int(input("Masukkan nomor kamar yang ingin diedit: "))
                            namaGanti = input("Masukkan nama baru: ")
                            IDGanti = cekID(nomorGanti,"Nomor Kamar")
                            DataPelanggan[IDGanti]["Nama"] = namaGanti
                            KamarIsi()
                            keluar()
                            break
                        except:
                            print("Masukkan inputan yang benar.")
                            continue
                if subMenuInput3 == 2:
                    while True:
                        try:
                            KamarIsi()
                            nomorPindah = int(input("Masukkan nomor kamar yang ingin pindah: "))
                            IDPd = cekID(nomorPindah,"Nomor Kamar")
                            if DataPelanggan[IDPd]["Tipe Kamar"] == "Kamar Bronze":
                                tipePindah = "Kamar Gold"
                                print("\n Anda akan dipindahkan ke tipe Kamar Gold")
                            elif DataPelanggan[IDPd]["Tipe Kamar"] == "Kamar Gold":
                                tipePindah = "Kamar Bronze"
                                print("\n Anda akan dipindahkan ke tipe Kamar Bronze")
                            durPindah = int(input("Masukkan durasi sewa: "))
                            J = pindah(nomorPindah, durPindah, tipePindah)
                            subMenuInput2 = input("Lanjutkan ke Pembayaran? (Y/N): ").upper()
                            if subMenuInput2 == "Y":    
                                while True:
                                    print(f"\nJumlah yang harus dibayar sebesar: {J}\n")
                                    UangBayar = int(input("Masukkan Jumlah Uang Anda :")) 
                                    Kembalian = UangBayar - J
                                    if Kembalian < 0:
                                        Kembalian = Kembalian * -1
                                        print(f"\nTransaksi anda BATAL, kekurangan uang sebesar {Kembalian}")
                                    elif Kembalian == 0:
                                        print("\nUang anda pas \nSELAMAT MENIKMATI KAMAR BARU ANDA\n")
                                        break
                                    else:
                                        print(f"\nKembalian anda sebesar {Kembalian} \nSELAMAT MENIKMATI KAMAR BARU ANDA\n")
                                        break
                            elif subMenuInput2 == "N":
                                break
                            keluar()
                            break
                        except:
                            print("Masukkan inputan yang benar.")
                            continue
                    break 
                break   
        elif menuInput == 0:
            clearScreenView()
            print("TERIMAKASIH TELAH MENGUNJUNGI KOSAN D\'RESIDENCE MINANGKABAU\n")
            break                                                      
    except:
        print("JANGAN MAIN MAIN")
        continue



