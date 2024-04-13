#d=(2R/r)*n*lambda
#use d=(2R*1/slope)
d1=(2*(63.5*10**-3)*(0.0675**-1))*100
print(d1)#2.66 angstrom -> 266pm
d2=(2*(63.5*10**-3)*(0.0936**-1))*100
print(d2)#1.91 angstrom -> 191pm

#error:
theo_d1=213
theo_d2=123
print(((theo_d1-d1)/theo_d1)*100)#%24
print(((theo_d2-d2)/theo_d2)*100)#%55