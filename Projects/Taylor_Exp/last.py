# Student ID  : 2423341
# Project Name: Taylor Expansion
# Project ID  : S-Taylor
# Description : This code calculates the Taylor expansion of e^x and compares it with the real value of e^x for a given x value. It also investigates the % error for random x value and increasing N values.

import math
import matplotlib.pyplot as plt
import random



N=int(input("Number of expansion terms: "))
x=float(input("x value: "))

x_prime=x*1.2


##Taylor serie calculator
def taylor(x,N):
    serie=[]
    for i in range(0,N+1):
        serie.append(x**i/math.factorial(i))
    return sum(serie)

##Taylor serie array
i = 0
taylor_y = []
taylor_x = []
while (i <= x_prime):
    taylor_x.append(i)
    taylor_y.append(taylor(i,N))
    i+=0.1

##e^x array
exp_x=[]
exp_y=[]
j=0
while (j<=x_prime):
    exp_x.append(j)
    exp_y.append(math.exp(j))
    j+=0.1
####Draw the Graph
##plot
plt.plot(taylor_x,taylor_y, linestyle='--', color='red')
plt.plot(exp_x,exp_y)

##Settings
plt.grid(True)
plt.axvline(x, linestyle='--', color="black")
indices = [i for i, val in enumerate(taylor_x) if round(val, 1) == round(x,1)]
index = indices[0]
if indices:
    plt.axhline(taylor_y[index], linestyle='--', color="black")
    plt.axhline(exp_y[index], linestyle='--', color="black")
plt.legend([f"Taylor: {round(taylor_y[index],2)}", f"e\u00B2: {round(exp_y[index],2)}"],loc='upper left')
plt.text(0.02, 0.75, f'x={x}', transform=plt.gca().transAxes, ha='left', va='top')
plt.text(0.02, 0.80, f'N={N}', transform=plt.gca().transAxes, ha='left', va='top')
plt.text(0.02, 0.85, f'Difference={round(exp_y[index]-taylor_y[index],2)}', transform=plt.gca().transAxes, ha='left', va='top')
plt.ylabel("f(x)")
plt.xlabel("x")

plt.show()

####ERROR
N_err=20
x_err=random.randint(2,10)

taylor_x_err=[]
taylor_y_err=[]

for i in range(N_err):
    taylor_y_err.append(taylor(x_err,i))
    taylor_x_err.append(i)

exp_err=math.exp(x_err)

difference_array=[((exp_err-i)/exp_err)*100 for i in taylor_y_err]

plt.plot(taylor_x_err,difference_array)
plt.axhline(0, linestyle='--', color="black")
plt.axhline(100, linestyle='--', color="black")
plt.ylabel("%Error")
plt.xlabel("N")
plt.show()

