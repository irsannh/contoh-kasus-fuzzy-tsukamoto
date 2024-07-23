import math

print("Contoh Kasus Penghitungan Logika Fuzzy (Metode Tsukamoto)")
print("Silakan masukkan Suhu dan Kelembapan")
suhu = float(input("Masukkan Suhu: "))
kelembapan = float(input("Masukkan Kelembapan: "))

print(f"Suhu: {suhu}")
print(f"Kelembapan: {kelembapan}")

def fungsi_keanggotaan_suhu_dingin(suhu):
    if(suhu >= 24):
        return 0
    elif(suhu > 22 and suhu < 24):
        return ((suhu - 22)/(24 - 22))
    elif(suhu <= 22):
        return 1

def fungsi_keanggotaan_suhu_ideal(suhu):
    if(suhu >= 29 or suhu <= 22):
        return 0
    elif(suhu > 22 and suhu < 24):
        return ((suhu - 22)/(24 - 22))
    elif(suhu > 27 and suhu < 29):
        return ((29 - suhu)/(29 - 27))
    elif(suhu >= 24 and suhu <= 27):
        return 1

def fungsi_keanggotaan_suhu_panas(suhu):
    if(suhu <= 27):
        return 0
    elif(suhu > 27 and suhu < 29):
        return ((29 - x)/(29 - 27))
    elif(suhu >= 29):
        return 1

def fungsi_keanggotaan_kelembapan_rendah(kelembapan):
    if(kelembapan >= 60):
        return 0
    elif(kelembapan > 55 and kelembapan < 60):
        return((60 - kelembapan)/(60 - 55))
    elif(kelembapan <= 55):
        return 1

def fungsi_keanggotaan_kelembapan_sedang(kelembapan):
    if(kelembapan >= 80 or kelembapan <= 55):
        return 0
    elif(kelembapan > 55 and kelembapan < 60):
        return ((kelembapan - 55)/(60 - 55))
    elif(kelembapan > 75 and kelembapan < 80):
        return((80 - kelembapan)/(80 - 75))
    elif(kelembapan >= 60 and kelembapan <= 75):
        return 1

def fungsi_keanggotaan_kelembapan_ideal(kelembapan):
    if(kelembapan <= 75):
        return 0
    elif(kelembapan > 75 and kelembapan < 80):
        return ((80 - kelembapan)/(80 - 75))
    elif(kelembapan >= 80):
        return 1

derajat_suhu_dingin = fungsi_keanggotaan_suhu_dingin(suhu)
derajat_suhu_ideal = fungsi_keanggotaan_suhu_ideal(suhu)
derajat_suhu_panas = fungsi_keanggotaan_suhu_panas(suhu)
derajat_kelembapan_rendah = fungsi_keanggotaan_kelembapan_rendah(kelembapan)
derajat_kelembapan_sedang = fungsi_keanggotaan_kelembapan_sedang(kelembapan)
derajat_kelembapan_ideal = fungsi_keanggotaan_kelembapan_ideal(kelembapan)
print("Derajat Keanggotaan Suhu: ")
print(f"Derajat Keanggotaan Dingin Untuk Suhu {suhu} derajat celcius adalah:{derajat_suhu_dingin}")
print(f"Derajat Keanggotaan Ideal Untuk Suhu {suhu} derajat celcius adalah:{derajat_suhu_ideal}")
print(f"Derajat Keanggotaan Panas Untuk Suhu {suhu} derajat celcius adalah:{derajat_suhu_panas}")
print("------------------------------------------")
print("------------------------------------------")
print(f"Derajat Keanggotaan Rendah Untuk Suhu {kelembapan} derajat celcius adalah:{derajat_kelembapan_rendah}")
print(f"Derajat Keanggotaan Sedang Untuk Suhu {kelembapan} derajat celcius adalah:{derajat_kelembapan_sedang}")
print(f"Derajat Keanggotaan Ideal Untuk Suhu {kelembapan} derajat celcius adalah:{derajat_kelembapan_ideal}")
print("------------------------------------------")
print("Proses Inferensi")
aturan_1 = min(derajat_suhu_dingin, derajat_kelembapan_rendah)
aturan_2 = min(derajat_suhu_dingin, derajat_kelembapan_sedang)
aturan_3 = min(derajat_suhu_dingin, derajat_kelembapan_ideal)
aturan_4 = min(derajat_suhu_ideal, derajat_kelembapan_rendah)
aturan_5 = min(derajat_suhu_ideal, derajat_kelembapan_sedang)
aturan_6 = min(derajat_suhu_ideal, derajat_kelembapan_ideal)
aturan_7 = min(derajat_suhu_panas, derajat_kelembapan_rendah)
aturan_8 = min(derajat_suhu_panas, derajat_kelembapan_sedang)
aturan_9 = min(derajat_suhu_panas, derajat_kelembapan_ideal)
print(f"Hasil Inferensi Aturan 1: {aturan_1}")
print(f"Hasil Inferensi Aturan 2: {aturan_2}")
print(f"Hasil Inferensi Aturan 3: {aturan_3}")
print(f"Hasil Inferensi Aturan 4: {aturan_4}")
print(f"Hasil Inferensi Aturan 5: {aturan_5}")
print(f"Hasil Inferensi Aturan 6: {aturan_6}")
print(f"Hasil Inferensi Aturan 7: {aturan_7}")
print(f"Hasil Inferensi Aturan 8: {aturan_8}")
print(f"Hasil Inferensi Aturan 9: {aturan_9}")
print("------------------------------------------")

