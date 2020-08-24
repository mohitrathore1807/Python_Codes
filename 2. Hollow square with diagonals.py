#!/usr/bin/env python
# coding: utf-8

# In[2]:


#program 2:- Hollow square star pattern with diagonals
n = int(input())
for i in range(n+1):
    for j in range(n+1):
        if j == (n-i) or i == j or i == 0 or j == 0 or j == (n) or i == n:
            print('*', end = " ")
        else:
            print(" ", end = " ")
    print("\r")

