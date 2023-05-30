import math

d=[3,5,6,10,20]
N=[10,14,18,31,64]
data=[]


class ResultData:
    def __init__(self, dist,N_count):
        self.lambdaResult=0
        self.findLambda(dist,N_count)
    def findLambda(self,d,N):
        self.lambdaResult=1000*((2*1*d)/N)

for i in range(len(d)):
    new_data=ResultData(d[i],N[i])
    data.append(new_data)

def findLambda(d,N):
    print(1000*((2*1*d)/N))
# findLambda(20,64)

def calculateAvg():
    lamdaSum=0
    for i in data:
        lamdaSum+=i.lambdaResult
    return lamdaSum/len(data)
avg=calculateAvg()

def deltaLambda():
    res=0
    for i in data:
        res+=((i.lambdaResult-avg)**2)/(len(data)-1)
    return math.sqrt(res)

print(deltaLambda())

# print(calculateAvg())

