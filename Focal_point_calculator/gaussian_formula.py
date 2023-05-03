def gasussian_formula():
    s_i=29
    s_0=10.3
    focal_point=1/s_i+1/s_0
    print(1/focal_point)

import math
x=[-14.16,-9.3,-15.7]
def mean_value():
    sum_x=sum(x)
    return (sum_x/len(x))
mean_v=mean_value()
print(mean_v)
def error_value():
    result=0
    for e in x:
        result+=(e-mean_v)**2
    result/=len(x)-1
    print(math.sqrt(result))
error_value()




