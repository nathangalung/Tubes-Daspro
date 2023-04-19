from main_bry import *
import random

"""
Kamus:
jumlah_jin_pengumpul: int -> jumlah jin pengumpul yang ada
jumlah_jin_pembangun: int -> jumlah jin pembangun yang ada
total_pasir_kumpul: int -> total pasir yang dikumpulkan jin pengumpul dalam satu command
total_batu_kumpul: int -> total batu yang dikumpulkan jin pengumpul dalam satu command
total_air_kumpul: int -> total air yang dikumpulkan jin pengumpul dalam satu command
total_pasir_bangun: int -> total pasir yang digunakan untuk membangun semua candi dalam satu command
total_batu_bangun: int -> total batu yang digunakan untuk membangun semua candi dalam satu command
total_air_bangun: int -> total air yang digunakan untuk membangun semua candi dalam satu command
kurang_pasir: int -> jumlah pasir yang kurang untuk membangun semua candi dalam satu command
kurang_batu: int -> jumlah batu yang kurang untuk membangun semua candi dalam satu command
kurang_air: int -> jumlah air yang kurang untuk membangun semua candi dalam satu command
total_pasir_candi: int -> jumlah pasir yang digunakan untuk membangun semua candi
total_batu_candi: int -> jumlah batu yang digunakan untuk membangun semua candi
total_air_candi: int -> jumlah air yang digunakan untuk membangun semua candi
jin_termalas: str -> username jin yang membangun candi paling sedikit
jin_terajin: str -> username jin yang membangun candi paling banyak
candi_termurah: int -> harga candi yang dibangun termurah
candi_termahal: int -> harga candi yang dibangun termahal
id_hancur: int -> id candi yang akan dihancurkan
YN: str -> yes atau no untuk menghancurkan candi
"""

# F08 batchkumpul
def batchkumpul(jumlah):

    if jumlah_jin_pengumpul == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu")

    else:
        total_pasir_kumpul = 0
        total_batu_kumpul = 0
        total_air_kumpul = 0

        for i in range(jumlah_jin_pengumpul):
            total_pasir_kumpul  += random.randint(0, 5)
            total_batu_kumpul += random.randint(0, 5)
            total_air_kumpul += random.randint(0, 5)

        jumlah[0] += total_pasir_kumpul
        jumlah[1] += total_batu_kumpul
        jumlah[2] += total_air_kumpul

        print("Mengerahkan %d jin untuk mengumpulkan bahan." %jumlah_jin_pengumpul)
        print(f"Jin menemukan total {total_pasir_kumpul} pasir, {total_batu_kumpul} batu, dan {total_air_kumpul} air")

    return jumlah

# F08 batchbangun
def batchbangun(jumlah, id, pembuat, pasir, batu, air):
    
    if jumlah_jin_pembangun == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

    else:
        total_pasir_bangun = 0
        total_batu_bangun = 0
        total_air_bangun = 0

    
        for i in range(jumlah_jin_pembangun):
            for j in range(100):
                if pembuat[j] == None:
                    break
                
            id[j] = j
            pembuat[j] = random.choice(function.arr_target())
            pasir[j] = random.randint (1, 5)
            batu[j] = random.randint (1, 5)
            air[j] = random.randint (1, 5)
            total_pasir_bangun += pasir[j]
            total_batu_bangun += batu[j]
            total_air_bangun += air[j]

            if j == 99 and i != (jumlah_jin_pembangun - 1):
                break

        print(f"Mengerahkan {jumlah_jin_pembangun} jin untuk membangun candi dengan total bahan {jumlah[0]} pasir, {jumlah[1]} batu, dan {jumlah[2]} air.")
        
        if total_pasir_bangun > jumlah[0] or total_batu_bangun > jumlah[1] or total_air_bangun > jumlah[2]:
            kurang_pasir = total_pasir_bangun - jumlah[0]
            kurang_batu = total_batu_bangun - jumlah[1]
            kurang_air = total_air_bangun - jumlah[2]

            if kurang_pasir <= 0 and kurang_batu <= 0:
                print(f"Bangun gagal. Kurang {kurang_air} air.")

            elif kurang_batu <= 0 and kurang_air <= 0:
                    print(f"Bangun gagal. Kurang {kurang_pasir} pasir.")

            elif kurang_pasir <= 0 and kurang_air <= 0:
                print(f"Bangun gagal. Kurang {kurang_batu} batu.")

            elif kurang_pasir <= 0:
                print(f"Bangun gagal. Kurang {kurang_batu} batu dan {kurang_air} air.")

            elif kurang_batu <= 0:
                print(f"Bangun gagal. Kurang {kurang_pasir} pasir dan {kurang_air} air.")

            elif kurang_air <= 0:
                print(f"Bangun gagal. Kurang {kurang_pasir} pasir dan {kurang_batu} batu.")

            else:
                print(f"Bangun gagal. Kurang {kurang_pasir} pasir, {kurang_batu} batu, dan {kurang_air} air.")

            print(f"Sisa bahan bangunan sebanyak {jumlah[0]} pasir, {jumlah[1]} batu, dan {jumlah[2]} air.")

            for i in range(j, (j-jumlah_jin_pembangun), -1):
                id[i] = None
                pembuat[i] = None
                pasir[i] = 0
                batu[i] = 0
                air[i] = 0

        else:
            jumlah[0] -= total_pasir_bangun
            jumlah[1] -= total_batu_bangun
            jumlah[2] -= total_air_bangun

            print(f"Jin berhasil membangun total {jumlah_jin_pembangun} candi.")
            print(f"Sisa bahan bangunan sebanyak {jumlah[0]} pasir, {jumlah[1]} batu, dan {jumlah[2]} air.") # kreativitas

    return (jumlah, id, pasir, batu, air)

