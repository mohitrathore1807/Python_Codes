#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Program 15 :- Mirrored Rhombus
n = int(input())
for i in range(n):
    for j in range(n):
        if j < (n-i):
            print(end = " ")
    for k in range(n):
        print("* ", end = "")
    print("\r")

