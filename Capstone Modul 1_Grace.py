from colorama import Fore, Style, init
from prettytable import PrettyTable
# Database ID Login
user_db = {
    'Admin' : { 'password' : 'admin123', 'role' : 'admin'} ,
    'TeacherJCDS' : { 'password' : 'teacher123' , 'role' : 'teacher'} ,
}

# dictionary dummy data siswa
siswa_db = {
    '20241001' : { 'namaSiswa':'Charlie Puth', 'kelas':'JCDS100', 'alamat': 'Perum 3 ',
                  'tugas':0, 'kuis':0, 'uts':0, 'uas':0 },

    '20241002' : { 'namaSiswa':'Shawn Mendes', 'kelas':'JCDS100', 'alamat': 'Komplek Palem Raya',
                  'tugas':0, 'kuis':0, 'uts':0, 'uas':0 },

    '20241003' : { 'namaSiswa':'Bernadya Ribka', 'kelas':'JCDS100', 'alamat': 'Pesona Atlantis',
                  'tugas':0, 'kuis':0, 'uts':0, 'uas':0},

    '20241004' : { 'namaSiswa':'Taylor Swift', 'kelas':'JCDS100', 'alamat': 'Serdang Asri 1',
                  'tugas':0, 'kuis':0, 'uts':0, 'uas':0 },
}

# fungsi Auto Increment ID
def auto_idSiswa ():
    prefix = '20241'
    idSiswa_auto = [int(key) for key in siswa_db.keys() if key.startswith(prefix)]

    if idSiswa_auto:
        max_id = max(idSiswa_auto)
        new_id = max_id + 1
    else:
        new_id = int(prefix + '001')
    return str(new_id)

# Menu Awal Pilihan Login
def pilih_login():
    print('''
    ======================================
        Pilih Login:
        1. Admin
        2. Teacher
        3. Siswa
        0. Keluar
    ======================================
    ''')

# Menu Login
def login_AdminTeacher(username, password):
    for user, data in user_db.items():
        if user == username and data['password'] == password:
            print(Fore.GREEN + f'\nLogin berhasil!' + Style.RESET_ALL)
            return True, data['role']
        continue

    print(Fore.RED + '\nLogin gagal! Username atau Password salah.' + Style.RESET_ALL)
    return False, None

# Menu untuk siswa menggunakan ID    
def login_Siswa():
    id_siswa = input('\nMasukkan ID Siswa: ')
   
    if id_siswa in siswa_db:
        print(Fore.GREEN + f'\nLogin berhasil! Selamat datang, {siswa_db[id_siswa]['namaSiswa']}.' + Style.RESET_ALL)
        return id_siswa
    else:
        print(Fore.RED + '\nID Siswa tidak ditemukan.' + Style.RESET_ALL)
        return None

# Menu Utama Admin dan Teacher  
def admin_menu(username):
    print(f'''\n** Hi, {username}! Welcome to Dashboard. *
          
        List Menu Admin:
            1. List Daftar Siswa
            2. Input Data Siswa
            3. Hapus Data Siswa
            4. Edit Data Siswa
            0. Menu Awal '''
        )

def teacher_menu(username):
    print(f'''\n** Hi, {username}! Welcome to Dashboard. **
          
        List Menu Teacher:
            1. List Data Nilai
            2. Input Nilai
            3. Edit Nilai
            0. Menu Awal '''
        )
    
# Report Nilai Siswa
def siswa_menu(idSiswa):
    data_siswa = siswa_db[idSiswa]
    print("\n** Data Siswa **")
    print(f"ID: {idSiswa}")
    print(f"Nama: {data_siswa['namaSiswa']}")
    print(f"Kelas: {data_siswa['kelas']}")
    print(f"Alamat: {data_siswa['alamat']}")
      
    print(f'''
    ============================================
        Laporan Hasil Belajar {data_siswa['namaSiswa']}
    ============================================
          Nilai Tugas: {data_siswa['tugas']}
          Nilai Kuis: {data_siswa['kuis']}
          Nilai UTS: {data_siswa['uts']}
          Nilai UAS: {data_siswa['uas']}
        ''')

    # Hitung nilai akhir dan keterangan lulus
    nilai_akhir = (data_siswa['tugas'] + data_siswa['kuis'] 
                   + data_siswa['uts'] + data_siswa['uas']) / 4
    keterangan = 'Lulus' if nilai_akhir >= 85 else 'Tidak Lulus'
    
    print(f'''\t  Nilai Akhir: {nilai_akhir}''')
    print(f'''\t  Keterangan: {keterangan}''')

# Menampilkan Data Siswa
def listDataSiswa():
    table_listDataSiswa = PrettyTable()
    table_listDataSiswa.field_names = ['ID Siswa', 'Nama', 'Kelas', 'Alamat']
    for key, value in siswa_db.items():
        table_listDataSiswa.add_row([key, value['namaSiswa'], value['kelas'],
                                     value['alamat']])
    print('\nList Data Siswa')
    print(table_listDataSiswa)

