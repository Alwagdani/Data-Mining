import scipy.stats as stats
import csv
import math
import matplotlib.pyplot as plt


def mean():
    global int_Min
   
    count= len(int_Min)
    sumation =sum(int_Min)
    mean =sumation/count   
    return mean

def Std():
    global int_Min
    meanX = mean()
    summation =0
    for e in int_Min:
        temp =e-meanX
        temp = temp**2
        summation += temp
    var =summation/(len(int_Min)-1)
    std=math.sqrt(var)   
    return std

def zScore():
    global int_Min
    meanX = mean()
    stdX =Std()
    z =[]
    for e in int_Min:
        z.append( (e -meanX)/ stdX)    
    return z



    


int_Min=[]        
with open('churn.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    next(reader)
    for row in reader:
      int_Min.append(float(row[14]))

z= zScore()
stats.probplot(z, dist="norm", plot=plt)
plt.title("Normal Q-Q plot")
plt.show()

