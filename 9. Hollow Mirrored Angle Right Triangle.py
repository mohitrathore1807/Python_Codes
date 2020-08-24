#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Program 9 :- Hollow Mirrored Angle Right Triangle Star Pattern
n = int(input())
for i in range(1, n):
    for j in range(1, n):
        if j == (n-1) or i == (n-1) or j == (n-i):
            print("* ", end = "")
        else:
            print("", end = "  ")
    print("\r")

