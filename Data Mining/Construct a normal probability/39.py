import scipy.stats as stats
import csv
import math
import matplotlib.pyplot as plt
def mean():
    global day_Min
   
    count= len(day_Min)
    sumation =sum(day_Min)
    mean =sumation/count   
    return mean

def Std():
    global day_Min
    meanX = mean()
    summation =0
    for e in day_Min:
        temp =e-meanX
        temp = temp**2
        summation += temp
    var =summation/(len(day_Min)-1)
    std=math.sqrt(var)   
    return std

def zScore():
    global day_Min
    meanX = mean()
    stdX =Std()
    z =[]
    for e in day_Min:
        z.append( (e -meanX)/ stdX)    
    return z
    


day_Min=[]        
with open('churn.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    next(reader)
    for row in reader:
      day_Min.append(float(row[7]))

z= zScore()
stats.probplot(z, dist="norm", plot=plt)
plt.title("Normal  plot")
plt.show()

