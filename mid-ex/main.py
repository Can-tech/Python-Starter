import matplotlib.pyplot as plt
x_t=[]
y_d=[]

with open("mid-ex/data.txt") as file:
    for line in file:
        data=line.split()
        x_t.append(data[1])
        y_d.append(data[2])

plt.bar(x_t,y_d)
plt.xlabel("Burası label X")
plt.ylabel("Burası label Y")
plt.title("Bu bir yol zaman grafiği")
plt.show()
print(x_t, y_d)

with open("mid-ex/data2.txt","w") as file:
    for i in range(len(x_t)):
        file.write(x_t[i]+"    ")
        file.write(y_d[i]+"\n")
    file.close()
x=[]
y=[]
with open("mid-ex/data2.txt","r") as file:
    for line in file:
        data=line.split()
        x.append(data[0])
        y.append(data[1])
plt.plot(x,y)
plt.savefig("graph2.jpg",format="jpeg")
plt.show()


