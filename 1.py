import numpy as np
import matplotlib.pyplot as plt

# Data
bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
curah_hujan_tahun_1 = [490, 300, 300, 260, 200, 150, 40, 70, 120, 230, 420, 400]
curah_hujan_tahun_2 = [450, 430, 430, 350, 150, 120, 50, 60, 60, 400, 500, 400]
curah_hujan_tahun_3 = [430, 400, 360, 280, 120, 100, 40, 0, 60, 340, 640, 420]

# Menentukan lebar setiap bar
bar_width = 0.25

# Menentukan posisi setiap bar pada sumbu x
posisi_bulan = np.arange(len(bulan))
posisi_tahun_1 = posisi_bulan
posisi_tahun_2 = [x + bar_width for x in posisi_bulan]
posisi_tahun_3 = [x + 2 * bar_width for x in posisi_bulan]

# Membuat bar chart
plt.bar(posisi_tahun_1, curah_hujan_tahun_1, bar_width, label='1981 - 1990')
plt.bar(posisi_tahun_2, curah_hujan_tahun_2, bar_width, label='1991 - 2000')
plt.bar(posisi_tahun_3, curah_hujan_tahun_3, bar_width, label='2001 - 2010')

# Menambahkan judul dan label sumbu
plt.title('Curah Hujan per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Curah Hujan (mm)')

# Menambahkan tick label pada sumbu x
plt.xticks(posisi_bulan, bulan)

# Menampilkan legenda
plt.legend()

# Menampilkan grafik
plt.show()