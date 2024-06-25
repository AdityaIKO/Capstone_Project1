from tabulate import tabulate
import mylib

daftarMobil = {
    1: [1,'Nissan','March', 'Automatic', 'Bensin', 2011, 95000000],
    2: [2, 'Toyota', 'Kijang', 'Manual', 'Bensin', 2002, 75000000],
    3: [3, 'Mazda', '3', 'Automatic', 'Bensin', 2019, 310000000],
    4: [4, 'Honda', 'HRV', 'Automatic', 'Bensin', 2019, 255000000],
    5: [5, 'Toyota', 'Innova Venturer', 'Manual', 'Bensin', 2019, 320000000],
    6: [6, 'Honda', 'BRV', 'Automatic', 'Bensin', 2022, 275000000],
    7: [7, 'Suzuki', 'Karimun', 'Manual', 'Bensin', 2016, 97000000],
    8: [8, 'Nissan', 'Grand Livina', 'Automatic', 'Bensin', 2011, 100000000],
    9: [9, 'Nissan', 'X-Trail', 'Automatic', 'Bensin', 2015, 215000000],
    10: [10, 'Chevrolet', 'Orlando', 'Automatic', 'Bensin', 2015, 140000000],
    11: [11, 'Mitsubishi', 'Xpander', 'Automatic', 'Bensin', 2022, 288000000],
    12: [12, 'Toyota', 'Innova Venturer', 'Automatic', 'Diesel', 2020, 475000000],
    13: [13, 'BMW', 'X1', 'Automatic', 'Bensin', 2019, 436000000],
    14: [14, 'Mitsubishi', 'Pajero Sport', 'Automatic', 'Diesel', 2022, 568000000],
    15: [15, 'Suzuki', 'Ertiga', 'Manual', 'Diesel', 2016, 140000000],
    16: [16, 'Toyota', 'Hilux', 'Automatic', 'Diesel', 2023, 449000000],
    17: [17, 'Wuling', 'AirEV', 'Automatic', 'Electric', 2022, 240000000],
    18: [18, 'Mercedes-Benz', 'GLA', 'Automatic', 'Bensin', 2016, 435000000],
    19: [19, 'Mercedes-Benz', 'C', 'Automatic', 'Bensin', 2015, 380000000],
    20: [20, 'Ford', 'EcoSport', 'Automatic', 'Bensin', 2014, 105000000],
    }

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
            print('Yang anda inputkan bukan bilangan')
    return num


def printTable(database, header = ['No', 'Merek', 'Model', 'Transmisi', 'Bahan Bakar', 'Tahun', 'Harga']):
    print(tabulate(database.values(), headers = header, tablefmt = 'grid'))

def add(database, header = ['No', 'Merek', 'Model', 'Transmisi', 'Bahan Bakar', 'Tahun', 'Harga']):
    print(tabulate(database.values(), headers = header, tablefmt = 'grid'))

    listPerintah2 = '''
    
    Silakan masukkan perintah yang Anda inginkan:

    1. Add a car to the list
    2. Back to main menu
    3. Add column

    '''

    while True:
        print(listPerintah2)
        option = input('Masukkan angka perintah yang ingin dijalankan: ')

        if option == '1':
            Merek = stringValidation('Silakan masukkan merek mobil: ')
            Model = stringValidation('Silakan masukkan model/nama mobil: ')
            Transmisi = stringValidation('Silakan pilih diantara Manual atau Automatic: ')
            BahanBakar = stringValidation('Silakan pilih diantara Bensin, Diesel, atau Electric: ')
            Tahun = integerValidation(
                title = 'Silakan tulis tahun mobil: ',
                minval = 0
            )
            Harga = integerValidation(
                title = 'Masukkan harga buah: ',
                minval = 0,
                maxval = 1000000000000
            )

            for key, No in database.copy().items():
                if Merek in No:
                    database[key] = [No[0], Merek, Model, Transmisi, BahanBakar, Tahun, Harga]
                    break
                else:
                    database[len(database)+1] = [(len(database) + 1), Merek, Model, Transmisi, BahanBakar, Tahun, Harga]
                    break

            printTable(database)

        elif option == '2':
            break

        elif option == '3':
            newCol = stringValidation('Silakan masukkan nama column baru: '),
            newColVal = stringValidation('Silakan masukkan nama column baru: '),
            database[newCol] = [len(database) + newColVal],
            printTable(database)
        else:
            print('''
                  

            Mohon input angka yang sesuai.

                  
                  ''')
            
    print(add)

