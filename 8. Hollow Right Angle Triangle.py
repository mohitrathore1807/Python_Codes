#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Program 8 :- Hollow Right Angle Triangle Star Pattern
n = int(input())
for i in range(n):
    for j in range(n):
        if j == 0 or i == j or i == (n-1) :
            print("* ", end = "")
        else:
            print("", end = "  ")
    print("\r")

