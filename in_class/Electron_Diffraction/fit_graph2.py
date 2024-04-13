import numpy as np
import matplotlib.pyplot as plt

Wavelength = [27.38, 25.81, 24.49, 23.35, 22.36]
First_Ring_Avg_Radius = [1.340, 1.370, 1.245, 1.218, 1.108]
Second_Ring_Avg_Radius = [2.212,2.143,2.009,1.941,1.900]

plt.plot(First_Ring_Avg_Radius , Wavelength , color = "red", marker = "s", label = "First Ring",
linestyle = "none")
plt.plot(Second_Ring_Avg_Radius , Wavelength , color = "black", marker = "o", label = "Second Ring",
linestyle = "none")

plt.errorbar(First_Ring_Avg_Radius , Wavelength , yerr = [0.0964,0.0642,0.1403,0.1891,0.2103 ], linestyle = "none")
plt.errorbar(Second_Ring_Avg_Radius , Wavelength , yerr = [0.0224,0.1193,0.1129,0.1396,0.1962], linestyle = "none")

fitA = np.polyfit(First_Ring_Avg_Radius , Wavelength , 1)
mA = fitA [0] # extract the m value in y = mx + n line equation
nA = fitA [1] # extract the n value in y = mx + n line equation                 

# store the line equation y = mx + n in a variable called equationA
# "round(x,y)" function rounds the number x to y decimals
# "str()" function turns its argument into string (text)
equationA = "$y_A$ = " + str(round(mA ,4)) + "$x_A$" " + " + str(round(nA ,4))

fitB = np.polyfit(Second_Ring_Avg_Radius , Wavelength , 1)
mB = fitB [0] # extract the m value in y = mxˆ2 + nx + c curve equation
nB = fitB [1] # extract the n value in y = mxˆ2 + nx + c curve equation

# store the curve equation y = mxˆ2 + nx + c in a variable called equationB
equationB = "$y_B$ = " + str(round(mB ,4)) + "$x_B$" " + " + str(round(nB ,4))

Wavelength_new = np.polyval(fitA , First_Ring_Avg_Radius)
plt.plot(First_Ring_Avg_Radius , Wavelength_new , color = "blue")

Wavelength_new = np.polyval(fitB , Second_Ring_Avg_Radius)
plt.plot(Second_Ring_Avg_Radius , Wavelength_new , color = "green")

plt.title("Wavelength vs Radius", fontsize =20)
plt.xlabel("Radius(cm)", fontsize =18)
plt.ylabel("Wavelengt(pm)", fontsize =18)

plt.xticks(fontsize =16); plt.yticks(fontsize =16)

# show equations on the plot
# first two numbers indicate the starting (x,y) coordinates of the text
# you can use "rotation" and "color" options for better visualizations

plt.text(1.2, 22.5, equationA , fontsize = 13, color = "blue", rotation =   0)
plt.text(1.9, 26.5, equationB , fontsize = 13, color = "green", rotation = 0)

plt.legend(fontsize =16); plt.grid(alpha =0.5, linestyle ="--")
plt.show()
# plt.savefig("CombinedGraphs_finalversion.pdf", bbox_inches = "tight")
