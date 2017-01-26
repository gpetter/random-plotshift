import matplotlib.pyplot as plt
import random
import numpy as np
from astropy.io import ascii

plt2=plt
num = input("Enter number of coordinates: ")
shift = random.randint(1,6)
my_listx = []
my_listy = []
shiftlist = ['shift value:', shift]

ascii.write([shiftlist], 'shift.txt', overwrite=True)
#fill x,y lists with random values
for x in range(0, num, 1):
    my_listx.append(random.randint(0,100))
    my_listy.append(random.randint(0,100))

#plot  and save initial plot with random values
plt.plot(my_listx, my_listy, 'ro')

plt.savefig('initial_plot.png', bbox_inches='tight')
print('init_coordinates.txt \n', my_listx, "\n", my_listy)
ascii.write([my_listx, my_listy], 'init_coordinates.txt', names=('x','y'), overwrite=True)
plt.show()
plt.close()


axes = plt2.gca()
axes.set_xlim([0,100])
axes.set_ylim([0,100])

#randomly choose which axis will be shifted, and shift all values by the same random number
if random.randint(0,1) == 0:
    for x in range(0, num, 1):
        my_listx[x]=my_listx[x]+shift
else:
    for x in range(0, num, 1):
        my_listy[x]=my_listy[x]+shift
print('fin_coordinates.txt \n', my_listx, '\n', my_listy)
ascii.write([my_listx, my_listy], 'fin_coordinates.txt', names=('x', 'y'), overwrite=True)

#plot and save graph which has had its values shifted
plt2.plot(my_listx,my_listy, 'ro')

plt2.savefig('shifted_plot.png', bbox_inches='tight')
