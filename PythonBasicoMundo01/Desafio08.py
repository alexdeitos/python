#Leia medida em metros e imprima em centimetros e em milimetros

metros = int(input("MEDIDA EM METROS: "))
km = metros / 1000
hec = metros / 100
dam = metros /10
dc = metros * 10
cc = metros * 100
mm = metros * 1000



print("Metros: {}\n Centrimetros: {}\n Decimetros: {}\n Milimetros: {}\n ".format(metros, cc,dc,mm))
print("Kilometros: {}km\n Hectometros: {}hm\n Decametros: {:.1f}dam".format(km,hec,dam))

