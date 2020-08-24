#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Program 14 :- Rhombus
n = int(input())
for i in range(n):
    for j in range(n):
        if j < i:
            print(end=" ")
    for k in range(n):
            print("* ", end = "")
    print("\r")

