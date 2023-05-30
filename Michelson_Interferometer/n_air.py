import math
def refAir(N,P,lambdaValue,d):
    return ((N/P*0.00986)*(lambdaValue/2*d)*1)+1
# print(refAir(14,60,650,0.034))

refractive_index_data=[refAir(3,10,650,0.034),refAir(5,20,650,0.034),refAir(10,40,650,0.034),refAir(12,50,650,0.034),refAir(14,60,650,0.034)]
print(refractive_index_data)

def calculateAvg():
    sum_data=0
    for i in refractive_index_data:
        sum_data+=i
    return sum_data/len(refractive_index_data)
avg=calculateAvg()

def deltaRefractive():
    res=0
    for i in refractive_index_data:
        res+=((i-avg)**2)/(len(refractive_index_data)-1)
    return math.sqrt(res)
print(deltaRefractive())

def errorMargin():
    print(avg+deltaRefractive(),"-",avg-deltaRefractive())

errorMargin()