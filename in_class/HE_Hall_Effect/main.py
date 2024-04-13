import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

sample_current=[-30,-25,-20,-15,-10,-5,0,5,10, 15, 20, 25, 30]
hall_effect=[-61.6, -52.9, -41.3, -31.2, -22.5, -11.3, -2.4, 11.2, 19.4, 31.2, 40.4, 50.3, 60.7, ]

x=sample_current
y=hall_effect

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
plt.xlabel("Sample Current ($I_{P}$) (mA)")
plt.ylabel("Hall Voltage($V_{H}$)(mV)")
plt.title(f"Hall Voltage(mV) - Sample Current(mA)")
plt.text(-20,-60, equationA , fontsize = 16, color = "blue", rotation = 0)

plt.show()