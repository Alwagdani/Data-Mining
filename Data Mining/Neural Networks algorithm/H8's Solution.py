###############################################################################
##  Preparation of dataset to use NN in Orange 3
##
##	HANDS-ON ANALYSIS 
##	Exercise 12 Page 207
##	Chapter 9: Neural Networks 
##  Larose & Larose textbook: Discovering Knowledge in Data 2e
##  
##
##
## ACSG 555 Data Mining and Warehousing
## Saint Xavier University
## Date: 12/08/2018
##
## Author: Hanan Alwagdani
## 
## 
## File:C:\Users\Hanan\Desktop\H8\H8's Solution.py
##          
###############################################################################

import csv      # To read & write csv files in Python
import pandas as pd


output_field_names = [  "Account Length", # 0
                        "CustServ Calls", # 1
                        "Day Calls",    # 2
                        "Day Mins",     # 3
                        "Eve Calls",    # 4
                        "Eve Mins",     # 5
                        "Intl Calls",   # 6
                        "Intl Mins",    # 7
                        "Int'l Plan",    # 8 Dichotomous ==> Binary: 1 or 0
                        "Night Calls",  # 9
                        "Night Mins",   # 10
                        "VMail Message",# 11 
                        "VMail Plan",   # 12 Dichotomous ==> Binary: 1 or 0
                        "Churn?"         # 13
          ]

##########################################################################
##
##########################################################################

def minMaxs( df, output_field_names ):
  global min_0, max_0, range_0
  min_0 = min( df[ output_field_names[0]] )
  max_0 = max( df[output_field_names[0]] )
  range_0 = max_0 - min_0
  ##
  global min_1, max_1, range_1
  min_1 = min( df[output_field_names[1]] )
  max_1 = max( df[output_field_names[1]] )
  range_1 = max_1 - min_1

  ##
  global min_2, max_2,range_2
  min_2 = min( df[ output_field_names[2]] )
  max_2 = max( df[output_field_names[2]] )
  range_2 = max_2 - min_2

  ##
  global min_3, max_3, range_3
  min_3 = min( df[output_field_names[3]] )
  max_3 = max( df[output_field_names[3]] )
  range_3 = max_3 - min_3
  
  ##
  global min_4, max_4, range_4
  min_4 = min( df[ output_field_names[4]] )
  max_4 = max( df[output_field_names[4]] )
  range_4 = max_4 - min_4

  ##
  global min_5, max_5, range_5
  min_5 = min( df[output_field_names[5]] )
  max_5 = max( df[output_field_names[5]] )
  range_5 = max_5 - min_5

  ##
  global min_6, max_6, range_6
  min_6 = min( df[ output_field_names[6]] )
  max_6 = max( df[output_field_names[6]] )
  range_6 = max_6 - min_6

  ##
  global min_7, max_7, range_7
  min_7 = min( df[output_field_names[7]] )
  max_7 = max( df[output_field_names[7]] )
  range_7 = max_7 - min_7

  ##
  global min_9, max_9, range_9
  min_9 = min( df[output_field_names[9]] )
  max_9 = max( df[output_field_names[9]] )
  range_9 = max_9 - min_9

  ##
  global min_10, max_10, range_10
  min_10 = min( df[ output_field_names[10]] )
  max_10 = max( df[output_field_names[10]] )
  range_10 = max_10 - min_10

  ##
  global min_11, max_11, range_11
  min_11 = min( df[output_field_names[11]] )
  max_11 = max( df[output_field_names[11]] )
  range_11 = max_11 - min_11



# read the input file using pandas

input_file_name = "churn.csv"
df = pd.read_csv(input_file_name, delimiter=",")

# variables to count rows

row_count=0
# compute mins, mxs and ranges

minMaxs (df, output_field_names)

output_file_name = "churn_4NN.csv"

with open(output_file_name, mode="w", newline ="") as out_csv_file:

    writer = csv.DictWriter(out_csv_file, fieldnames=output_field_names)
    writer.writeheader()
    for index, row in df.iterrows():
        row_count =+1

        if row[output_field_names[8]] == "yes":
            Intlplan = 1
        else:
            Intlplan = 0

        if row[output_field_names[12]] == "yes":
            Vmainlplan = 1
        else:
            Vmainlplan = 0

        
        if row[output_field_names[13]] == "True.":
            churn = 1
        else:
           churn = 0

        # ready to write the modified row
        writer.writerow( {output_field_names[0]:(row [output_field_names[0]] - min_0)/ range_0,
                          output_field_names[1]:(row [output_field_names[1]] - min_1)/ range_1,
                          output_field_names[2]:(row [output_field_names[2]] - min_2)/ range_2,
                          output_field_names[3]:(row [output_field_names[3]] - min_3)/ range_3,
                          output_field_names[4]:(row [output_field_names[4]] - min_4)/ range_4,
                          output_field_names[5]:(row [output_field_names[5]] - min_5)/ range_5,
                          output_field_names[6]:(row [output_field_names[6]] - min_6)/ range_6,
                          output_field_names[7]:(row [output_field_names[7]] - min_7)/ range_7,
                          output_field_names[8]:(Intlplan),
                          output_field_names[9]:(row [output_field_names[9]] - min_9)/ range_9,
                          output_field_names[10]:(row [output_field_names[10]] - min_10)/ range_10,
                          output_field_names[11]:(row [output_field_names[11]] - min_11)/ range_11,
                          output_field_names[12]:(Vmainlplan),
                          output_field_names[13]:str(churn)
            })
            

