#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Program 5 :- Mirrored Right Triangle Star Pattern
n = int(input())
for i in range(1, n+1):
    for j in range(n):
        if j >= (n-i) :
            print("* ", end = "")
        else:
            print("", end = "  ")
    print("\r")

