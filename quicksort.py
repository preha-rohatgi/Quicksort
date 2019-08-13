#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def quickSort(alist):
    quickSort1(alist,0,len(alist)-1)

def quickSort1(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSort1(alist,first,splitpoint-1)
        quickSort1(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            print(alist)
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    print(alist)

    return rightmark


# In[2]:


def median(array,alist):
    print(array)
    median=np.median(alist)
    print('median',median)
    small=100
    index=0
    start=0
    end=0
    for i in range(len(array)):
        if(abs(array[i]-median)<small):
            index=i
            small=abs(array[i]-median)
    print(array[index])
    if(array[index]==alist[0]):
        indexx=0
    elif(array[index]==alist[-1]):
        indexx=len(alist)-1
    else:
        indexx=int(len(alist)/2)
        
        
    
    return indexx


# In[3]:


def swap(indexx):
    temp=alist[indexx]
    alist[indexx]=alist[0]
    alist[0]=temp
    return alist 

    


# In[5]:


import random
import time
alist=[]
start=0
end=0
p=[]
print('chooose from the type of data required:')
print('1)Data generated randomly')
print('2)Data evenly balanced ')
print('3)Data unevenly balanced')
a=input()
if(a=='1'):
    for i in range(15):
        alist.append(random.randint(1,500))
    print(alist)
    print('pivot=',alist[0])
    time_start = time.clock()
    quickSort(alist)
    time_elapsed = (time.clock() - time_start)
    print(time_elapsed)
    print(alist)
    
    
elif(a=='2'):
    for i in range(15):
        alist.append(random.randint(1,50))
    print(alist)
    p.append(alist[0])
    p.append(alist[int(len(alist)/2)])
    p.append(alist[-1])
    indexx=median(p,alist)
    alist=swap(indexx)
    print('pivot=',alist[0])
    time_start = time.clock()
    quickSort(alist)
    time_elapsed = (time.clock() - time_start)
    print(alist)
    print(time_elapsed)

else:
    b=random.randint(1,100)
    for i in range(15):
        alist.append(i+b)
    print(alist)
    print('pivot=',alist[0])
    time_start = time.clock()
    quickSort(alist)
    time_elapsed = (time.clock() - time_start)
    print(time_elapsed)
    print(alist)
    
  
    


    
  
  
  
    
  


# In[ ]:





# In[ ]:




