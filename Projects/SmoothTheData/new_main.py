# Student ID  : 2423341
# Project Name: Smooth Data
# Project ID  : S-GEN-SmoothData
# Description : This code is used to smooth the data and calculate the chi-square value.

import math
import matplotlib.pyplot as plt

   
x=[]
y=[]
with open("data.txt") as file:
    lines = file.readlines()  # Read all lines into a list
    lines.reverse()  # Reverse the order of the lines

    for line in lines:
        if line.strip() != "":
            data = line.split()
            x.append(float(data[0]))
            y.append(float(data[1]))

plt.plot(x, y)

smooth_x=[]
smooth_y=[]
def moving_average(N):
    for i in range(len(x)):
        avg_x_data=[]
        avg_y_data=[]
        if(N%2==0):
            for j in range(1,int(N/2)+1):
                if(i+j >= len(x)):
                    avg_x_data.append(x[i])
                    avg_y_data.append(y[i])
                else:
                    avg_x_data.append(x[i+j])
                    avg_y_data.append(y[i+j])

            for j in range(int(-N/2),0):
                if(i+j<0):
                    avg_x_data.append(x[i])
                    avg_y_data.append(y[i])
                else:
                    avg_x_data.append(x[i+j])
                    avg_y_data.append(y[i+j])
        else:
            for j in range(1,int(N/2)+2):
                if(i+j >= len(x)):
                    avg_x_data.append(x[i])
                    avg_y_data.append(y[i])
                else:
                    avg_x_data.append(x[i+j])
                    avg_y_data.append(y[i+j])

            for j in range(int(-N/2),0):
                if(i+j<0):
                    avg_x_data.append(x[i])
                    avg_y_data.append(y[i])
                else:
                    avg_x_data.append(x[i+j])
                    avg_y_data.append(y[i+j])
        smooth_x.append(sum(avg_x_data)/N)
        smooth_y.append(sum(avg_y_data)/N)

def chi_square():
    chi_elements=[]
    for i in range(len(y)):
        chi_elements.append((smooth_y[i]-y[i])/y[i])
    return sum(chi_elements)
N=10
moving_average(N)
plt.plot(x, smooth_y)
plt.title("USA inflation rate")#USA inflation rate
plt.xlabel("time(years)")#x
plt.ylabel("Rate(%)")#rate
plt.legend(["Real Data", "Smooth Data"])
plt.text(0.02, 0.05, f"Chi-square: {round(chi_square(),2)}", transform=plt.gca().transAxes, ha='left', va='top')
plt.text(0.02, 0.09, f"N: {N}", transform=plt.gca().transAxes, ha='left', va='top')

plt.show()
#######DATA:https://www.macrotrends.net/countries/USA/united-states/inflation-rate-cpi
