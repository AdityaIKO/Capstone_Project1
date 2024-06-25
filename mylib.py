from tabulate import tabulate
import random
import tabulate
import csv


PATH_DB_ADMIN = 'data_Admin.csv'
PATH_DB_LIST_USER = 'data_ListUser.csv'
PATH_DB_USER = 'data_User.csv'


HEADERS = ['ID', 'Merek', 'Model', 'Transmisi', 'Bahan Bakar', 'Tahun', 'Harga']

def stringValidation(title):
    """Fungsi untuk validasi tipe data string

    Args:
        title (String): Pesan yang akan ditampilkan pada layar

    Returns:
        String: Nilai yang diinputkan
    """
    while True:
        teks = input(title)
        if teks.isalpha() == True:
            break
        else:
            print('Silakan input hanya teks')
    return teks.capitalize()

def integerValidation(title, minval = 0, maxval = 3000):
    """Fungsi untuk validasi bilangan bulat

    Args:
        title (String): Pesan yang akan ditampilkan pada layar
        minval (int, optional): Nilai minimal. Defaults to 0.
        maxval (int, optional): Nilai maksimal. Defaults to 100.

    Returns:
        Int: Nilai yang diinputkan
    """
    while True:
        num = input(title)
        try:
            num = int(num)
            if num >= minval and num <= maxval:
                break
            else:
                print('Angka yang Anda masukkan di luar rentang.')
        except:
            print('Yang anda input bukan bilangan')
    return num



def printTable(database):
    print(tabulate.tabulate(database.values(), headers = HEADERS, tablefmt = 'grid'))


def show(db_admin, db_user):
    db_all = {}
    db_all_temp = {}
    db_all_temp.update(db_user)
    db_all.update(db_admin)
    db_all.update(db_all_temp)

    listPerintah = '''
    
    Silakan masukkan perintah yang Anda inginkan:

    1. Lihat Daftar Mobil Admin
    2. Lihat Daftar Mobil Collaborator
    3. Lihat Daftar Semua Mobil
    4. Urutkan Berdasarkan Harga
    5. Urutkan Berdasarkan Tahun
    6. Pilih Merek Yang Diinginkan
    7. Pilih Nama Mobil Yang Diinginkan
    8. Pilih Transmisi (Manual/Automatic)
    9. Pilih Bahan Bakar (Bensin/Diesel/Electric)
    10. Kembali Ke menu utama

    '''

    while True:
        print(listPerintah)
        option = input('Masukkan angka perintah yang ingin dijalankan: ')
        

        if option == '1':
            printTable(db_admin)
        elif option == '2':
            printTable(db_user)
        elif option == '3':
            printTable(db_all)
        elif option == '4':
            priceSorted = dict(sorted(db_all.items(), key = lambda item: item[1][6]))
            printTable(priceSorted)
        elif option == '5':
            yearSorted = dict(sorted(db_all.items(), key = lambda item: item[1][5]))
            printTable(yearSorted)
        elif option == '6':
            wantMerek = input('Tulis merek mobil: ').lower()
            def myFilterMerekWant(f):
                if f[1].lower() == wantMerek:
                    return True
                else:
                    return False
            if wantMerek == wantMerek:
                listWantMerek = list(filter(myFilterMerekWant, list(db_all.values())))
                print(tabulate.tabulate(listWantMerek,headers=HEADERS,tablefmt='grid'))
            else:
                break
        elif option == '7':
            wantNama = input('Tulis nama mobil: ').lower()
            def myFilterNamaWant(f):
                if f[2].lower() == wantNama:
                    return True
                else:
                    return False
            if wantNama == wantNama:
                listWantNama = list(filter(myFilterNamaWant, list(db_all.values())))
                print(tabulate.tabulate(listWantNama,headers=HEADERS,tablefmt='grid'))
            else:
                break
        elif option == '8':
            wantTransmisi = input('Tulis transmisi mobil: ').lower()
            def myFilterTransmisiWant(f):
                if f[3].lower() == wantTransmisi:
                    return True
                else:
                    return False
            if wantTransmisi == wantTransmisi:
                listWantTransmisi = list(filter(myFilterTransmisiWant, list(db_all.values())))
                print(tabulate.tabulate(listWantTransmisi,headers=HEADERS,tablefmt='grid'))
            else:
                break
        elif option == '9':
            wantFuel = input('Tulis bahan bakar: ').lower()
            def myFilterFuelWant(f):
                if f[4].lower() == wantFuel:
                    return True
                else:
                    return False
            if wantFuel == wantFuel:
                listWantFuel = list(filter(myFilterFuelWant, list(db_all.values())))
                print(tabulate.tabulate(listWantFuel,headers=HEADERS,tablefmt='grid'))
            else:
                break
        elif option == '10':
            break
        else:
            print('''
                  
        Gagal input nomor. Silakan masukkan nomor yang tersedia: 
                  
            ''')

