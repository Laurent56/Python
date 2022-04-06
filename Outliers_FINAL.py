#!/usr/bin/env python
# coding: utf-8

# In[38]:


# Need this for median() function
import statistics

# My first attempt at implementing IQR Outliers in Python
# I am mimicing the data and results on this YouTube presentation: 
# https://youtu.be/STSP8gTSdT8
# This example the quartiles are four equal parts: Q1 at0.25, Q2 at 0.5, and Q3 0.75
# At Collibra DQ we allow for the user to adjust the Q1 and Q3 location (long discussion)

# We need a Dataset first:
# The _No_Outliers_ in the Dataset dataset is this:
# unordered_data = [5, 8, 15, 26, 10, 18, 3, 12, 6, 14, 11]

# The _There_Are_Outliers_ in the Dataset dataset is this:
unordered_data = [11, 31, 21, 19, 8, 54, 35, 26, 23, 13, 29, 17]

# Order this list from lowest to highest values:
ordered_data = sorted(unordered_data)

# print(ordered_data) that works

# Need to identify the "median" of the entire dataset.
# Q2 is the median of the dataset.

Q2 = statistics.median(ordered_data)

# We need the median of the lower half of the dataset (not inlcuding the Q2 value )
# We need first half of the ordered_data without the Q2.

# Find the median value index
print('Q2 = ', Q2)
print('all data', ordered_data)

# In the second set of data there is no median value in the data, it has to be computed
# So this old indexing code doesn't work


# in an odd mumber of elements in a list, the median is found
# if length / 2 has a remainder it is odd number of elements
# if length / 2 has no remainder it is even number of elements
# Need to treat even and odd number of values differently for this to work
# In an even number of elements in a list, the median is computed
# Index starts at 0 for a List (for half of the dataset, index should be 5 if the length is 12)

# ODD: 
if len(ordered_data) % 2 > 0:
    print('Odd number of elements found...\n')
    index = ordered_data.index(Q2)
    print('index of Q2 =', index)
    #first half of dataset:
    first = ordered_data[:index]
    second = ordered_data[(index +1):]
# EVEN:
else:
    print('Even number of elements found...\n')
    length_of_dataset = len(ordered_data)
    index = int(length_of_dataset / 2)
    print('even index first half ends at =', index)
    first = ordered_data[:index]
    second = ordered_data[(index):]

Q1 = statistics.median(first)
print('Q1 = ', Q1)

print('first half', first) 
print('second half', second)

Q3 = statistics.median(second)
print('Q3 = ', Q3)

# Interquartile Range is the Q3 - Q1
IQR = Q3 - Q1
print('IQR value = ', IQR)

# Next we search for an Outlier in the dataset using an IQR based formula:
# We create a range of values, within which a number is NOT an outlier, outside if which
# It will be called an Outlier:
# Formula is: [Q1 - (1.5 x IQR), Q3 + (1.5 x IQR)]

not_outliers = [(Q1 - 1.5 * IQR),(Q3 + 1.5 * IQR)]
print('Within this range of values are NOT outliers [low, high]:', not_outliers)

# Check for outliers in the given dataset
for value in ordered_data:
    foundOutlier = False
    #low_check
    if value < not_outliers[0]:
        print('I just found a low Outlier!:', value)
        foundOutlier = True
    elif value > not_outliers[1]:
        print('I just found a high Outlier!:', value)
        foundOutlier = True

if (foundOutlier):
    print('I did find at least one Outlier today, Woo hoo!!')
else:
    print('I dont see any outliers in this Dataset...')

# Done


# In[ ]:




