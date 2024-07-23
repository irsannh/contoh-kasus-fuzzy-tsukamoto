import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt

x = np.arange(0, 120001, 1)

mati = fuzzy.trapmf(x, [0, 0, 30000, 60000])
nyala = fuzzy.trapmf(x, [30000, 60000, 120000, 120000])

plt.plot(x, mati, color='#00008B', linewidth=1.5, label='Mati')
plt.plot(x, nyala, color='#8B0000', linewidth=1.5, label='Nyala')
plt.title('Grafik Keanggotaan Himpunan Fuzzy Output Durasi Heater')
plt.ylabel('Keanggotaan')
plt.xlabel('Variabel')

points = [30000, 60000]
for point in points:
    plt.plot([point, point], [0, 1], 'k--', linewidth=0.75)

plt.xticks([0, 30000, 60000, 120000], ['0', '30000', '60000', '120000'])

plt.legend()
plt.show()