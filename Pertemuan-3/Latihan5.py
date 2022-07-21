Tahun=int(input('Masukkan tahun = '))
if Tahun%400==0:
    print('tahun',Tahun,'adalah tahun kabisat')
elif Tahun%100==0:
    print('tahun',Tahun,'bukan tahun kabisat')
elif Tahun%4==0:
    print('tahun',Tahun,'adalah tahun kabisat')
else:
    print('tahun',Tahun,'bukan tahun kabisat')