def hitung_kecepatan_kipas_aturan_1(aturan_1):
    if aturan_1 == 0:
        return 40
    elif(aturan_1 > 0 and aturan_1 < 1):
        return (40 - (aturan_1 * 15))
    elif aturan_1 == 1:
        return 25

def hitung_kecepatan_kipas_aturan_2(aturan_2):
    if aturan_2 == 0:
        return 40
    elif (aturan_2 > 0 and aturan_2 < 1):
        return (40 - (aturan_2 * 15))
    elif aturan_2 == 1:
        return 25

def hitung_kecepatan_kipas_aturan_3(aturan_3):
    if aturan_3 == 0:
        return 40
    elif (aturan_3 > 0 and aturan_3 < 1):
        return (40 - (aturan_3 * 15))
    elif aturan_3 == 1:
        return 25

def hitung_kecepatan_kipas_aturan_4(aturan_4):
    if aturan_4 == 0:
        return 25
    elif (aturan_4 > 0 and aturan_4 < 1):
        return ((aturan_4 * 57) + 25)
    elif aturan_4 == 1:
        return 82

def hitung_kecepatan_kipas_aturan_5(aturan_5):
    if aturan_5 == 0:
        return 25
    elif (aturan_5 > 0 and aturan_5 < 1):
        return ((aturan_5 * 57) + 25)
    elif aturan_5 == 1:
        return 82

def hitung_kecepatan_kipas_aturan_6(aturan_6):
    if aturan_6 == 0:
        return 25
    elif (aturan_6 > 0 and aturan_6 < 1):
        return ((aturan_6 * 57) + 25)
    elif aturan_6 == 1:
        return 82

def hitung_kecepatan_kipas_aturan_7(aturan_7):
    if aturan_7 == 0:
        return 128
    elif (aturan_7 > 0 and aturan_7 < 1):
        return ((aturan_7 * 12) + 128)
    elif aturan_7 == 1:
        return 140

def hitung_kecepatan_kipas_aturan_8(aturan_8):
    if aturan_8 == 0:
        return 128
    elif (aturan_8 > 0 and aturan_8 < 1):
        return ((aturan_8 * 12) + 128)
    elif aturan_8 == 1:
        return 140

def hitung_kecepatan_kipas_aturan_9(aturan_9):
    if aturan_9 == 0:
        return 128
    elif (aturan_9 > 0 and aturan_9 < 1):
        return ((aturan_9 * 12) + 128)
    elif aturan_9 == 1:
        return 140

def hitung_durasi_pompa_aturan_1(aturan_1):
    if aturan_1 == 0:
        return 110000
    elif (aturan_1 > 0 and aturan_1 < 1):
        return ((aturan_1 * 10000) + 110000)
    elif aturan_1 == 1:
        return 120000

