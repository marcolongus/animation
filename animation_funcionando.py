import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from classparticle import *
import matplotlib.patches as patches


data = np.loadtxt("evolution.txt",usecols=(0,1), unpack=True)
array =np.loadtxt("array.txt",usecols=(0,1), unpack=True)

x=np.loadtxt("array.txt", usecols=0)
y=np.loadtxt("array.txt", usecols=1)

#print(data),print() # (2, 25) array
print(data[..., :4]) # same as data[:, cols 0 to col 3]


######################################################################3

grafico1 = np.loadtxt('array.txt')


fig1 = plt.figure()
ax1 = fig1.add_axes([0.1,0.1,0.8,0.8])

l, = ax1.plot([],[],'o')


plt.title("Obstacles configuration") 
plt.xlabel("x axis") 
plt.ylabel("y axis")

plt.axis('square')

plt.xlim(-1,L+1)
plt.ylim(-1,L+1)

#Graficamos la configuración inical de obstáculos

for i in range(N):

	if (i==0):
		circ = patches.Circle((grafico1[i,0], grafico1[i,1]), 1, alpha=0.7, fc='green')
		ax1.add_patch(circ)
	else:
		circ = patches.Circle((grafico1[i,0], grafico1[i,1]), 1, alpha=0.7, fc='yellow')
		ax1.add_patch(circ)

plt.plot(grafico1[0:,0],grafico1[0:,1], "o", color='b')
plt.grid(color='b', linestyle='-.', linewidth=0.5)
#plt.axis('square')



def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,

line_ani = animation.FuncAnimation(fig1, update_line, frames=99, fargs=(data, l), interval=300, blit=True)

plt.show()

