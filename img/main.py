# Fungsi untuk membaca input himpunan dari pengguna tanpa fungsi bawaan
def baca_himpunan():
    input_pengguna = input("Masukkan elemen-elemen untuk Himpunan (dipisahkan dengan koma): ")
    elemen = input_pengguna.split(",")  # Memisahkan elemen berdasarkan koma
    hasil_himpunan = set()  # Membuat himpunan kosong
    
    for e in elemen:
        hasil_himpunan.add(e.strip())  # Menambah elemen ke himpunan setelah menghapus spasi
    
    return hasil_himpunan

# 1. Himpunan Bagian (Subset)
def apakah_himpunan_bagian(himpunan1, himpunan2):
    for elemen in himpunan1:
        if elemen not in himpunan2:
            return False
    return True

# 2. Gabungan Himpunan (Union)
def gabungan_himpunan(himpunan1, himpunan2):
    hasil = himpunan1.copy()
    for elemen in himpunan2:
        if elemen not in hasil:
            hasil.add(elemen)
    return hasil

# 3. Himpunan Disjoint (Tidak memiliki elemen yang sama)
def apakah_disjoint(himpunan1, himpunan2):
    for elemen in himpunan1:
        if elemen in himpunan2:
            return False
    return True

# 4. Pengurangan Himpunan (Difference)
def pengurangan_himpunan(himpunan1, himpunan2):
    hasil = set()
    for elemen in himpunan1:
        if elemen not in himpunan2:
            hasil.add(elemen)
    return hasil

# 5. Himpunan Biasa (Intersection)
def irisan_himpunan(himpunan1, himpunan2):
    hasil = set()
    for elemen in himpunan1:
        if elemen in himpunan2:
            hasil.add(elemen)
    return hasil

# 6. Himpunan Kuasa (Power Set)
def himpunan_kuasa(himpunan):
    hasil = [[]]  # Memulai dengan himpunan kosong
    for elemen in himpunan:
        hasil += [subset + [elemen] for subset in hasil]
    kuasa = []
    for subset in hasil:
        kuasa.append(set(subset))
    return kuasa

# 7. Kardinalitas Himpunan
def kardinalitas_himpunan(himpunan):
    count = 0
    for _ in himpunan:
        count += 1
    return count

# 8. Memeriksa apakah dua himpunan sama (identik)
def apakah_sama(himpunan1, himpunan2):
    if kardinalitas_himpunan(himpunan1) != kardinalitas_himpunan(himpunan2):
        return False
    for elemen in himpunan1:
        if elemen not in himpunan2:
            return False
    return True

# 9. Memeriksa apakah dua himpunan memiliki jumlah anggota yang sama
def apakah_sama_kardinalitas(himpunan1, himpunan2):
    return kardinalitas_himpunan(himpunan1) == kardinalitas_himpunan(himpunan2)

# Meminta pengguna untuk memasukkan himpunan
print("Masukkan elemen-elemen untuk kedua himpunan.")
print("Contoh format input: A1, A2, B1, C, ...")

himpunan_A = baca_himpunan()
himpunan_B = baca_himpunan()

# Menampilkan hasil operasi himpunan
print("\n=== Hasil Operasi Himpunan ===")
print("Himpunan A:", himpunan_A)
print("Himpunan B:", himpunan_B)
print("Kardinalitas A:", kardinalitas_himpunan(himpunan_A))
print("Kardinalitas B:", kardinalitas_himpunan(himpunan_B))

# Operasi himpunan
print("\nOperasi Himpunan:")
if apakah_himpunan_bagian(himpunan_A, himpunan_B):
    print("1. Apakah A subset dari B? Ya")
else:
    print("1. Apakah A subset dari B? Tidak")

print("2. Gabungan A dan B:", gabungan_himpunan(himpunan_A, himpunan_B))

if apakah_disjoint(himpunan_A, himpunan_B):
    print("3. Apakah A dan B disjoint? Ya")
else:
    print("3. Apakah A dan B disjoint? Tidak")

print("4. Pengurangan A - B:", pengurangan_himpunan(himpunan_A, himpunan_B))
print("5. Irisan A dan B:", irisan_himpunan(himpunan_A, himpunan_B))

if apakah_sama(himpunan_A, himpunan_B):
    print("6. Apakah A dan B sama? Ya")
else:
    print("6. Apakah A dan B sama? Tidak")

if apakah_sama_kardinalitas(himpunan_A, himpunan_B):
    print("7. Apakah A dan B memiliki jumlah anggota yang sama? Ya")
else:
    print("7. Apakah A dan B memiliki jumlah anggota yang sama? Tidak")

print("\nHimpunan Kuasa:")
print("8. Himpunan Kuasa A:", himpunan_kuasa(himpunan_A))
print("9. Himpunan Kuasa B:", himpunan_kuasa(himpunan_B))