def hitung_durasi_pompa_aturan_2(aturan_2):
    if aturan_2 == 0:
        return 25000
    elif (aturan_2 > 0 and aturan_2 < 1):
        return ((aturan_2 * 48000) + 25000)
    elif aturan_2 == 1:
        return 73000

def hitung_durasi_pompa_aturan_3(aturan_3):
    if aturan_3 == 0:
        return 35000
    elif (aturan_3 > 0 and aturan_3 < 1):
        return (35000 - (aturan_3 * 10000))
    elif aturan_3 == 1:
        return 25000

def hitung_durasi_pompa_aturan_4(aturan_4):
    if aturan_4 == 0:
        return 110000
    elif (aturan_4 > 0 and aturan_4 < 1):
        return ((aturan_4 * 10000) + 110000)
    elif aturan_4 == 1:
        return 120000

def hitung_durasi_pompa_aturan_5(aturan_5):
    if aturan_5 == 0:
        return 25000
    elif (aturan_5 > 0 and aturan_5 < 1):
        return ((aturan_5 * 48000) + 25000)
    elif aturan_5 == 1:
        return 73000

def hitung_durasi_pompa_aturan_6(aturan_6):
    if aturan_6 == 0:
        return 35000
    elif (aturan_6 > 0 and aturan_6 < 1):
        return (35000 - (aturan_6 * 10000))
    elif aturan_6 == 1:
        return 25000

def hitung_durasi_pompa_aturan_7(aturan_7):
    if aturan_7 == 0:
        return 110000
    elif (aturan_7 > 0 and aturan_7 < 1):
        return ((aturan_7 * 10000) + 110000)
    elif aturan_7 == 1:
        return 120000

def hitung_durasi_pompa_aturan_8(aturan_8):
    if aturan_8 == 0:
        return 25000
    elif (aturan_8 > 0 and aturan_8 < 1):
        return ((aturan_8 * 48000) + 25000)
    elif aturan_8 == 1:
        return 73000

def hitung_durasi_pompa_aturan_9(aturan_9):
    if aturan_9 == 0:
        return 35000
    elif (aturan_9 > 0 and aturan_9 < 1):
        return (35000 - (aturan_9 * 10000))
    elif aturan_9 == 1:
        return 25000

def hitung_durasi_heater_aturan_1(aturan_1):
    if aturan_1 == 0:
        return 30000
    elif (aturan_1 > 0 and aturan_1 < 1):
        return ((aturan_1 * 30000) + 30000)
    elif aturan_1 == 1:
        return 60000

def hitung_durasi_heater_aturan_2(aturan_2):
    if aturan_2 == 0:
        return 30000
    elif (aturan_2 > 0 and aturan_2 < 1):
        return ((aturan_2 * 30000) + 30000)
    elif aturan_2 == 1:
        return 60000

def hitung_durasi_heater_aturan_3(aturan_3):
    if aturan_3 == 0:
        return 30000
    elif (aturan_3 > 0 and aturan_3 < 1):
        return ((aturan_3 * 30000) + 30000)
    elif aturan_3 == 1:
        return 60000

def hitung_durasi_heater_aturan_4(aturan_4):
    if aturan_4 == 0:
        return 60000
    elif (aturan_4 > 0 and aturan_4 < 1):
        return (60000 - (aturan_4 * 30000))
    elif aturan_4 == 1:
        return 30000

def hitung_durasi_heater_aturan_5(aturan_5):
    if aturan_5 == 0:
        return 60000
    elif (aturan_5 > 0 and aturan_5 < 1):
        return (60000 - (aturan_5 * 30000))
    elif aturan_5 == 1:
        return 30000

def hitung_durasi_heater_aturan_6(aturan_6):
    if aturan_6 == 0:
        return 60000
    elif (aturan_6 > 0 and aturan_6 < 1):
        return (60000 - (aturan_6 * 30000))
    elif aturan_6 == 1:
        return 30000

def hitung_durasi_heater_aturan_7(aturan_7):
    if aturan_7 == 0:
        return 60000
    elif (aturan_7 > 0 and aturan_7 < 1):
        return (60000 - (aturan_7 * 30000))
    elif aturan_7 == 1:
        return 30000

