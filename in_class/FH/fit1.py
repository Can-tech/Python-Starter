import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x_1=[9,12,14,17,19,22]
y_1=[1,-1,1,-1,1,-1]

x_2=[8.5,11,14.5,16,19,21,24,26.5]
y_2=[1,-1,1,-1,1,-1,1,-1 ]
x=x_2
y=y_2

# Test function with coefficients as parameters
def test(x, a, b,c,d):
    return a * np.sin(b*x + c) + d

param, param_cov = curve_fit(test, x, y)

print("Sine function coefficients:")
print(param)
print("Covariance of coefficients:")
print(param_cov)

x_fit = np.linspace(8.5, 26.5, 100)  # 200 points between min(x_2) and max(x_2)
y_fit = param[0] * (np.sin(param[1] * x_fit+param[2])) + param[3]
 
plt.scatter(x, y, color ='red', label = "Dataset: 3. and 4. columns")
plt.plot(x_fit, y_fit, color ='blue', label = "fit graph")
plt.legend()
plt.xlabel("Voltage(V)")
plt.ylabel("Max-Min")
plt.title("Max-Min Value - Voltage(V)")
plt.text(10, 0.95, r'Period: 1.56π', fontsize=19, color='blue')
plt.show()