# Menampilkan Nilai Siswa
def listDataNilai():
    table_listDataNilai = PrettyTable()
    table_listDataNilai.field_names = ['ID Siswa', 'Nama', 'Kelas', 'Tugas', 'Kuis', 'UTS', 'UAS']
    for key, value in siswa_db.items():
        table_listDataNilai.add_row([key, value['namaSiswa'], value['kelas'],
                                    value['tugas'], value['kuis'], value['uts'], value['uas']])
    print('\nList Data Nilai')
    print(table_listDataNilai)

# Input Siswa Baru
def inputDataSiswa():
    print('\n**************************')
    print('Input Siswa Baru\n')
    namaSiswa = input('Nama Siswa: ').title()
    kelas = input('Kelas (JCDS100): ').upper()
    alamat = input('Alamat: ').title()

    key = auto_idSiswa()

    if not key:
        return
    
    siswa_db[key] = {
        'namaSiswa': namaSiswa,
        'kelas': kelas,
        'alamat': alamat,
        'tugas': 0,
        'kuis': 0,
        'uts': 0,
        'uas': 0
    }
    print(Fore.GREEN + f'\nData siswa berhasil ditambahkan dengan ID: {key}.' + Style.RESET_ALL)
    lanjut = input('Ingin melanjutkan input (Yes/No)? ').strip().lower()
    if lanjut == 'yes':
        return inputDataSiswa()
    else:
        return()
    

# Input Nilai Siswa
def inputNilai():
    listDataSiswa()
    key = input('\t\nMasukkan ID siswa: ').strip()
    if key in siswa_db:
        if siswa_db[key]['tugas'] != 0 or siswa_db[key]['kuis'] != 0 or siswa_db[key]['uts'] != 0 or siswa_db[key]['uas'] != 0:
            print(Fore.RED + '\n\t\t\tNilai untuk siswa ini sudah diinput.' + Style.RESET_ALL)
            print(Fore.RED + '\t\tSilakan gunakan menu "Edit Nilai" untuk mengubah nilai.' + Style.RESET_ALL)
        else:
            while True:
                try:
                    tugas = int(input('Nilai Tugas: '))
                    kuis = int(input('Nilai Kuis: '))
                    uts = int(input('Nilai UTS: '))
                    uas = int(input('Nilai UAS: '))
                    
                    # Validasi rentang nilai
                    if not (0 <= tugas <= 100):
                        print(Fore.RED + 'Nilai Tugas harus berada dalam rentang 0 - 100!' + Style.RESET_ALL)
                        continue
                    if not (0 <= kuis <= 100):
                        print(Fore.RED + 'Nilai Kuis harus berada dalam rentang 0 - 100!' + Style.RESET_ALL)
                        continue
                    if not (0 <= uts <= 100):
                        print(Fore.RED + 'Nilai UTS harus berada dalam rentang 0 - 100!' + Style.RESET_ALL)
                        continue
                    if not (0 <= uas <= 100):
                        print(Fore.RED + 'Nilai UAS harus berada dalam rentang 0 - 100!' + Style.RESET_ALL)
                        continue

                    # Jika semua nilai valid, update database          
                    siswa_db[key]['tugas'] = tugas
                    siswa_db[key]['kuis'] = kuis
                    siswa_db[key]['uts'] = uts
                    siswa_db[key]['uas'] = uas
                    print(Fore.GREEN + '\tNilai siswa berhasil diperbarui.' + Style.RESET_ALL)
                    return
                    
                except ValueError:
                    print(Fore.RED + 'Input Nilai harus berada dalam rentang 0 - 100!' + Style.RESET_ALL)
    else:
        print(Fore.RED + '\nID siswa tidak ditemukan.' + Style.RESET_ALL)

# Hapus Data Siswa                
def hapusDataSiswa():
    listDataSiswa()
    key = input('\nMasukkan ID siswa yang ingin dihapus: ').strip()

    if key in siswa_db:
        konfirmasihapus = input(Fore.BLUE + 'Anda yakin ingin menghapus data siswa ini (Yes/No)?  ' + Style.RESET_ALL).lower()
        if konfirmasihapus == 'yes':

            for id_siswa in list(siswa_db.keys()):
                if id_siswa == key:
                    del siswa_db[id_siswa]
                    print(Fore.GREEN + '\nData siswa berhasil dihapus.' + Style.RESET_ALL)
                    break
            else:
                print(Fore.RED + '\nID siswa tidak ditemukan.' + Style.RESET_ALL)
        else:
            print(Fore.RED + '\nPenghapusan data dibatalkan.' + Style.RESET_ALL)
    else:
        print(Fore.RED + '\nID Siswa tidak ditemukan.' + Style.RESET_ALL)

