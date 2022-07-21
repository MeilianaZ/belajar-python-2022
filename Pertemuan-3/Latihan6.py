jumlah = 0
angka = 0
n=int(input('banyaknya angka yang akan dimasukkan = '))
while angka!='':
    angka = input('Masukkan angka = ')
    if angka !='':
        angka = float(angka)
        jumlah += angka
mean = jumlah/n
print('rata-ratanya adalah',round(mean,2))
