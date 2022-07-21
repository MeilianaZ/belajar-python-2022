Magnitude=float(input('Kekuatan gempa (magnitude) = '))
if Magnitude<2:
    print('Gempa tersebut adalah gempa jenis Micro')
elif 2<=Magnitude<3:
    print('Gempa tersebut adalah gempa jenis Very Minor')
elif 3<=Magnitude<4:
    print('Gempa tersebut adalah gempa jenis Minor')
elif 4<=Magnitude<5:
    print('Gempa tersebut adalah gempa jenis Light')
elif 5<=Magnitude<6:
    print('Gempa tersebut adalah gempa jenis Moderate')
elif 6<=Magnitude<7:
    print('Gempa tersebut adalah gempa jenis Strong')
elif 7<=Magnitude<8:
    print('Gempa tersebut adalah gempa jenis Major')
elif 8<=Magnitude<10:
    print('Gempa tersebut adalah gempa jenis Great')
else :
    print('Gempa tersebut adalah gempa jenis Meteoric')
