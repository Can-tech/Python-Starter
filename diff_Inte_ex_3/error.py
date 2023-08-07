import math
y_A=[3.3*(10**(-2)),2*(10**(-2)),3.5*(10**(-2))]
y_B=[0.012,0.018,0.018,0.015,0.015,0.015]
y_C=[0.01,0.005,0.01,0.012,0.01,0.08,0.007,0.008,0.007]
y_D=[0.004,0.053,0.002,0.018,0.004,0.012,0.039]
y_E=[0.003,0.003,0.002,0.003,0.002,0.003,0.002,0.004,0.002]
y_F=[0.005,0.006,0.004]
a=16*(10**(-5))
d=50*(10**(-5))
a=d
L=101.5*(10**(-2))
y=y_D
avg=sum(y)/len(y)

new_y=[]
for i in y:
    new_y.append(((i-avg)**2))
error_y=math.sqrt(sum(new_y)/2)


error_lambda=a/L*error_y


lambda_value=a*avg/L

lambda_interval_min=lambda_value-error_lambda
lambda_interval_max=lambda_value+error_lambda
print("avg: ", avg)
print("lambda value: ", lambda_value)
print("err y:", error_y)
print("err lamb,", error_lambda)
print("lambda intreval",lambda_interval_min,"-",lambda_interval_max)
