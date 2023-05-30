import matplotlib.pyplot as plt
import math
import numpy as np
theta_i=[20,30,40,50,60,70,80]
theta_t=[6,9.5,14.5,19,25,32,40]

ratio=[(math.tan(theta_i[i]-theta_t[i])/math.tan(theta_i[i]+theta_t[i]))/((math.sin(theta_i[i]-theta_t[i])/math.sin(theta_i[i]+theta_t[i])))**2 for i in range(len(theta_i))]

# Fit the data to a 4th degree polynomial function
p = np.polyfit(theta_i, ratio, deg=4)

# Create the polynomial object
fitted_polynomial = np.poly1d(p)

# Get the equation as a string
equation = str(fitted_polynomial)

# Generate points on the fitted curve
x_fitted = np.linspace(min(theta_i), max(theta_i), 100)
y_fitted = np.polyval(p, x_fitted)

# Log the obtained mathematical expression and fit
print("Fitted Equation:", equation)
print("Fit of the Equation:", list(zip(x_fitted, y_fitted)))

# Plot the data and the fitted curve
import matplotlib.pyplot as plt

plt.plot(theta_i, ratio, 'o', label='Data')
plt.plot(x_fitted, y_fitted, label='Best-fit Curve')

plt.xlabel("θ(i°)")
plt.ylabel("r(parallel)/r(perpendicular)")
plt.legend()
plt.show()
