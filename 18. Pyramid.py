#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Program 18 :- Pyramid
n = int(input())
for i in range(n):
    for j in range(2*n+1):
        if j >= (n-i) and j <= (n+i):
            print("* ", end = "")
        else:
            print("",  end = "  ")
    print("\r")

