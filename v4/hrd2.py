import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from numpy import *

x1 = []
y1 = []

with open('hrd.dat', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y1.append(float(row[0]))
        x1.append(float(row[1]))

y2 = [a - 5.5 for a in y1]

fig, ax1 = plt.subplots()
ax1.plot(x1, y1, 'bo', label='HRD Data')
ax1.set_xlabel('B-V /mag')
ax1.set_ylabel('Scheinbare Helligkeit /mag')

ax2 = ax1.twinx()

ax2.set_ylabel('Absolute Helligkeit /mag')

ax1.plot([0.65],[10.5],'ro')
ax1.set_ylim(14,2)
ax2.set_ylim(8.5,-3.5)

#plt.ylabel('Helligkeit /mag')
#plt.xlabel('B-V /mag')
plt.legend()
plt.show()
