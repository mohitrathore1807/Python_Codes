#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Program 6 :- Inverted Right Angle Triangle Star Pattern
n = int(input())
for i in range(n):
    for j in range(n):
        if j < (n-i):
            print("* ", end = "")
        else:
            print("", end = "  ")
    print("\r")

