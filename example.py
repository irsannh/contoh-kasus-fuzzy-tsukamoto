import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Mendefinisikan variabel
x = np.arange(0, 11, 1)

# Mendefinisikan himpunan fuzzy
low = fuzz.trimf(x, [0, 0, 5])
medium = fuzz.trimf(x, [0, 5, 10])
high = fuzz.trimf(x, [5, 10, 10])

# Plotting
plt.figure()
plt.plot(x, low, 'b', linewidth=1.5, label='Low')
plt.plot(x, medium, 'g', linewidth=1.5, label='Medium')
plt.plot(x, high, 'r', linewidth=1.5, label='High')
plt.title('Grafik Keanggotaan Himpunan Fuzzy')
plt.ylabel('Keanggotaan')
plt.xlabel('Variabel')
plt.legend()
plt.show()