# F09 laporanjin
def laporanjin (pembuat, jumlah):

    check_terajin = 0
    check_termalas = 0

    for i in range(jumlah_jin_pembangun):
        x = 0
        y = 0

        for j in range(jumlah_pembuat):
            if arr_jin_pembangun[i] == pembuat[j]:
                x += 1
            else:
                y += 1

        if x > check_terajin:
            check_terajin = x
            jin_terajin = arr_jin_pembangun[i]

        elif x == check_terajin:
            if jin_terajin > arr_jin_pembangun[i]:
                jin_terajin = arr_jin_pembangun[i]

        elif y > check_termalas:
            check_termalas = y
            jin_termalas = arr_jin_pembangun[i]

        elif y == check_termalas:
            if jin_termalas < arr_jin_pembangun[i]:
                jin_termalas = arr_jin_pembangun[i]
        
    print("Total Jin: %d" %(jumlah_jin_pengumpul + jumlah_jin_pembangun))
    print("Total Jin Pengumpul: %d" %jumlah_jin_pengumpul)
    print("Total Jin Pembangun: %d" %jumlah_jin_pembangun)
    print("Jin Terajin: %s" %jin_terajin)
    print("Jin Termalas: %s" %jin_termalas)
    print("Jumlah Pasir: %d unit" %jumlah[0])
    print("Jumlah Air: %d unit" %jumlah[1])
    print("Jumlah Batu: %d unit" %jumlah[2])

    return (jin_termalas, jin_terajin)

# F10 laporancandi
def laporancandi (pasir, batu, air):

    total_pasir_candi = 0
    total_batu_candi = 0
    total_air_candi = 0

    for i in range(jumlah_pembuat):
        total_pasir_candi += pasir[i]
        total_pasir_candi += batu[i]
        total_pasir_candi += air[i]

    harga_candi = [0 for i in range(100)]
    for i in range (100):
        harga_candi[i] = (10000 * pasir[i]) + (15000 * batu[i]) + (7500 * air[i])
    
    candi_termahal = harga_candi[0]
    candi_termurah = harga_candi[0]

    for i in range(jumlah_pembuat):
        if harga_candi[i] >= candi_termahal:
            candi_termahal = harga_candi[i]
            id_candi_termahal = i
        if harga_candi[i] <= candi_termurah:
            candi_termurah = harga_candi[i]
            id_candi_termurah = i

    print("Total Candi: %d" %jumlah_pembuat)
    print("Jumlah Pasir: %d unit" %total_pasir_candi)
    print("Jumlah Batu: %d unit" %total_batu_candi)
    print("Jumlah Air: %d unit" %total_air_candi)
    print("ID Candi Termahal:", id_candi_termahal, "(%d)" %candi_termahal)
    print("ID Candi Termurah:", id_candi_termurah, "(%d)" %candi_termurah)

    return (candi_termurah, candi_termahal)

# F11 hancurkancandi
def hancurkancandi (id, jumlah_pembuat):

    id_hancur = int(input("Masukkan ID candi: "))
    check = 0

    for i in range(jumlah_pembuat):
        if id_hancur == id[i]:
            check += 1
        break

    if check > 0:
        YN = input("Apakh anda yakin ingin menghancurkan candi ID: %d (Y/N)? " %id_hancur)

        while YN != "Y" and "N":
            print("\nTidak ada pilihan tersebut.")
            YN = input("Apakh anda yakin ingin menghancurkan candi ID: %d (Y/N)? " %id_hancur)

        if YN == "Y":
            if i == jumlah_id - 1:
                id[i] = None

            else:
                for j in range((i+1), jumlah_id):
                    id[j-1] = id[j]
                id[jumlah_id - 1] = None
                print("\nCandi telah berhasil dihancurkan.")

        else :
            print("\nCandi tidak jadi dihancurkan.")

    else:
        print("\nTidak ada candi dengan ID tersebut.")
        hancurkancandi (id, jumlah_pembuat)

    return (id)

def YN_hancurkancandi (id_hancur, i):
    YN = input("Apakah anda yakin ingin menghancurkan candi ID: %d (Y/N)? " %id_hancur)

    if YN == "Y":
        if i == jumlah_id - 1:
            id[i] = None

        else:
            for j in range((i+1), jumlah_id):
                id[j-1] = id[j]
            id[jumlah_id - 1] = None
            print("\nCandi telah berhasil dihancurkan.")

    elif YN == "N":
        print("\nCandi tidak jadi dihancurkan.")
        
    else:
        print("\nTidak ada pilihan tersebut.")
        YN_hancurkancandi (id_hancur, i)

    return id