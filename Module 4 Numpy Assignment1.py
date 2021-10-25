#!/usr/bin/env python
# coding: utf-8

# # Module 4: Numpy Assignment

# # 1. Create a 3x3 matrix array with values ranging from 2 to 10.

# In[1]:


import numpy as np


# In[3]:


a=np.random.randint(2,10,(3,3))
print(a)


# # 2. Create a numpy array having user input values and convert the integer type to the float type of the elements of the array. For instance:
# Original array [1, 2, 3, 4] Array converted to a float type: [ 1. 2. 3. 4.]

# In[44]:


a=[1,2,3,4,5]
print("original arra:")
print(a)
x=np.asfarray(a)
print("Float type ofthe elements:")
print(x)


# In[ ]:





# # 3. Write a Numpy program to append values to the end of an array. For instance:
# Original array: [10, 20, 30] After append values to the end of the array: [10 20 30 40 50 60 70 80 90]

# In[45]:


x = [10, 20, 30]
print("Original array:")
print(x)
x = np.append(x, [40, 50, 60, 70, 80, 90])
print("After append values to the end of the array:")
print(x)


# # 4.Create two numpy arrays and add the elements of both the arrays and store the result in sumArray.

# In[32]:


ab=np.random.randint(2,10,(3,3))
print(ab)
bc=np.random.randint(2,10,(3,3))
print(bc)
sumArray=np.sum([ab,bc],axis=1)
print(sumArray)


# # 5. Create a 3*3 array having values from 10-90(interval of 10) and store that in array1. Perform the following tasks:
# a. Extract the 1st row from the array.
# b. Extract the last element from the array.

# In[66]:


intervalarr=np.arange(10,100,10).reshape(3,3)
print(intervalarr)
print("1st row:",intervalarr[0])
print("the last elemant:",intervalarr[2,2])


# In[ ]:





# In[ ]:




