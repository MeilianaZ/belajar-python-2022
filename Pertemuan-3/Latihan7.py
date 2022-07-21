usia=0
biaya=0
jum=0
while usia != '':
    usia=input('Berapa usia anda = ')
    if usia != '':
        usia=int(usia)
        if usia<=2:
            biaya=0.0
        elif 3<=usia<=12:
            biaya=14.00
        elif usia>=65:
            biaya=18.00
        else:
            biaya=23.00
        jum += biaya

print('Biaya masuk yang harus dibayar adalah $',round(jum,2))
