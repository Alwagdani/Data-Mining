######################
## H4_Hanan_Alwagdani_ACSG-555-01-2018F
## Date:10/01/2018
## File: C:\Users\Hanan\Desktop\H4_Hanan_Alwagdani_ACSG-555-01-2018
######################

import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat

#to read data from file "cars.csv"
df = pd.read_csv("cars.csv") 

# to find the mean of the column weightIbs
mean = stat.mean(df['weightlbs'])

# to finf Standerd deviation of the column weightIbs 
stdev = stat.stdev(df['weightlbs'])

# to find Z-score of the column weightIbs
zscore_weightlbs = ( df['weightlbs'] - mean )/stdev

#number of bins to use
num_bins = 36

# Create histohram and chosse bins and color
# Add title and axis names
plt.hist(zscore_weightlbs, num_bins, color="#86bf91")
plt.title("Histogram of Z-score of Weight")
plt.ylabel("Counts")
plt.xlabel("Z-score of weightlbs")

plt.show()
