#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Program 11 :- Hollow Inverted Mirrored Right Angle Triangle Star Pattern
n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or j == (n-1) or i == j:
            print("* ", end = "")
        else:
            print("", end = "  ")
    print("\r")

