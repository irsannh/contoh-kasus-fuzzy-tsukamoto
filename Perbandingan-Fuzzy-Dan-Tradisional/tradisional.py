import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt

x = np.arange(0, 41, 1)

dingin = fuzzy.trapmf(x, [0, 0, 22, 22])

plt.figure()
plt.plot(x, dingin, color='#00008B', linewidth=0.75, label='Dingin')
plt.title('Grafik Pengendalian Secara Tradisional (Non-Fuzzy)')
plt.ylabel('Keanggotaan')
plt.xlabel('Variabel')

plt.xticks([0, 22, 40], ['0', '22', '40'])

plt.legend()
plt.show()