def hitung_durasi_heater_aturan_8(aturan_8):
    if aturan_8 == 0:
        return 60000
    elif (aturan_8 > 0 and aturan_8 < 1):
        return (60000 - (aturan_8 * 30000))
    elif aturan_8 == 1:
        return 30000

def hitung_durasi_heater_aturan_9(aturan_9):
    if aturan_9 == 0:
        return 60000
    elif (aturan_9 > 0 and aturan_9 < 1):
        return (60000 - (aturan_9 * 30000))
    elif aturan_9 == 1:
        return 30000

kipas_hasil_aturan_1 = hitung_kecepatan_kipas_aturan_1(aturan_1)
kipas_hasil_aturan_2 = hitung_kecepatan_kipas_aturan_2(aturan_2)
kipas_hasil_aturan_3 = hitung_kecepatan_kipas_aturan_3(aturan_3)
kipas_hasil_aturan_4 = hitung_kecepatan_kipas_aturan_4(aturan_4)
kipas_hasil_aturan_5 = hitung_kecepatan_kipas_aturan_5(aturan_5)
kipas_hasil_aturan_6 = hitung_kecepatan_kipas_aturan_6(aturan_6)
kipas_hasil_aturan_7 = hitung_kecepatan_kipas_aturan_7(aturan_7)
kipas_hasil_aturan_8 = hitung_kecepatan_kipas_aturan_8(aturan_8)
kipas_hasil_aturan_9 = hitung_kecepatan_kipas_aturan_9(aturan_9)

pompa_hasil_aturan_1 = hitung_durasi_pompa_aturan_1(aturan_1)
pompa_hasil_aturan_2 = hitung_durasi_pompa_aturan_2(aturan_2)
pompa_hasil_aturan_3 = hitung_durasi_pompa_aturan_3(aturan_3)
pompa_hasil_aturan_4 = hitung_durasi_pompa_aturan_4(aturan_4)
pompa_hasil_aturan_5 = hitung_durasi_pompa_aturan_5(aturan_5)
pompa_hasil_aturan_6 = hitung_durasi_pompa_aturan_6(aturan_6)
pompa_hasil_aturan_7 = hitung_durasi_pompa_aturan_7(aturan_7)
pompa_hasil_aturan_8 = hitung_durasi_pompa_aturan_8(aturan_8)
pompa_hasil_aturan_9 = hitung_durasi_pompa_aturan_9(aturan_9)

heater_hasil_aturan_1 = hitung_durasi_heater_aturan_1(aturan_1)
heater_hasil_aturan_2 = hitung_durasi_heater_aturan_2(aturan_2)
heater_hasil_aturan_3 = hitung_durasi_heater_aturan_3(aturan_3)
heater_hasil_aturan_4 = hitung_durasi_heater_aturan_4(aturan_4)
heater_hasil_aturan_5 = hitung_durasi_heater_aturan_5(aturan_5)
heater_hasil_aturan_6 = hitung_durasi_heater_aturan_6(aturan_6)
heater_hasil_aturan_7 = hitung_durasi_heater_aturan_7(aturan_7)
heater_hasil_aturan_8 = hitung_durasi_heater_aturan_8(aturan_8)
heater_hasil_aturan_9 = hitung_durasi_heater_aturan_9(aturan_9)

