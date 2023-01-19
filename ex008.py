medida = float(input('Informe uma medida: '))
cm = medida * 100
mm = medida * 1000
dec = medida * 10
dam = medida / 10
km = medida / 1000

print('O valor em metros é {} \nConvertido em mm {:.0f}mm \nConvertido em cm {:.0f}cm \nConvertido em dec {:.0f}dec \nConvertido em dam {:.1f}dam \nConvertido em kn {:.3f}km'.format(medida,mm,cm,dec,dam,km))
