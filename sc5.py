print("======= SISTEM PEMESANAN HOTEL =======")
print("=    Jenis kamar yang tersedia :     =")
print("=    1. Standard                     =")
print("=    2. Deluxe                       =")
print("======================================")

def biaya_pemesanan (jenis_kamar,durasi_menginap) : 
    if jenis_kamar.lower() == "standard" or jenis_kamar.lower() == "1" : 
        tarif = 200000
    elif jenis_kamar.lower() == "deluxe" or jenis_kamar.lower() == "2" : 
        tarif = 350000
    else : 
        print("Tidak Valid, silahkan pilih ulang")
        tarif = 0 

    return tarif * durasi_menginap

jenis_kamar = input ("Pilih jenis kamar (1/2): ")
checkin = int (input("Masukkan tanggal check in : "))
bulani = input("Masukkan Bulan check in : ")
tahuni = input("Masukkan Tahun check in : ")
checkout = int (input("Masukkan tanggal check out : "))
bulano = input("Masukkan Bulan check out : ")
tahuno = input("Masukkan Tahun check out : ")

durasi_menginap = checkout - checkin 
total = biaya_pemesanan (jenis_kamar,durasi_menginap)

print("============================================")
print("=             DATA PESANAN ANDA            =")
print("= Jenis kamar : ", jenis_kamar,"                        =")
print("= Check in :", checkin,bulani,tahuni,"            =")
print("= Check out :", checkout,bulano,tahuno,"           =")
print("= Durasi menginap : ", durasi_menginap,"                    =")
print("= Total Biaya Pemesanan Hotel : ", total,"   =")
print("============================================")