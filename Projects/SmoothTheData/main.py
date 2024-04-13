import math
import matplotlib.pyplot as plt

   
years=[]
inflation_rate=[]
with open("./Projects/SmoothData/data.txt") as file:
    lines = file.readlines()  # Read all lines into a list
    lines.reverse()  # Reverse the order of the lines

    for line in lines:
        if line.strip() != "":
            data = line.split()
            years.append(float(data[0]))
            inflation_rate.append(float(data[1]))

plt.plot(years, inflation_rate)

smooth_years=[]
smooth_infilation_rate=[]
def moving_average(N):
    for i in range(len(years)):
        avg_years_data=[]
        avg_infilation_rate_data=[]
        if(N%2==0):
            for j in range(1,int(N/2)+1):
                if(i+j >= len(years)):
                    avg_years_data.append(years[i])
                    avg_infilation_rate_data.append(inflation_rate[i])
                else:
                    avg_years_data.append(years[i+j])
                    avg_infilation_rate_data.append(inflation_rate[i+j])

            for j in range(int(-N/2),0):
                if(i+j<0):
                    avg_years_data.append(years[i])
                    avg_infilation_rate_data.append(inflation_rate[i])
                else:
                    avg_years_data.append(years[i+j])
                    avg_infilation_rate_data.append(inflation_rate[i+j])
        else:
            for j in range(1,int(N/2)+2):
                if(i+j >= len(years)):
                    avg_years_data.append(years[i])
                    avg_infilation_rate_data.append(inflation_rate[i])
                else:
                    avg_years_data.append(years[i+j])
                    avg_infilation_rate_data.append(inflation_rate[i+j])

            for j in range(int(-N/2),0):
                if(i+j<0):
                    avg_years_data.append(years[i])
                    avg_infilation_rate_data.append(inflation_rate[i])
                else:
                    avg_years_data.append(years[i+j])
                    avg_infilation_rate_data.append(inflation_rate[i+j])
        smooth_years.append(sum(avg_years_data)/N)
        smooth_infilation_rate.append(sum(avg_infilation_rate_data)/N)

def chi_square():
    chi_elements=[]
    for i in range(len(inflation_rate)):
        chi_elements.append((smooth_infilation_rate[i]-inflation_rate[i])/inflation_rate[i])
    return sum(chi_elements)
N=10
moving_average(N)
plt.plot(years, smooth_infilation_rate)
plt.title("USA inflation rate")#USA inflation rate
plt.xlabel("Years")#Years
plt.ylabel("Rate(%)")#rate
plt.legend(["Real Data", "Smooth Data"])
plt.text(0.02, 0.05, f"Chi-square: {round(chi_square(),2)}", transform=plt.gca().transAxes, ha='left', va='top')
plt.text(0.02, 0.09, f"N: {N}", transform=plt.gca().transAxes, ha='left', va='top')

plt.show()
#######DATA:https://www.macrotrends.net/countries/USA/united-states/inflation-rate-cpi
