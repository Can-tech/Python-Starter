import numpy as np

theta_i = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
ratio = [3/2, 3/1, 3/1, 1/2, 1/1, 1/1, 0/1, 0/2, 0/4, 4/4, 2/3, 3/3, 2/3]

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

plt.xlabel("θ(i)")
plt.ylabel("Ratio")
plt.legend()
plt.show()
