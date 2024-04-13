import numpy as np

fit_function="-2.5x+3.5"
hf=0.395
work_function=3.5
experimental_f=[8.214, 7.408, 6.879, 5.490, 5.196]
mean_value = np.mean(experimental_f)
print(mean_value)
planck_constant=0.39/(mean_value*10**14)
print(planck_constant)