import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import stats

delta_i=[20,30,40,50,60,70,80]
delta_t=[6,9.5,14.5,19,25,32,40]

# Degree of the fitting polynomial
deg = 1
# Parameters from the fit of the polynomial
p = np.polyfit(delta_i, delta_t, deg)
m = p[0]  # Gradient
c = p[1]  # y-intercept


# Number of observations
n = len(delta_i)
# Number of parameters: equal to the degree of the fitted polynomial (ie the
# number of coefficients) plus 1 (ie the number of constants)
m = len(delta_t)
# Degrees of freedom (number of observations - number of parameters)
dof = n - m
# Significance level
alpha = 0.05
# We're using a two-sided test
tails = 2
# The percent-point function (aka the quantile function) of the t-distribution
# gives you the critical t-value that must be met in order to get significance
t_critical = stats.t.ppf(1 - (alpha / tails), dof)

# Model the data using the parameters of the fitted straight line
y_model = np.polyval(p, delta_i)

# Create the linear (1 degree polynomial) model
model = np.poly1d(p)
# Fit the model
y_model = model(delta_i)

# Mean
y_bar = np.mean(delta_t)
# Coefficient of determination, R²
R2 = np.sum((y_model - y_bar)**2) / np.sum((delta_t - y_bar)**2)

print(f'The fitted straight line has equation y = {m:.1f}x {c:=+6.1f}')

plt.scatter(delta_i, delta_t, c='gray', marker='o', edgecolors='k', s=18)
xlim = plt.xlim()
ylim = plt.ylim()
# Line of best fit
plt.plot(np.array(xlim), p[1] + p[0] * np.array(xlim), label=f'Line of Best Fit, R² = {R2:.2f}, y = {m:.1f}x {c:=+6.1f}')
# Fit
x_fitted = np.linspace(xlim[0], xlim[1], 100)
y_fitted = np.polyval(p, x_fitted)

plt.xlabel("θ(i)")
plt.ylabel("θ(t)")
plt.legend(fontsize=8)
plt.show()

