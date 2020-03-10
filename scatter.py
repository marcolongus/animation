
import matplotlib.pyplot as plt
import numpy as np
from classparticle import *
import matplotlib.patches as patches


x = np.array([1, 3, 5, 7, 10])
y = np.array([1, 3, 5, 7, 10])
r = np.array([1000, 1000, 1000, 1000, 1000]) # in points, not data units

circle = np.empty(shape=5, dtype=object)
print(x.size)

for i in range(5):

	circle[i]= patches.Circle((x[i], y[i]), 1, alpha=0.7, fc='green')

r = np.ones(5)
r *=1000



fig, ax = plt.subplots(1,1)

ax.set(xlim=(-1, L+1), ylim = (-1, L+1))

ax.set_xlabel('x coordinate')
ax.set_ylabel('y coordinate')

ax.axis('square')
ax.grid()

for i in range(5):

	circle[i]= patches.Circle((x[i], y[i]), 1, alpha=0.7, fc='yellow')
	ax.add_patch(circle[i])

ax.scatter(x, y)


plt.show()


'''fig, ax = plt.subplots()

ax.set(xlim=(-1, 1), ylim = (-1, 1))
ax.axis('square')
ax.grid()
a_circle = plt.Circle((0, 0), 1)
ax.add_artist(a_circle)


plt.show()'''