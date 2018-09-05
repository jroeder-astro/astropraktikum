import matplotlib.pyplot as plt
import numpy as np
import csv
from numpy import *

x1 = []
y1 = []

with open('hrd.dat', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y1.append(float(row[0]))
        x1.append(float(row[1]))

plt.plot(x1, y1, 'bo', label='HRD Data')
plt.plot([0.65],[9.73],'ro')
#plt.title('Altersbestimmung von Sternhaufen\nHertzsprung-Russell-Diagramm')
plt.ylabel('Helligkeit /mag')
plt.xlabel('B-V /mag')
plt.legend(loc=4)
plt.show()
