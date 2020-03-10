
import matplotlib.pyplot as plt
import numpy as np
from classparticle import *


x = np.array([1, 1, 19, 19, 10])
y = np.array([1, 19, 1, 19, 10])
r = np.array([1000, 1000, 1000, 1000, 1000]) # in points, not data units

r = np.ones(5)
r *=1000

print(r)

fig, ax = plt.subplots(1,1)



ax.set(xlim=(-1, L+1), ylim = (-1, L+1))
ax.axis('square')
ax.grid()

ax.scatter(x, y, s=r)


plt.show()


'''fig, ax = plt.subplots()

ax.set(xlim=(-1, 1), ylim = (-1, 1))
ax.axis('square')
ax.grid()
a_circle = plt.Circle((0, 0), 1)
ax.add_artist(a_circle)


plt.show()'''