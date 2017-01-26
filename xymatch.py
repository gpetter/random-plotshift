import pyraf

f = open('init_coordinates.txt', "r")
lines = f.readlines()
xlist_init = []
ylist_init = []
for x in lines:
    xlist_init.append(x.split(' ')[1])
    ylist_init.append(x.split(' ')[2])
f.close()

f = open('fin_coordinates.txt', "r")
lines = f.readlines()
xlist_fin = []
ylist_fin = []
for x in lines:
    xlist_fin.append(x.split(' ')[1])
    ylist_fin.append(x.split(' ')[2])
f.close()

print(xlist_init[1])
pyraf.xyxymatch(xlist_init, xlist_fin)
