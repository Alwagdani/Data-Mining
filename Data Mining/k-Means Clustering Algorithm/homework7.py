#####################################################
## Homework 7
## ACSG 555 Data Mining and Warehousing
## Due: 12/1/2018
## Author: Hanan Alwagdani
## File: C:/Users/Hanan/Desktop/homework7.py
##########################################################

from scipy.spatial import distance
import math
from random import *
import numpy as np


def computeGrandMean():
    sumX=0
    sumY=0
    for i in range (0,len(points)):
        sumX += points[i][0]
        sumY += points[i][1]
    grandMean.append(sumX/len(points))
    grandMean.append(sumY/len(points))

    
def ecluDistance(a,b):
    diffX = abs(b[0]-a[0])
    diffX2 = diffX**2
    diffY = abs(b[1]-a[1])
    diffY2 = diffY**2 
    Diff = (diffX2+diffY2)    
    EluDis = math.sqrt(Diff)
    return EluDis

def initalCenters():    
    for i in range(0,k):
        clusters.append([])
        centers.append(points[randint(0, len(points)-1)].copy())
        
def assignCluster():
    for i in range(0,len(points)):
        dist=[]
        for j in range (0,k):            
            dist.append(ecluDistance(points[i],centers[j]))
        indMin = np.argmin(dist)        
        clusters[indMin].append(points[i])       
        print(str(points[i]).ljust(15),"{0:.3f}".format(dist[0]).ljust(20),"{0:.3f}".format(dist[1]).ljust(20),str(indMin).ljust(20))
        
def reCenters():
    for i in range(0,k):
        sumX =0.0
        sumY=0.0
        for j in range(0,len (clusters[i])):
            sumX+= clusters[i][j][0]
            sumY+= clusters[i][j][1]        
        newX = sumX/(len (clusters[i]))
        newY = sumY/(len (clusters[i]))
        centers[i][0]=newX
        centers[i][1]=newY
    
    
def computeSSB():
    global SSB
    temp=0.0
    for i in range(0,k):
        temp=0.0
        temp=(centers[i][0] - grandMean[0])**2       
        temp+=  (centers[i][1] - grandMean[1])**2               
        SSB +=  len(clusters[i]) * temp
    print("SSB: {0:.3f}".format(SSB))
    
def computeMSB():
    global SSB
    MSB=0.0   
    MSB= SSB/(k-1)
    print("MSB: {0:.3f}".format(MSB))


def computeMSE():
    global SSE
    N= len(points)
    MSE=0.0   
    MSE= SSE/(N-k)
    print("MSE: {0:.3f}".format(MSE))

def F():
    global MSB
    global MSE    
    F=0.0   
    F= MSB/MSE
    print("F: {0:.3f}".format(F))
         
        
points = [[1,3],[3,3],[4,3],[5,3],[1,2],[4,2],[1,1],[2,1]]
centers =[]
clusters=[]
dist=[]
grandMean=[]
computeGrandMean()
SSB=0.0
MSB=0.0
SSE=0.0
MSE=0.0
F=0.0
k = input('Please Enter The number of cluster: ')
k= int(k)
initalCenters()
for i in range(0,3):    
    print("******************")
    print ("Point".ljust(15),"Distance from m1".ljust(20),"Distance from m2".ljust(20),"Cluster Membership".ljust(20))
    assignCluster()
    reCenters()
    computeSSB()
    computeMSB()
    clusters[0]= []
    clusters[1]= []
   
       