# Edit Data Siswa
def editDataSiswa():
    listDataSiswa()  # Menampilkan daftar siswa
    idSiswa = input('\nMasukkan ID siswa yang ingin diedit: ').strip()

    if idSiswa in siswa_db:
        print(f'\nMengedit data untuk siswa dengan ID: {idSiswa}')
        dataSiswa = siswa_db[idSiswa]
        print('*Tekan Enter jika tidak ingin mengubah.\n')

        namabaru = input(f'Nama Siswa [{dataSiswa["namaSiswa"]}]: ').strip()
        kelasbaru = input(f'Kelas [{dataSiswa["kelas"]}]: ').strip()
        alamatbaru = input(f'Alamat [{dataSiswa["alamat"]}]: ').strip()

        # Perbarui hanya jika ada input baru, jika tidak tetap gunakan data lama
        if namabaru:
            dataSiswa['namaSiswa'] = namabaru
        if kelasbaru:
            dataSiswa['kelas'] = kelasbaru
        if alamatbaru:
            dataSiswa['alamat'] = alamatbaru

        print(Fore.GREEN + '\nData siswa berhasil diperbarui.' + Style.RESET_ALL)
    else:
        print(Fore.RED + 'ID siswa tidak ditemukan.' + Style.RESET_ALL)

# Edit Nilai Siswa
def editNilaiSiswa():
    listDataNilai()
    id_siswa_input = input('\nMasukkan ID siswa yang ingin diedit: ').strip()

    if id_siswa_input in siswa_db:
        print(f'''\nMengedit data untuk siswa dengan ID: {id_siswa_input}''')
        dataNilai = siswa_db[id_siswa_input]
        print('*Tekan Enter jika tidak ingin mengubah.\n')

        # Fungsi untuk validasi nilai
        def validasiNilai(nilai_lama, label):
            while True:
                nilai_baru = input(f'{label} [{nilai_lama}]: ').strip()
                if nilai_baru == "":  # Tekan Enter untuk mempertahankan nilai lama
                    return nilai_lama
                if nilai_baru.isdigit() and 0 <= int(nilai_baru) <= 100:  # isdigit: Cek apakah angka valid
                    return int(nilai_baru)
                else:
                    print('Harap masukkan nilai berupa bilangan bulat antara 0 - 100.')

        # Ambil input nilai baru dengan validasi
        dataNilai['tugas'] = validasiNilai(dataNilai['tugas'], 'Nilai Tugas')
        dataNilai['kuis'] = validasiNilai(dataNilai['kuis'], 'Nilai Kuis')
        dataNilai['uts'] = validasiNilai(dataNilai['uts'], 'Nilai UTS')
        dataNilai['uas'] = validasiNilai(dataNilai['uas'], 'Nilai UAS')

        print(Fore.GREEN + '\nData siswa berhasil diperbarui.' + Style.RESET_ALL)
        return
    else:
        print(Fore.RED + 'ID siswa tidak ditemukan.' + Style.RESET_ALL)

# Main Menu
def back_to_main_menu():
    while True:
        pilih_login()
        action = input('Masukkan pilihan login anda: ').strip()

        if action == '1' or action == '2':
            username = input('\n\t Username: ')
            password = input('\t Password: ')
            success, role = login_AdminTeacher(username, password)
            if not success:
                action = input("\t>> Enter 'Exit to quit or press anywhere to retry: ").strip()
                if action.lower() == 'exit' :
                    print('Exiting Program.')
                    break
                continue

            while True :
                if role == 'admin' and action == '1' :
                    admin_menu(username)
                    choice = input('\nPilih Menu: ').strip()

                    if choice == '1':
                        listDataSiswa()
                    elif choice == '2':
                        inputDataSiswa()
                    elif choice == '3':
                        hapusDataSiswa()
                    elif choice == '4':
                        editDataSiswa()
                    elif choice == '0':
                        break
                    else:
                        print(Fore.RED + 'Pilihan tidak valid.' + Style.RESET_ALL)

                elif role == 'teacher' and action == '2':
                    teacher_menu(username)
                    choice = input('\nPilih Menu: ').strip()

                    if choice == '1':
                        listDataNilai()
                    elif choice == '2':
                        inputNilai()
                    elif choice == '3':
                        editNilaiSiswa()
                    elif choice == '0':
                        break
                    else:
                        print(Fore.RED + 'Pilihan tidak valid.' + Style.RESET_ALL)

        elif action == '3':
            idSiswa = login_Siswa()
            if idSiswa:
                siswa_menu(idSiswa)
                choice = input("\n>>>Tekan Enter untuk kembali atau 'Exit' untuk keluar.  ")
                if choice.lower() == 'exit':
                    print('Exiting Program.')
                    return
            else:
                print(Fore.RED + 'Login siswa gagal, coba lagi.' + Style.RESET_ALL)
        elif action == '0':
            print('Exiting Program.')
            return
        else:
            print(Fore.RED + 'Pilihan tidak valid.' + Style.RESET_ALL)

if __name__ == '__main__' :
    back_to_main_menu()
