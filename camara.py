import numpy as np
from celluloid import Camera
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from classparticle import *

grafico1 =  np.loadtxt('array.txt')

############################################
# Definimos figure 
############################################

fig, ax =plt.subplots()
plt.axis([-1, L+1, -1, L+1])
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axis('square')


camera = Camera(fig)


############################################

t = np.loadtxt('evolution.txt',usecols=2)
x = np.loadtxt('evolution.txt', usecols=0)
y = np.loadtxt('evolution.txt', usecols=1)

print (t.size)

for i in range(t.size):

	for j in range(N):

		if (j==0):
			circ = patches.Circle((grafico1[j,0], grafico1[j,1]), 1, alpha=0.7, fc='green')
			ax.add_patch(circ)
		else:
			circ = patches.Circle((grafico1[j,0], grafico1[j,1]), 1, alpha=0.7, fc='yellow')
			ax.add_patch(circ)

	circ = patches.Circle((x[i],y[i]), 1, alpha=0.7, fc='red')
	ax.add_patch(circ)
	

	plt.plot(x[i],y[i],"o", color='b')
	camera.snap()

animation = camera.animate(blit=True)
animation.save('otro.gif')
plt.show()


'''
fig = plt.figure()

camera = Camera(fig)

for i in range(10):
	plt.plot([i]*10)
	camera.snap()


animation = camera.animate()
animation.save('liena.gif')

################################################################
'''

'''



for i in range(N):

	if (i==0):
		circ = patches.Circle((grafico1[i,0], grafico1[i,1]), 1, alpha=0.7, fc='green')
		ax.add_patch(circ)
	else:
		circ = patches.Circle((grafico1[i,0], grafico1[i,1]), 1, alpha=0.7, fc='yellow')
		ax.add_patch(circ)

plt.plot(grafico1[0:,0],grafico1[0:,1], "o", color='b')





#######################################################################

'''