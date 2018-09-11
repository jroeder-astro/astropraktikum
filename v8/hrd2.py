import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from numpy import *

x1 = []
y1 = []

with open('p-e-new.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append(float(row[0]))
        y1.append(float(row[1]))

x2 = [a*15 for a in x1]

fig, ax1 = plt.subplots()
ax1.plot(x2, y1, '-bo')
ax1.set_xlabel('Rektaszension (deg)')
ax1.set_ylabel('Dekl (deg)')

#ax2 = ax1.twinx()

#ax2.set_ylabel('Absolute Helligkeit /mag')


ax1.set_xlim(209,202)
#ax2.set_ylim(8.5,-3.5)

#plt.ylabel('Helligkeit /mag')
#plt.xlabel('B-V /mag')
plt.title('Pluto-Bewegung')
#plt.legend()
plt.show()
