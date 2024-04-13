import math

a=0;
V_A = [4000,4500,5000,5500,6000];
for V in V_A:
    print(f"wavelength: {math.sqrt(150/V)*100}")