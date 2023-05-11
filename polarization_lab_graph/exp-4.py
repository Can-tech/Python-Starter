from matplotlib import pyplot as plt
import numpy as np
x=[]
y=[]

with open("polarisization-lab-data3.txt") as file:
    for line in file:
        if not line.isspace():
            s=line.split()
            x.append(-float(s[2])*57.3)
            y.append(float(s[1]))

fig, ax = plt.subplots()
ax.plot(x,y)
# plt.scatter(61.6, 0, s=50, c='red', marker='o')
# plt.text(61+0.1, 0+0.1, f'({60}, {0})', fontsize=12)
# plt.scatter(240, 0, s=50, c='red', marker='o')
# plt.text(240, 0+0.1, f'({240}, {0})', fontsize=12)
# plt.scatter(420, 0, s=50, c='red', marker='o')
# plt.text(420, 0+0.1, f'({420}, {0})', fontsize=12)

# plt.scatter(154, 13.63, s=50, c='red', marker='o')
# plt.text(154, 13.63+0.1, f'({154}, {13.63})', fontsize=12)
# plt.scatter(334, 13.63, s=50, c='red', marker='o')
# plt.text(334, 13.63+0.1, f'({334}, {13.63})', fontsize=12)

# plt.scatter(x[0], y[0], s=50, c='red', marker='o')
# plt.text(x[0], y[0], f'({x[0]}, {y[0]})', fontsize=12)

## Label the axes
plt.xlabel("\u03b8\N{DEGREE SIGN} between the polarizers")
plt.ylabel("Intensity I(\u03b8)")

## Show the plot
plt.show()