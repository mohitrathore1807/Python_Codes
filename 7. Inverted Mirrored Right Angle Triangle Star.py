#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Program 7 :- Inverted Mirrored Right Angle Triangle Star Pattern
n = int(input())
for i in range(n):
    for j in range(n):
        if j >= i:
            print("* ", end = "")
        else:
            print("", end = "  ")
    print("\r")

