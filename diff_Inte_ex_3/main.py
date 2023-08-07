import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
y=[]
x=[]
with open("dataA.txt") as file:
    for line in file:
        if line.strip() != "":
            data=line.split()
            x.append(float(data[0]))
            y.append(float(data[1]))
plt.plot(x,y)
# Customizing y-axis tick marks
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=15))
plt.xticks(rotation=45) 
plt.show()
