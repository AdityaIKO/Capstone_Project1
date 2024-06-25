import mylib
import tabulate
import csv

PATH_DB_ADMIN = 'data_Admin.csv'
PATH_DB_LIST_USER = 'data_ListUser.csv'
PATH_DB_USER = 'data_User.csv'


# Open the CSV file in read mode
def init_db():
    with open(PATH_DB_ADMIN, 'r') as csvfile_admin:
        # Create a reader object
        # reader = csv.DictReader(csvfile_admin)
        reader = csv.reader(csvfile_admin, delimiter=',')
        db_admin = {}
        # Iterate through the rows in the CSV file
        for row in reader:
            ID, merek, nama, transmisi, bahan_bakar, tahun, harga = row
            db_admin.update({str(ID): [str(ID), str(merek), str(nama), str(transmisi), str(bahan_bakar), int(tahun), int(harga)]})
    
    with open(PATH_DB_USER, 'r') as csvfile_user:
        # Create a reader object
        reader = csv.reader(csvfile_user, delimiter=',')
        db_user = {}
        # Iterate through the rows in the CSV file
        for row in reader:
        # Access each element in the row
            ID, merek, nama, transmisi, bahan_bakar, tahun, harga = row
            db_user.update({str(ID): [str(ID), str(merek), str(nama), str(transmisi), str(bahan_bakar), int(tahun), int(harga)]})
    
    with open(PATH_DB_USER, 'r') as csvfile_list_user:
        # Create a reader object
        reader = csv.reader(csvfile_list_user, delimiter=',')
        db_list_user = {}
        # Iterate through the rows in the CSV file
        for row in reader:
        # Access each element in the row
            ID, merek, nama, transmisi, bahan_bakar, tahun, harga = row
            db_list_user.update({str(ID): [str(ID), str(merek), str(nama), str(transmisi), str(bahan_bakar), int(tahun), int(harga)]})
    
    return db_admin,db_user,db_list_user

def main():
    global db_admin, db_user, db_list_user
    print('Selamat Datang di MoKu - MobilKu - Mobil dan Aku!')

    listMenu = '''
      
      Selamat Datang di MoKu - MobilKu - Mobil dan Aku!

      
      List Menu:
      1. Admin
      2. Kolaborator
      3. Pembeli
      4. Keluar

      '''
    
    while True:
        print(listMenu)
        option = input('Masukkan angka yang ingin dijalankan: ')

        if option == '1':
            print ("Selamat Datang di MoKu - MobilKu - Mobil dan Aku!")
            while True:
                passw = input("Please enter your Password: ")
                if passw == '123AbC':
                    print ('Selamat Datang di MoKu - MobilKu - Mobil dan Aku!')
                else:
                    print ('Masukkan password yang benar')
                print('Selamat Datang di MoKu - MobilKu - Mobil dan Aku!')

                listMenu = '''
                    
                    Selamat Datang di MoKu - MobilKu - Mobil dan Aku!

                    
                    List Menu:
                    1. Lihat Daftar Mobil
                    2. Tambah Daftar Mobil
                    3. Hapus Daftar Mobil
                    4. Perbarui Daftar Mobil
                    5. Keluar
                    '''

                while True:
                    print(listMenu)
                    option = input('Masukkan angka yang ingin dijalankan: ')

                    if option == '1':
                        mylib.show(db_admin, db_user)
                    elif option == '2':
                        mylib.add(db_admin)
                    elif option == '3':
                        mylib.delete(db_admin)
                    elif option == '4':
                        mylib.update(db_admin)
                    elif option == '5':
                        break


        elif option == '2':
            while True:
                    passw = input("Please enter your Password: ")
                    if passw == '123AbC':
                        print ('Welcome to hospital database')
                    else:
                        print ('Please Input the right password')
                    print('Selamat Datang di MoKu - MobilKu - Mobil dan Aku!')

                    listMenu = '''
                    
                    Selamat Datang di MoKu - MobilKu - Mobil dan Aku!

                    
                    List Menu:
                    1. Lihat Daftar Mobil
                    2. Tambah Daftar Mobil
                    3. Hapus Daftar Mobil
                    4. Perbarui Daftar Mobil
                    5. Keluar
                    '''

                    while True:
                        print(listMenu)
                        option = input('Masukkan angka yang ingin dijalankan: ')

                        if option == '1':
                            mylib.show(db_admin, db_user)
                        elif option == '2':
                            mylib.add(db_user)
                        elif option == '3':
                            mylib.delete(db_user)
                        elif option == '4':
                            mylib.update(db_user)
                        elif option == '5':
                            break


        elif option == '3':
            print('Selamat Datang di MoKu - MobilKu - Mobil dan Aku!')

            listMenu = '''
                    
            Selamat Datang di MoKu - MobilKu - Mobil dan Aku!

                    
                List Menu:
                1. Lihat Daftar Mobil
                2. Keluar

                '''
            while True:
                print(listMenu)
                option = input('Masukkan angka yang ingin dijalankan: ')
                if option == '1':
                    mylib.show(db_admin, db_user)
                elif option == '2':
                    break


        elif option == '4':
            break
        
        with open(PATH_DB_ADMIN, 'w') as file_admin:
            # Creating 'writer' variable
            writer_admin = csv.writer(file_admin, delimiter=",")
            # Writing data into csv file
            writer_admin.writerows(db_admin.values())
        
        with open(PATH_DB_USER, 'w') as file_user:
            # Creating 'writer' variable
            writer_user = csv.writer(file_user, delimiter=",")
            # Writing data into csv file
            writer_user.writerows(db_user.values())

db_admin, db_user, db_list_user = init_db()
main()

# def main():
#     global db_admin, db_user, db_list_user
#     print('Selamat Datang di MoKu - MobilKu - Mobil dan Aku!')

#     listMenu = '''
      
#       Selamat Datang di MoKu - MobilKu - Mobil dan Aku!

      
#       List Menu:
#       1. Lihat Daftar Mobil
#       2. Tambah Daftar Mobil
#       3. Hapus Daftar Mobil
#       4. Perbarui Daftar Mobil
#       5. Keluar
#       '''

#     while True:
#         print(listMenu)
#         option = input('Masukkan angka yang ingin dijalankan: ')

#         if option == '1':
#             mylib.show(db_admin, db_user)
#         elif option == '2':
#             mylib.add(db_admin)
#         elif option == '3':
#             mylib.delete(db_admin)
#         elif option == '4':
#             mylib.update(db_admin)
#         elif option == '5':
#             break
#         else:
#             print(input('Input Anda salah. Silakan input ulang!'))

#         with open(PATH_DB_ADMIN, 'w') as file_admin:
#             # Creating 'writer' variable
#             writer_admin = csv.writer(file_admin, delimiter=",")
#             # Writing data into csv file
#             writer_admin.writerows(db_admin.values())
        
#         with open(PATH_DB_USER, 'w') as file_user:
#             # Creating 'writer' variable
#             writer_user = csv.writer(file_user, delimiter=",")
#             # Writing data into csv file
#             writer_user.writerows(db_user.values())
        
#         with open(PATH_DB_LIST_USER, 'w') as file_list_user:
#             # Creating 'writer' variable
#             writer_list_user = csv.writer(file_list_user, delimiter=",")
#             # Writing data into csv file
#             writer_list_user.writerows(db_list_user.values())


# db_admin, db_user, db_list_user = init_db()
# main()
