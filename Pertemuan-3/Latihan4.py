Wavelength=float(input('Panjang gelombang cahaya (nm) = '))
if 380<=Wavelength<450:
    print('Spektrum yang terlihat adalah Violet')
elif 450<=Wavelength<495:
    print('Spektrum yang terlihat adalah Blue')
elif 495<=Wavelength<570:
    print('Spektrum yang terlihat adalah Green')
elif 570<=Wavelength<590:
    print('Spektrum yang terlihat adalah Yellow')
elif 590<=Wavelength<620:
    print('Spektrum yang terlihat adalah Orange')
elif 620<=Wavelength<750:
    print('Spektrum yang terlihat adalah Red')
else :
    print('input kamu diluar spektrum yang diketahui…!!')
