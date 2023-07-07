import matplotlib.pyplot as plt

plt.rcParams['figure.subplot.bottom'] = 0.283

# Data
tanggal_waktu = [
    '24 Juli 2013 00.00 UTC', '24 Juli 2013 03.00 UTC', '24 Juli 2013 06.00 UTC',
    '24 Juli 2013 09.00 UTC', '24 Juli 2013 12.00 UTC', '24 Juli 2013 15.00 UTC',
    '24 Juli 2013 18.00 UTC', '24 Juli 2013 21.00 UTC', '25 Juli 2013 00.00 UTC'
]
asimilasi = [23.1, 25.4, 25.5, 24.9, 22.5, 22.3, 23.0, 22.0, 25.7]
observasi = [24.0, 25.0, 23.8, 23.9, 24.0, 24.2, 24.0, 22.9, 23.0]
non_amilasi = [23.5, 25.5, 25.2, 25.5, 24.9, 25.0, 24.5, 24.2, 25.9]

# Membuat plot
plt.plot(tanggal_waktu, asimilasi, marker='o', markersize=3, linewidth=2, color='blue', label='Asimilasi')
plt.plot(tanggal_waktu, observasi, marker='o', markersize=3, linewidth=2, color='yellow', label='Observasi')
plt.plot(tanggal_waktu, non_amilasi, marker='o', markersize=3, linewidth=2, color='red', label='Non Amilasi')

# Menambahkan judul dan label sumbu
plt.title('Grafik Data')
plt.xlabel('Tanggal & Waktu')
plt.ylabel('Nilai')

# Menentukan rentang sumbu y
plt.ylim(20, 27)

# Menampilkan legenda
plt.legend()

# Menampilkan grafik
plt.xticks(rotation=45)
plt.show()
