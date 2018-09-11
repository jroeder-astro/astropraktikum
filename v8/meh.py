import matplotlib.pyplot as plt
import numpy as np
import csv
from numpy import *

x1 = []
y1 = []

with open('p-e-new.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append(float(row[0]))
        y1.append(float(row[1]))

fig = plt.plot(x1, y1,'-bo')

#plt.subplot(2,1,1)
#plt.plot(x1, y1, label='Euler')
#plt.plot(x2, y2, 'ro', label='Rec_Stefan')
#plt.plot(x3, y3, 'go', label='Rec_Jan')
#plt.ylabel('M')
#plt.legend()

#plt.subplot(2,1,2)
#plt.plot(x1, y1, label='Euler')
#plt.plot(x4, y4, 'ro', label='Rec_Stefan_RK4')
#plt.plot(x3, y3, 'go', label='Rec_Jan')
#plt.ylabel('M')
#plt.legend()

fig.set_xlim(14,13.4)

plt.title('Pluto-Bewegung')
plt.ylabel('Deklination (deg)')
plt.xlabel('Rektaszension (hrs)')
#plt.legend()
plt.show()
