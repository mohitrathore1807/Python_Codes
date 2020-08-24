#!/usr/bin/env python
# coding: utf-8

# In[30]:


# Program 20 :- Hollow Pyramid
n = int(input())
for i in range(n):
    for j in range(1,2*n):
        if j == (n+i) or j == (n-i) or i == (n-1):
            print("* ", end = "")
        else:
            print("",  end = "  ")
    print("\r")

