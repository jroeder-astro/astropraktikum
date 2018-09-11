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

x3 = []
y3 = []

with open('p-e-next.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x3.append(float(row[0]))
        y3.append(float(row[1]))

x2 = [a*15 for a in x1]

fig, ax1 = plt.subplots()
ax1.plot(x2, y1, '-bo', label = 'Bewegung')
ax1.plot(x3, y3, '-go', label = 'keine Eigenbew.')
ax1.set_xlabel('Rektaszension (deg)')
ax1.set_ylabel('Dekl (deg)')
ax1.set_xlim(209,200.5)
plt.tight_layout()
plt.legend()
plt.show()
