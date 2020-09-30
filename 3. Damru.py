#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Program 3 :- Damru
n = int(input('PLEASE ENTER THE SIZE : ))
for i in range(n+1):
    for j in range(n+1):
        if j <= i and j >= (n-i) or j >= i and j <= (n-i) and j <= n:
            print("* ", end = "")
        else:
            print("", end = "  ")
    print("\r")

