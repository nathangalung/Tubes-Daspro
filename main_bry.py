import spesifikasi_bry
import function_bry



# deklarasi variabel

def command ():

    # F08 batchkumpul
    cmd = input(">>> ")
    if cmd == ">>> batchkumpul":
        if login == 1:
            spesifikasi_bry.batchkumpul(jumlah)
            command ()
        elif login == 0:
            print("Anda belum login, silahkan login terlebih dahulu sebelum memberikan arahan")
            command ()
        else:
            print("Anda tidak dapat memeberikan arahan ini, silahkan login sebagai bandung_bondowoso terkebih dahulu")
            command ()
    # F08 batchbangun
    elif cmd == ">>> batchbangun":
        if login == 1:
            spesifikasi_bry.batchbangun(jumlah, id, pembuat, pasir, batu, air)
            command ()
        elif login == 0:
            print("Anda belum login, silahkan login terlebih dahulu sebelum memberikan arahan")
            command ()
        else:
            print("Anda tidak dapat memeberikan arahan ini, silahkan login sebagai bandung_bondowoso terkebih dahulu")
            command ()

    # F09 laporanjin
    elif cmd == ">>> laporanjin":
        if login == 1:
            spesifikasi_bry.laporanjin(pembuat, jumlah)
            command ()
        elif login == 0:
            print("Anda belum login, silahkan login terlebih dahulu sebelum memberikan arahan")
            command ()
        else:
            print("Anda tidak dapat memeberikan arahan ini, silahkan login sebagai bandung_bondowoso terkebih dahulu")
            command ()

    # F10 laporancandi
    elif cmd == ">>> laporancandi":
        if login == 1:
            spesifikasi_bry.laporancandi(pasir, batu, air)
            command ()
        elif login == 0:
            print("Anda belum login, silahkan login terlebih dahulu sebelum memberikan arahan")
            command ()
        else:
            print("Anda tidak dapat memeberikan arahan ini, silahkan login sebagai bandung_bondowoso terkebih dahulu")
            command ()

    # F11 hancurkancandi
    elif cmd == ">>> hancurkancandi":
        if login == 2:
            spesifikasi_bry.hancurkancandi(id, jumlah_pembuat)
            command ()
        elif login == 0:
            print("Anda belum login, silahkan login terlebih dahulu sebelum memberikan arahan")
            command ()
        else:
            print("Anda tidak dapat memeberikan arahan ini, silahkan login sebagai 'roro_jonggrang' terkebih dahulu")
            command ()

username = [] # array file csv candi kolom username
password = [] # array file csv user kolom password
role = [] # array file csv user kolom role
id = [] # array file csv candi kolom id
pembuat = [] # array file csv candi kolom pembuat
pasir = [] # array file csv candi kolom pasir
batu = [] # array file csv candi kolom batu
air = [] # array file csv candi kolom air
nama = [] # array file csv bahan_bangunan
jumlah = [] # array file csv candi kolom jumlah
login = [0, 1, 2, 3, 4] # array jenis login, 0 = belum login, 1 = bondowoso, 2 = roro, 3 = jin pengumpul, 4 = jin pembangun

arr_jin_pembangun = function_bry.arr_target("jin_pembangun", username, role)
jumlah_jin_pengumpul = function_bry.jumlah_target ("jin_pengumpul", role)
jumlah_jin_pembangun = function_bry.jumlah_target ("jin_pengumpul", role)
jumlah_pembuat = function_bry.jumlah_column(pembuat)
jumlah_id = function_bry.jumlah_column(id)