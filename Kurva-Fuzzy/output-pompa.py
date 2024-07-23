import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt

x = np.arange(0, 180001, 1)

mati = fuzzy.trapmf(x, [0, 0, 25000, 35000])
nyala_sebentar = fuzzy.trimf(x, [25000, 73000, 120000])
nyala_lama = fuzzy.trapmf(x, [110000, 120000, 180000, 180000])

plt.plot(x, mati, color='#00008B', linewidth=1.5, label='Mati')
plt.plot(x, nyala_sebentar, color='#006400', linewidth=1.5, label='Nyala Sebentar')
plt.plot(x, nyala_lama, color='#8B0000', linewidth=1.5, label='Nyala Lama')
plt.title('Grafik Keanggotaan Himpunan Fuzzy Output Durasi Pompa')
plt.ylabel('Keanggotaan')
plt.xlabel('Variabel')

points = [25000, 73000, 120000]
for point in points:
    plt.plot([point, point], [0, 1], 'k--', linewidth=0.75)

plt.xticks([0, 25000, 35000, 73000, 110000, 120000, 180000], ['0', '25000', '35000', '73000', '110000', '120000', '180000'])

plt.legend()
plt.show()