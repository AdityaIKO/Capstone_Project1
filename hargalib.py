from tabulate import tabulate

daftarMobilHarga = {
    'Nissan1': [1,'Nissan','March', 'Automatic', 'Bensin', 2011, 95000000],
    'Toyota1': [2, 'Toyota', 'Kijang', 'Manual', 'Bensin', 2002, 75000000],
    'Mazda1': [3, 'Mazda', '3', 'Automatic', 'Bensin', '2019', 310000000],
    'Honda1': [4, 'Honda', 'HRV', 'Automatic', 'Bensin', 2019, 255000000],
    'Toyota2': [5, 'Toyota', 'Innova Venturer', 'Manual', 'Bensin', 2019, 320000000],
    'Honda2': [6, 'Honda', 'BRV', 'Automatic', 'Bensin', 2022, 275000000],
    'Suzuki1': [7, 'Suzuki', 'Karimun', 'Manual', 'Bensin', 2016, 97000000],
    'Nissan2': [8, 'Nissan', 'Grand Livina', 'Automatic', 'Bensin', 2011, 100000000],
    'Nissan3': [9, 'Nissan', 'X-Trail', 'Automatic', 'Bensin', 2015, 215000000],
    'Chevrolet1': [10, 'Chevrolet', 'Orlando', 'Automatic', 'Bensin', 2015, 140000000],
    'Mitsubishi1': [11, 'Mitsubishi', 'Xpander', 'Automatic', 'Bensin', 2022, 288000000],
    'Toyota3': [12, 'Toyota', 'Innova Venturer', 'Automatic', 'Diesel', 2020, 475000000],
    'BMW1': [13, 'BMW', 'X1', 'Automatic', 'Bensin', 2019, 436000000],
    'Mitsubishi2': [14, 'Mitsubishi', 'Pajero Sport', 'Automatic', 'Diesel', 2022, 568000000],
    'Suzuki2': [15, 'Suzuki', 'Ertiga', 'Manual', 'Diesel', 2016, 140000000],
    'Toyota4': [16, 'Toyota', 'Hilux', 'Automatic', 'Diesel', 2023, 449000000],
    'Wuling1': [17, 'Wuling', 'AirEV', 'Automatic', 'Electric', 2022, 240000000],
    'Mercedes1': [18, 'Mercedes-Benz', 'GLA', 'Automatic', 'Bensin', 2016, 435000000],
    'Mercedes2': [19, 'Mercedes-Benz', 'C', 'Automatic', 'Bensin', 2015, 380000000],
    'Ford1': [20, 'Ford', 'EcoSport', 'Automatic', 'Bensin', 2014, 105000000],
    }
    
priceSorted = dict(sorted(daftarMobilHarga.items(), key=lambda x: (x[1][-1])))
print(priceSorted)

# priceSorted = dict(sorted(daftarMobilHarga.items(), key = lambda item: item[-1]))   
# print(priceSorted)

def showHarga(database, header = ['No', 'Merek', 'Model', 'Transmisi', 'Bahan Bakar', 'Tahun', 'Harga']):
        print(tabulate(database.values(), headers = header, tablefmt = 'grid'))

# print(priceSorted)
    
# marklist = sorted((value, key) for (key, value) in daftarMobilHarga.items())
# sortdict = dict([(k, [6]) for v, k in marklist])
# print(sortdict)
# priceSorted = dict(sorted(daftarMobilHarga.items(), key=lambda x: (x[1]['Harga'])))
# print(priceSorted)

# priceSorted = dict(sorted(daftarMobilHarga.items(), key = lambda item: item[-1]))
# print(priceSorted)