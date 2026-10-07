harga_a = 400000
harga_b = 350000
diskon_a = 13
diskon_b = 21

akhir_a = int(harga_a - (harga_a * diskon_a / 100))
akhir_b = int(harga_b - (harga_b * diskon_b / 100))

print(f"Harga sepatu A adalah {harga_a}")
print(f"Harga sepatu B adalah {harga_b}")
print(f"Sepatu A mendapat diskon {diskon_a}% sehingga harganya menjadi {akhir_a}")
print(f"Sepatu A mendapat diskon {diskon_b}% sehingga harganya menjadi {akhir_b}")