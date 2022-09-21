#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


def findMaximumSubArray(a,low,high):
    if low==high:
        return low,high,a[low]
    else:
        mid=math.floor((low+high)/2)
        leftLow,leftHigh,leftSum=findMaximumSubArray(a,low,mid)
        rightLow,rightHigh,rightSum=findMaximumSubArray(a,low,mid)
        crossLow,crossHigh,crossSum=findMaxCrossingSubArrray(a,low,mid,high)
        if (leftSum>crossSum and leftSum>rightSum):
            return leftLow,leftHigh,leftSum
        elif (rightSum>crossSum and rightSum>leftSum):
            return rightLow,rightHigh,rightSum
        else:
            return crossLow,crossHigh,crossSum


# In[3]:



def findMaxCrossingSubArrray(a,low,mid,high):
    leftSum=-math.inf
    sum=0
    for i in reversed(range(mid+1)):
        sum+=a[i]
        if (sum>leftSum):
            leftSum=sum
            maxLeft=i

    rightSum=-math.inf
    sum=0
    maxRight=mid+1
    for j in range(mid+1,high+1):
        sum+=a[j]
        if sum>rightSum:
            rightSum=sum
            maxRight=j

    return maxLeft,maxRight,(leftSum+rightSum)


# In[4]:


#First and last element are positive

a=[65,20,91,-56,28,83,74,-40,24,73,59,28,-30,35]
print('\nFirst and last elements are positive')
l,h,s=findMaximumSubArray(a,0,len(a)-1)
print('Starting index of MAXIMUM SUM ARRAY: ',l)
print('End index of MAXIMUM SUM ARRAY: ',h)
print('Sum of MAXIMUM SUM ARRAY: ',s)


# In[5]:


# Both First and last elemests are negative
a=[-65,20,91,-56,28,83,74,-40,24,73,59,28,-30,-35]
print('\nFirst and last elements are negative')
l,h,s=findMaximumSubArray(a,0,len(a)-1)
print('Starting index of MAXIMUM SUM ARRAY: ',l)
print('End index of MAXIMUM SUM ARRAY: ',h)
print('Sum of MAXIMUM SUM ARRAY: ',s)


# In[6]:


#First element is positive and last element is negative
a=[65,20,91,-56,28,83,74,-40,24,73,59,28,-30,-35]
print('\nFirst element is positive and last element is negative')
l,h,s=findMaximumSubArray(a,0,len(a)-1)
print('Starting index of MAXIMUM SUM ARRAY: ',l)
print('End index of MAXIMUM SUM ARRAY: ',h)
print('Sum of MAXIMUM SUM ARRAY: ',s)


# In[7]:


#First element is negative and last element is positive
a=[-65,20,91,-56,28,83,74,-40,24,73,59,28,-30,35]
print('\nFirst element is negative and last element is positive')
l,h,s=findMaximumSubArray(a,0,len(a)-1)
print('Starting index of MAXIMUM SUM ARRAY: ',l)
print('End index of MAXIMUM SUM ARRAY: ',h)
print('Sum of MAXIMUM SUM ARRAY: ',s)


# In[ ]:




