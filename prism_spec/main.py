import matplotlib.pyplot as plt
#refractive İndex
y=[1.492,1.486,1.503]
#wavelength
x=[577*10**-9,546.1*10**-9,404.6*10**-9]

plt.plot(x,y)
plt.xlabel("wavelengths")
plt.ylabel("refractive index(n)")
plt.show()