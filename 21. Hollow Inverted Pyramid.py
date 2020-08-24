#!/usr/bin/env python
# coding: utf-8

# In[32]:


# Program 21 :- Hollow Inverted Pyramid
n = int(input())
for i in range(n+1):
    for j in range(2*n+1):
        if i == 0 or j == i or j == (2*n - i):
            print("* ", end = "")
        else:
            print("",  end = "  ")
    print("\r")

