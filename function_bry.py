from main_bry import *

def jumlah_target (target, column) -> int: # menghitung jumlah variabel dari 1 kolom seperti "jin_pembangun" dari kolom role
    jumlah_variabel = 0
    for i in range(100):
        if column[i] == target:
            jumlah_variabel += 1
    return jumlah_variabel

def jumlah_column (column) -> int: # menghitung jumlah kolom yang terisi, selain None dan 0
    jumlah_data = 0
    for i in range(100):
        if column[i] != None and column[i] != 0:
            jumlah_data += 1
    return jumlah_data

def arr_target (target, column1, column2) -> list: # membuat suatu array yang berisi target dari 2 kolom,
    # contoh seperti array baru dari kolom role sebagain "jin_pembangun" yang berupa nama namanya dari kolom "username"
    arr_target = [None for i in range(jumlah_target (target, column2))]
    j = 0
    for i in range(100):
        if column2[i] == target:
            arr_target[j] = column1[i]
            j += 1
    return arr_target