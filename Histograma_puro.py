#https://www.codigopiton.com/como-hacer-un-histograma-en-python/
edades = [12, 15, 13, 12, 18, 20, 19, 20, 13, 12, 13, 17, 15, 16, 13, 14, 13, 17, 19]

mapa_edades = {}

for edad in edades:
	if edad in mapa_edades:
		mapa_edades[edad] += 1
	else:
		mapa_edades[edad] = 1

for valor in sorted(mapa_edades):
	print(f'{valor}: {"*" * mapa_edades[valor]}')