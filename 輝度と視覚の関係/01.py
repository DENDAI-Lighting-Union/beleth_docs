import matplotlib.pyplot as plt
import math

Y = []
L = []

fig = plt.figure()

ax = fig.add_subplot()

maxVal = 1000000

for i in range(maxVal+1):
    y = i/maxVal
    y100 = y/1
    y100_3 = math.pow(y100,(1/3))
    y100_3_116 = 116*y100_3
    Y.append(y*255)
    L.append(((y100_3_116-16)/100)*255)

    
ax.plot(Y,L)

ax.set_aspect('equal', adjustable='box')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.set_xlim([0, 255]) 
ax.set_ylim([0, 255]) 

ax.set_xlabel("Actual brightness(DMX Value)")
ax.set_ylabel("Brightness perceived by the sense of sight")

equation_text = r'$L^*  = 116(\frac{Y}{255})^{\frac{1}{3}}-16$'

text_x = 0.7*255
text_y = 0.2*255

ax.text(text_x, text_y, equation_text, fontsize=12,
        ha='center', va='center',
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.5'))

plt.savefig("main_1.png")