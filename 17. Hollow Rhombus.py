#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Program 17 :- Hollow Rhombus
n = int(input())
for i in range(n):
    for j in range(n):
        if j < i:
            print(end = " ")
    for k in range(n):
        if i == 0 or i == (n-1) or k == 0 or k == (n-1):
            print("* ", end = "")
        else:
            print("", end = "  ")
    print("\r")

