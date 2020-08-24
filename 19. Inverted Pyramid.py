#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Program 19 :- Inverted Pyramid
n = int(input("Enter Odd integer "))
for i in range(n):
    for j in range(2*n + 1):
        if j < i:
            print(end = "  ")
    for k in range(2*n +1):
        if k < (n-i*2):
            print("* ", end = "")

    print("\r")

