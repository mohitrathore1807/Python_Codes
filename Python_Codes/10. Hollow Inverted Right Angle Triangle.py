#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Program 10 :- Hollow Inverted Right Angle Triangle Star Pattern
n = int(input())
for i in range(n+1):
    for j in range(n+1):
        if j == 0 or i == 0 or j == (n-i):
            print("* ", end = "")
        else:
            print("", end = "  ")
    print("\r")