def add(database):
    printTable(database)

    listPerintah2 = '''
    
    Silakan masukkan perintah yang Anda inginkan:

    1. Tambah Daftar Mobil
    2. Kembali Ke Menu Utama

    '''

    while True:
        print(listPerintah2)
        option = input('Masukkan angka perintah yang ingin dijalankan: ')

        if option == '1':
            while True:
                newValue = []

                for header in HEADERS :
                    if header == 'ID' :
                        pass
                    else :
                        insertData = input('Masukkan %s mobil baru: ' %(HEADERS[HEADERS.index(header)]))
                        newValue.insert(HEADERS.index(header), insertData)
                newValue.insert(0, (newValue[1][:2] + str(random.randint(10,90))).upper())
                print(tabulate.tabulate([newValue], tablefmt = 'grid', headers=HEADERS))
                confirmation = input('Apakah Anda yakin ingin menyimpan data ini? (y/n)')
                if confirmation == 'y':
                    database[len(database) + 1] = newValue
                else:
                    break
                printTable(database)
                break

        elif option == '2':
            break
        else:
            print('''
                  

            Mohon input angka yang sesuai.

                  
                  ''')
    

def delete(database):
    printTable(database)

    listPerintah3 = '''
    
    Silakan masukkan perintah yang Anda inginkan:

    1. Pilih Daftar Mobil Yang Ingin Anda Hapus
    2. Kembali Ke Menu Utama

    '''
    while True:
        print(listPerintah3)
        option = input('Masukkan angka perintah yang ingin dijalankan: ')

        if option == '1':
            hapusInt = input('Masukkan ID Mobil yang ingin dihapus: ')
            databaseTempo = {}
            if hapusInt in database.keys():
                databaseTempo[hapusInt]=database[hapusInt]
                printTable(databaseTempo)
                while True:
                    option = stringValidation(title = 'Apakah Anda yakin ingin mengubah data pada daftar mobil? (y/n) ').lower()
                    if option in ['no', 'n', 'tidak']:
                        print('Kembali ke menu awal.')
                        break
                    elif option in ['y', 'yes', 'ya', 'iya']:
                        del database[hapusInt]
                        break
                    else:
                        print('Mobil yang Anda cari tidak tersedia')
                        break

                printTable(database)
                print('''
                      
                      Data telah diperbarui

                      ''')

        elif option == '2':
            break
        else:
            print('''
                  

        Mohon input angka yang sesuai.

                  
                  ''')         

def update(database):
    printTable(database)

    listPerintah4 = '''
    
    Silakan masukkan perintah yang Anda inginkan:

    1. Perbarui Data Di Database
    2. Kembali Ke Menu Utama

    '''
    while True:
        print(listPerintah4)
        option = input('Masukkan angka perintah yang ingin dijalankan: ')

        if option == '1':
            databaseTemp = {}
            noUbah = input('Masukkan ID mobil yang ingin Anda ubah: ')
            if noUbah in database:
                databaseTemp[noUbah]=database[noUbah]
                printTable(databaseTemp)

                while True:
                    option = stringValidation(title = 'Apakah Anda yakin ingin mengubah data pada daftar mobil? (y/n) ').lower()

                    if option in ['no', 'n', 'tidak']:
                        print('Kembali ke menu awal.')
                        break

                    elif option in ['y', 'yes', 'ya', 'iya']:
                        while True:
                            for index in range(len(HEADERS)-1) :
                                idx = index
                                headers = HEADERS[1:][index]
                                print("%i) %s" %(idx+1, headers))
                            editColumn = integerValidation(title='Silakan masukan kolom yang ingin diubah: ')
                            if editColumn < len(HEADERS):    
                                database[noUbah][editColumn] = input('Masukkan data baru: ')
                            
                                printTable(database)
                                break
                            else:
                                print('''
                                      
                                Kolom tidak tersedia
                                      
                                      ''')
                                break
                        break
                    else:
                        print('''
                              
                    Mohon untuk input (y/n)
                              
                              ''')
                        break
            else:
                print('''
                      
        Mohon input daftar angka yang tersedia
                      
                      ''')
        
                    
        elif option == '2':
            break
        else:
            print('''
                  

        Mohon input angka yang sesuai.

                  
                  ''')