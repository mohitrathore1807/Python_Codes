#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Program 13 :- X pattern
n = int(input("Enter even integer "))
for i in range(1, n):
    for j in range(n):
        if j == i or j == (n-i):
            print("* ", end = "")
        else:
            print("",  end = "  ")
    print("\r")
            

