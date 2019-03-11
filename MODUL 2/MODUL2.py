============================================== NOMER 1 ==============================================
class Pesan (object):
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumlahKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimat mempunyai', len(self.teks), 'karakter')
    def perbarui(self, stringBaru):
        self.teks = stringBaru
============================================== NOMER 1 A ==============================================
    def apakahTerkandung(self,huruf):
        if huruf in self.teks():
            return True
        else:
            return False
============================================== NOMER 1 B ==============================================
    def hitungKonsonan(self):
        konson = "bcdfghjklmnpqrstvwxyzBCDFGHKLMNPQRSTVWXYZ"
        jumlah = 0
        for ii in self.teks:
            if ii in konson:
                jumlah += 1
        return jumlah
============================================== NOMER 1 C ==============================================
    def hitungVokal(self):
        vokal = "aiueAIUEO"
        jumlah = 0
        for ii in self.teks:
            if ii in vokal:
                jumlah += 1
        return jumlah
============================================== NOMER 2 ==============================================
class Manusia(object):
    """class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self, s):
        print("Saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya baru saja latihan ", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n * 2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku

    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            +". "+ self.uangSaku +' tiap bulannya.'
        return s
============================================== NOMER 2 A ==============================================
    def ambilKotaTinggal(self):
        return self.kotaTinggal

============================================== NOMER 2 B ==============================================
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal = ubah
============================================== NOMER 2 C ==============================================
    def tambahUangSaku(self, e):
        self.uangSaku += e
        return self.uangSaku

============================================== NOMER 4  ==============================================
    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)
============================================== NOMER 5 ==============================================
    def hapusKuliah(self, hapuslah):
        self.listKuliah.remove(hapuslah)

============================================== NOMER 3 ==============================================
print("\nNomer 3")
print("Silahkan Masukkan Data Mahasiswa Di bawah Ini :")
a = input("Nama Mahasiswa      : ")
b = input("NIM Mahasiswa       : ")
c = input("Asal Mahasiswa      : ")
d = input("Uang Saku Mahasiswa : ")
ma = Mahasiswa(a, b, c, d)
print(str(ma))

============================================== NOMER 6 ==============================================
class SiswaSMA(Manusia):
    def __init__(self, nama, NIS, uangMain, alamat):
        self.nama = nama
        self.nis = NIS
        self.uangMain = uangMain
        self.alamat = alamat
    def __str__(self):
        s = "Nama : " + str(self.nama) \
            + "NIS : " + str(self.nis) \
            + "Alamat : " + str(self.alamat)\
            + "Uang Main : " + str(self.uangMain)
        return s

============================================== NOMER 7 ==============================================
# Metoode atau state yang muncul berasal dari semua class baik Manusia, Mahasiswa, atau MhsTIF.
# Ini karena MhsTIF yang merupakan anak class dari Mahasiswa, dan itu membuat MhsTIF mewarisi
# semua properties dari Mahasiswa dan Manusia.
