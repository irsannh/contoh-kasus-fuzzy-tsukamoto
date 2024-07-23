import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt

x = np.arange(0, 101, 1)

rendah = fuzzy.trapmf(x, [0, 0, 55, 60])
sedang = fuzzy.trapmf(x, [55, 60, 75, 80])
ideal = fuzzy.trapmf(x, [75, 80, 100, 100])

plt.figure()
plt.plot(x, rendah, color='#00008B', linewidth=0.75, label='Rendah')
plt.plot(x, sedang, color='#006400', linewidth=0.75, label='Sedang')
plt.plot(x, ideal, color='#8B0000', linewidth=0.75, label='Ideal')
plt.title('Grafik Keanggotaan Himpunan Fuzzy Input Kelembapan')
plt.ylabel('Keanggotaan')
plt.xlabel('Variabel')

points = [55, 60, 75, 80]
for point in points:
    plt.plot([point, point], [0, 1], 'k--', linewidth=0.75)

plt.xticks([0, 55, 60, 75, 80, 100], ['0', '55', '60', '75', '80', '100'])

plt.legend()
plt.show()