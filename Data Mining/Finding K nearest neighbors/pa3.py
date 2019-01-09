#############################################
## Program to solve problem 12, chapter 7 from textbook
##  using the data in Table 7.5, find the k-nearest nieghbor for record #10  using k = 3
##  ACSG555: Datamining & Warehousing
##  Date: Oct,10
##  Author: Hana Alwagdani
##  File:C:\Users\Hanan\Desktop\PA3  
#############################################

import csv 	#	To read csv file
import sklearn
from sklearn.neighbors import NearestNeighbors

neigh = NearestNeighbors( n_neighbors = 3)

samples = [ ]
file_name = "Figure_7_5.csv"
with open(file_name) as csv_file:
	f75_Reader = csv.reader( csv_file, delimiter=",")
	row_count = 0

	for row in f75_Reader:
		row_count = row_count + 1
		if( row == [] ):
			continue
		# create a new row to put first 4 columns from row
		newRow = [ ]
                # process the row
		newRow.append( float( row[0]) )
		newRow.append( float( row[1]) )
		if( row [2] == " Single"):
			newRow.append(float(0) )
		if( row [2] == " Married"):
			newRow.append(float(1) )
		if( row [2] == " Other"):
			newRow.append( float(2) )
		newRow.append( float( row[3]) )
		
		# process target variable
		if( row [4] == " Bad loss"):
			row[4] = 0
		if( row [4] == " Good risk"):
			row[4] = 1
		
		samples.append ( newRow )

neigh.fit( samples)
print("row count", row_count)
for r in samples:
	print( r)

distances, indices = neigh.kneighbors( [[ 10, 66, 1, 36120.34]])

print("distances", end=":")
for d in distances:
	print( d )

print("indices", end=":")
for index in indices:
	print( index )















