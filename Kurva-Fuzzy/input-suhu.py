import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt

x = np.arange(0, 41, 1)

dingin = fuzzy.trapmf(x, [0, 0, 22, 24])
ideal = fuzzy.trapmf(x, [22, 24, 27, 29])
panas = fuzzy.trapmf(x, [27, 29, 40, 40])

plt.figure()
plt.plot(x, dingin, color='#00008B', linewidth=0.75, label='Dingin')
plt.plot(x, ideal, color='#006400', linewidth=0.75, label='Ideal')
plt.plot(x, panas, color='#8B0000', linewidth=0.75, label='Panas')
plt.title('Grafik Keanggotaan Himpunan Fuzzy Input Suhu')
plt.ylabel('Keanggotaan')
plt.xlabel('Variabel')

points = [22, 24, 27, 29]
for point in points:
    plt.plot([point, point], [0, 1], 'k--', linewidth=0.75)

plt.xticks([0, 22, 24, 27, 29, 40], ['0', '22', '24', '27', '29', '40'])

plt.legend()
plt.show()