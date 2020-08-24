#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Program 4 :- Right Angle Triangle Star Pattern
n = int(input())
for i in range(n):
    for j in range(n):
        if j <= i :
            print("* ", end = "")
        else:
            print("", end = "  ")
    print("\r")

