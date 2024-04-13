import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd

csv_file_path = 'in_class\HE_Hall_Effect\part2data.csv' 

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path, sep='\t')

flux_density = df['flux_density']
hall_voltage = df['hall_voltage']
sample_voltage = df['sample_voltage']

print(hall_voltage[0])

x=sample_voltage
y=flux_density

fitA = np.polyfit(x , y , 1)
mA = fitA [0] # extract the m value in y = mx + n line equation
nA = fitA [1] # extract the n value in y = mx + n line equation                 

equationA = "Fit Function = " + str(round(mA ,4)) + "$x_A$" " + " + str(round(nA ,4))
 
y_new = np.polyval(fitA , x)
plt.plot(x, y, color ='red', label = "Experimental results")
plt.plot(x, y_new, color ='blue', label = "Fit graph")

# plt.errorbar(x , y , yerr = [0.1,0.1,0.1,0.1,0.1], linestyle = "none")
scinum = 1e14

plt.legend()
plt.ylabel("Magnetic Field(mT)(B)")
plt.xlabel("Sample Voltage(mV)($V_{sample}$)")
plt.title(f"Magnetic Field(mT) - Sample Voltage(mA)")
plt.text(15,0, equationA , fontsize = 16, color = "blue", rotation = 0)

plt.show()