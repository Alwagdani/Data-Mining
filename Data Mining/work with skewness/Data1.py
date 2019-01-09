import math
import statistics
def mean():
    global stockPrice
   
    count= len(stockPrice)
    sumation =sum(stockPrice)
    mean =sumation/count
    print ("Mean of list:",sumation/count)
    return mean
    

def median():
    global stockPrice   
    orderList = stockPrice.copy()
    orderList.sort()
    lenthOfList = len(orderList)
    if(lenthOfList%2 ==1):        
        middle = (lenthOfList//2 )       
        print ("Median of list:",orderList[middle])
        return orderList[middle]
def mode():
    global stockPrice
   
    occurance=[]
    occurance=[[x,stockPrice.count(x)] for x in set(stockPrice)]
    maxCount=0
    maxNumber=[]   
    for i in range(0,len(occurance)):
        if occurance[i][1]>maxCount:            
            maxCount =occurance[i][1]
            maxNumber=[]           
            maxNumber.append(occurance[i][0])
        if occurance[i][1]==maxCount:
            maxNumber.append(occurance[i][0])   
    if maxNumber[0] == 1:
        print ("All values only appear once")
    elif len(maxNumber) > 1:
        print ("List has multiple modes")
    else:
        print ("Mode of list:", maxNumber[0])

def Std():
    global stockPrice
    meanX = mean()
    summation =0
    for e in stockPrice:
        temp =e-meanX
        temp = temp**2
        summation += temp
    var =summation/(len(stockPrice)-1)
    std=math.sqrt(var)
    print ("STD of List = ", std)
    return std

    
def min_max(parm):
    global stockPrice
    min_max= (parm - min(stockPrice))/(max(stockPrice)- min(stockPrice))
    print ('MIN-MAX NORMALIZATION of ',str(parm), '$ is ',min_max)

def mid_Range():
    global stockPrice
    ranges = max(stockPrice)- min(stockPrice)   
    midRange = 0.5 *ranges + min(stockPrice)
    print ('Mid Rnge is  ',midRange)

def zScore(parm):
    global stockPrice
    meanX = mean()
    stdX =Std()
    zScore = (parm -meanX)/ stdX
    print ('zScore of ',parm, '$ is ',zScore)
    return zScore

def decimalScaling(parm):
    global stockPrice
    d = len(str(max(stockPrice)))
    xdec = parm / (10**d)
    print ('Decimal scaling of  ',parm, '$ is ',xdec)

def skewness():
    global stockPrice
    Xmedian = median()
    Zmean = 0
    Zmedian = zScore(Xmedian)
    skewness =Zmean -Zmedian
    print ('skewness is ',skewness)

    
    

    
    
    
stockPrice =[10,7,20,12,75,15,9,18,4,12,4]
mean()
median()
mode()
Std()
min_max(20)
mid_Range()
zScore(20)
decimalScaling(20)
skewness()

