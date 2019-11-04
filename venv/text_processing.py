# Aplikasi Text Processing
import re, string
from operator import itemgetter
from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Inisialisasi
path_file = "test_text.txt"
file = open(path_file, "r")
kalimat = file.read()

kalimat_terformat = re.sub(r"\d+", "", kalimat).translate(str.maketrans("", "", string.punctuation)).lower().strip()

# Tokenizing
def Tokenizing(kalimat):
    tokens = word_tokenize(kalimat)
    return tokens

# Stopword
def StopWord(kalimat):
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    stop = stopword.remove(kalimat)
    tokens = word_tokenize(stop)
    return tokens

# Stemming
def Stemming(kalimat):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    tokens = stemmer.stem(kalimat)
    return tokens

def SimpanHasil(kalimat):
    hasil_teks = open("hasil.txt", "a+")
    hasil_teks.write("\n============= Tokenizing =============\n\'")
    hasil_teks.write('\',\''.join(Tokenizing(kalimat)))
    hasil_teks.write("\'\n============= Stopword =============\n")
    hasil_teks.write(' '.join(StopWord(kalimat)))
    hasil_teks.write("\n============= Stemming =============\n")
    hasil_teks.write(Stemming(kalimat))
    hasil_teks.write("\n============= Hasil Gabungan =============\n")
    hasil_teks.write(Stemming(kalimat))
    hasil_teks.close()
    print("Sudah di simpan")

# ZipfLaw
def ZipfLaw(kalimat):
    frequency = {}
    for word in kalimat:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    for key, value in reversed(sorted(frequency.items(), key = itemgetter(1))):
        return key, value

# Test
def TestMulti(kalimat):
        hasil = StopWord(kalimat)
        return hasil

# Menu
def menu():
    print("=========================================")
    print("[1] Tokenizing")
    print("[2] Stopword")
    print("[3] Stemming")
    print("[4] Simpan Hasil")
    # print("[5] Test Zipf's  Law")
    # print("[6] Gabungan")
    print("=========================================")
    print("[0] Keluar")

    menu = input("Pilih menu : ")

    try:
        num = int(menu)
        if num == 1:
            print("================= Hasil ================")
            print(Tokenizing(kalimat_terformat))
        elif num == 2:
            print("================= Hasil ================")
            print(StopWord(kalimat_terformat))
        elif num == 3:
            print("================= Hasil ================")
            print(Stemming(kalimat_terformat))
        elif num == 4:
            SimpanHasil(kalimat_terformat)
        elif num == 5:
            print(ZipfLaw(kalimat_terformat))
        elif num == 6:
            print("============= Hasil Gabungan =============")
            print(TestMulti(kalimat_terformat))
        elif num == 0:
            file.close()
            exit()
        else:
            print("Tidak ada pilihan!")
    except ValueError:
        print("Silakan pilih menu!")

if __name__ == "__main__":
    while(True):
        print()
        menu()
