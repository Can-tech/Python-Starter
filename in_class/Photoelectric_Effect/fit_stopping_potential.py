import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from math import floor, log10

#To print beautiful exponential number on the graph
def sci_notation(num, decimal_digits=1, precision=None, exponent=None):
    if exponent is None:
        exponent = int(floor(log10(abs(num))))
    coeff = round(num / float(10**exponent), decimal_digits)
    if precision is None:
        precision = decimal_digits

    return r"${0:.{2}f}\cdot10^{{{1:d}}}$".format(coeff, exponent, precision)


frequency=[8.214,	7.408,	6.879,	5.490,	5.196]
stop_pot=[1.909,1.462,	1.3,0.781,0.672]

x=frequency
y=stop_pot

fitA = np.polyfit(x , y , 1)
mA = fitA [0] # extract the m value in y = mx + n line equation
nA = fitA [1] # extract the n value in y = mx + n line equation                 

equationA = "Fit Function = " + str(round(mA ,4)) + "$x_A$" " + " + str(round(nA ,4))
 
y_new = np.polyval(fitA , x)
plt.scatter(x, y, color ='red', label = "Experimental results")
plt.plot(x, y_new, color ='blue', label = "Fit graph")

plt.errorbar(x , y , yerr = [0.1,0.1,0.1,0.1,0.1], linestyle = "none")
scinum = 1e14

plt.legend()
plt.xlabel(f"Frequency ({sci_notation(scinum,1)})Hz")
plt.ylabel("Stopping Potential(V)")
plt.title(f"Stopping Potential(V) - Frequency ({sci_notation(scinum,1)})Hz")
plt.text(6,0.6, equationA , fontsize = 16, color = "blue", rotation = 0)

plt.show()