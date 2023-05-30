import matplotlib.pyplot as plt
import numpy as np
i_parallel=[3,3,3,1,1,1,0,0,0,4,2,3,2]
i_perpendicular=[2,1,1,2,1,1,1,2,4,4,3,3,3]
theta_i=[20,25,30,35,40,45,50,55,60,65,70,75,80]

ratio=[i_parallel[i]/i_perpendicular[i] for i in range(len(i_perpendicular))]

# Degree of the fitting polynomial
deg = 4
# Parameters from the fit of the polynomial
p = np.polyfit(theta_i, ratio, deg)
m = p[0]  # Gradient
c = p[1]  # y-intercept

print(f'The fitted straight line has equation y = {m:.1f}x {c:=+6.1f}')

# Number of observations
n = len(theta_i)
# Number of parameters: equal to the degree of the fitted polynomial (ie the
# number of coefficients) plus 1 (ie the number of constants)
m = len(ratio)
# Degrees of freedom (number of observations - number of parameters)
dof = n - m
# Significance level
alpha = 0.05
# We're using a two-sided test
tails = 2
# The percent-point function (aka the quantile function) of the t-distribution
# gives you the critical t-value that must be met in order to get significance
# t_critical = stats.t.ppf(1 - (alpha / tails), dof)

# Model the data using the parameters of the fitted straight line
y_model = np.polyval(p, theta_i)

# Create the linear (1 degree polynomial) model
model = np.poly1d(p)
# Fit the model
y_model = model(theta_i)

# Mean
y_bar = np.mean(ratio)
# Coefficient of determination, R²
R2 = np.sum((y_model - y_bar)**2) / np.sum((ratio - y_bar)**2)

print(f'The fitted straight line has equation y = {m:.1f}x {c:=+6.1f}')

plt.plot(theta_i, ratio, c='gray', marker='o', edgecolors='k', s=18)
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