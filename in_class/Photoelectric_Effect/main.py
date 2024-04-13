from matplotlib import pyplot as plt
from math import floor, log10

V365=[-2.0,-1.909,-1.5,-1.0,-0.5,0.0,5.0,10.0,15.0,20.0,25.0,30.0]
i365=[-5.0,0.0,152,473,805,1190,6500,10830,14500,17700,20000,22500]

V405=[-2.0,-1.5,-1.462,-1.0,-0.5,0.0,5.0,10.0,15.0,20.0,25.0,30.0]
i405=[-9.5,-0.2,0.0,72,173,288,1660,2770,3680,4450,5110,5610]

V436=[-2.0,-1.5,-1.3,-1.0,-0.5,0.0,5.0,10.0,15.0,20.0,25.0,30.0]
i436=[-13.2,-9.7,0.0,75,23.8,410,2340,3910,5140,6260,7170,7870]

V546=[-2.0,-1.5,-1.0,-0.781,-0.5,0.0,5.0,10.0,15.0,20.0,25.0,30.0]
i546=[-7.4,-7.2,-6.9,0.0,77.8,277,1570,2500,3160,3630,3960,4170]

V577=[-2.0,-1.5,-1.0,-0.672,-0.5,0.0,5.0,10.0,15.0,20.0,25.0,30.0]
i577=[-3.1,-2.8,-2.6,0.0,15.8,91.8,532,840,1036,1167,1260,1323]

def sci_notation(num, decimal_digits=1, precision=None, exponent=None):
    if exponent is None:
        exponent = int(floor(log10(abs(num))))
    coeff = round(num / float(10**exponent), decimal_digits)
    if precision is None:
        precision = decimal_digits

    return r"${0:.{2}f}\cdot10^{{{1:d}}}$".format(coeff, exponent, precision)

plt.plot(V365,i365, label = "Dataset: λ=365nm")
plt.plot(V405,i405, label = "Dataset: λ=405nm")
plt.plot(V436,i436, label = "Dataset: λ=436nm")
plt.plot(V546,i546, label = "Dataset: λ=546nm")
plt.plot(V577,i577, label = "Dataset: λ=577nm")

scinum = 1e-13

plt.legend()
plt.xlabel("Voltage(V)")
plt.ylabel(f"Current ({sci_notation(scinum,1)}A)")
plt.title(f"Current ({sci_notation(scinum,1)}A) - Voltage(V) graph")

plt.xlim(-2, 0)
plt.ylim(-2, 2)

plt.show()