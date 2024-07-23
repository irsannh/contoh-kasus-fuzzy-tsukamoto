import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt

x = np.arange(0, 256, 1)

mati = fuzzy.trapmf(x, [0, 0, 25, 40])
pelan = fuzzy.trimf(x, [25, 82, 140])
cepat = fuzzy.trapmf(x, [128, 140, 255, 255])

plt.figure()
plt.plot(x, mati, color='#00008B', linewidth=1.5, label='Mati')
plt.plot(x, pelan, color='#006400', linewidth=1.5, label='Pelan')
plt.plot(x, cepat, color='#8B0000', linewidth=1.5, label='Cepat')
plt.title('Grafik Keanggotaan Himpunan Fuzzy Output Kecepatan Kipas')
plt.ylabel('Keanggotaan')
plt.xlabel('Variabel')

points = [25, 82, 140]
for point in points:
    plt.plot([point, point], [0, 1], 'k--', linewidth=0.75)

plt.xticks([0, 25, 40, 82, 128, 140, 255], ['0', '25', '40', '82', '128', '140', '255'])

plt.legend()
plt.show()