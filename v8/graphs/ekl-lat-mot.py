import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from numpy import *

x1 = []
y1 = []

with open('solar-new.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y1.append(float(row[0]))
        x1.append(int(row[1]))

fig, ax1 = plt.subplots()
ax1.plot(x1, y1, '-b')
ax1.set_xlabel('Zeit (day)')
ax1.set_ylabel('Eklipt. Breite (deg)')
plt.tight_layout()
plt.show()
