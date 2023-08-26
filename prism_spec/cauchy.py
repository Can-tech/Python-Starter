import matplotlib.pyplot as plt

#wavelength
x=[577*(10**(-9)),546.1*(10**(-9)),404.6*(10**(-9))]
#refractive index
y=[1.53+(-1.285*(10**(-14)))/(i**2) for i in x]

y_experiment=[1.492,1.486,1.503]

plt.plot(x,y)
plt.scatter(x,y_experiment)
plt.xlabel("wavelength")
plt.ylabel("refractive index")
plt.legend(["Cauchy's Equation", "Experimental data"])
plt.text(0.02, 0.75, f'A = 1.53', transform=plt.gca().transAxes, ha='left', va='top')
plt.text(0.02, 0.81, f"B = 1.2851 * 10\u207B\u00B9\u2074", transform=plt.gca().transAxes, ha='left', va='top')
plt.title("Cauchy's equation and the experimental data")
plt.show()