print(f"Output Aturan 1 (Kecepatan Kipas): {kipas_hasil_aturan_1}")
print(f"Output Aturan 2 (Kecepatan Kipas): {kipas_hasil_aturan_2}")
print(f"Output Aturan 3 (Kecepatan Kipas): {kipas_hasil_aturan_3}")
print(f"Output Aturan 4 (Kecepatan Kipas): {kipas_hasil_aturan_4}")
print(f"Output Aturan 5 (Kecepatan Kipas): {kipas_hasil_aturan_5}")
print(f"Output Aturan 6 (Kecepatan Kipas): {kipas_hasil_aturan_6}")
print(f"Output Aturan 7 (Kecepatan Kipas): {kipas_hasil_aturan_7}")
print(f"Output Aturan 8 (Kecepatan Kipas): {kipas_hasil_aturan_8}")
print(f"Output Aturan 9 (Kecepatan Kipas): {kipas_hasil_aturan_9}")
print("------------------------------------------")
print(f"Output Aturan 1 (Durasi Pompa): {pompa_hasil_aturan_1}")
print(f"Output Aturan 2 (Durasi Pompa): {pompa_hasil_aturan_2}")
print(f"Output Aturan 3 (Durasi Pompa): {pompa_hasil_aturan_3}")
print(f"Output Aturan 4 (Durasi Pompa): {pompa_hasil_aturan_4}")
print(f"Output Aturan 5 (Durasi Pompa): {pompa_hasil_aturan_5}")
print(f"Output Aturan 6 (Durasi Pompa): {pompa_hasil_aturan_6}")
print(f"Output Aturan 7 (Durasi Pompa): {pompa_hasil_aturan_7}")
print(f"Output Aturan 8 (Durasi Pompa): {pompa_hasil_aturan_8}")
print(f"Output Aturan 9 (Durasi Pompa): {pompa_hasil_aturan_9}")
print("------------------------------------------")
print(f"Outpur Aturan 1 (Durasi Heater): {heater_hasil_aturan_1}")
print(f"Outpur Aturan 2 (Durasi Heater): {heater_hasil_aturan_2}")
print(f"Outpur Aturan 3 (Durasi Heater): {heater_hasil_aturan_3}")
print(f"Outpur Aturan 4 (Durasi Heater): {heater_hasil_aturan_4}")
print(f"Outpur Aturan 5 (Durasi Heater): {heater_hasil_aturan_5}")
print(f"Outpur Aturan 6 (Durasi Heater): {heater_hasil_aturan_6}")
print(f"Outpur Aturan 7 (Durasi Heater): {heater_hasil_aturan_7}")
print(f"Outpur Aturan 8 (Durasi Heater): {heater_hasil_aturan_8}")
print(f"Outpur Aturan 9 (Durasi Heater): {heater_hasil_aturan_9}")

output_kipas = ((aturan_1 * kipas_hasil_aturan_1) + (aturan_2 * kipas_hasil_aturan_2) + (aturan_3 * kipas_hasil_aturan_3) + (aturan_4 * kipas_hasil_aturan_4) + (aturan_5 * kipas_hasil_aturan_5) + (aturan_6 * kipas_hasil_aturan_6) + (aturan_7 * kipas_hasil_aturan_7) + (aturan_8 * kipas_hasil_aturan_8) + (aturan_9 * kipas_hasil_aturan_9))/(aturan_1 + aturan_2 + aturan_3 + aturan_4 + aturan_5 + aturan_6 + aturan_7 + aturan_8 + aturan_9)
output_pompa = ((aturan_1 * pompa_hasil_aturan_1) + (aturan_2 * pompa_hasil_aturan_2) + (aturan_3 * pompa_hasil_aturan_3) + (aturan_4 * pompa_hasil_aturan_4) + (aturan_5 * pompa_hasil_aturan_5) + (aturan_6 * pompa_hasil_aturan_6) + (aturan_7 * pompa_hasil_aturan_7) + (aturan_8 * pompa_hasil_aturan_8) + (aturan_9 * pompa_hasil_aturan_9))/(aturan_1 + aturan_2 + aturan_3 + aturan_4 + aturan_5 + aturan_6 + aturan_7 + aturan_8 + aturan_9)
output_heater = ((aturan_1 * heater_hasil_aturan_1) + (aturan_2 * heater_hasil_aturan_2) + (aturan_3 * heater_hasil_aturan_3) + (aturan_4 * heater_hasil_aturan_4) + (aturan_5 * heater_hasil_aturan_5) + (aturan_6 * heater_hasil_aturan_6) + (aturan_7 * heater_hasil_aturan_7) + (aturan_8 * heater_hasil_aturan_8) + (aturan_9 * heater_hasil_aturan_9))/(aturan_1 + aturan_2 + aturan_3 + aturan_4 + aturan_5 + aturan_6 + aturan_7 + aturan_8 + aturan_9)
print(f"Kecepatan Kipas Yang Diperlukan Adalah: {math.ceil(output_kipas)} PWM")
print(f"Durasi Pompa Aktifnya Adalah: {math.ceil(output_pompa)} milisecond")
print(f"Durasi Heater Aktifnya Adalah: {math.ceil(output_heater)} milisecond")