import matplotlib.pyplot as plt

x=[]
y=[]

with open("data.txt") as file:
    for line in file:
        data=line.split()
        x.append(data[1])
        y.append(data[2])

print("{0} was {1}".format("Ahmet", "here"))

# plt.plot(x,y,linestyle="--")
# plt.xlabel("X laber is here")
# plt.ylabel("y abel is here")
# plt.title("title is here")
# plt.savefig("dneme.jpg")
# plt.show()