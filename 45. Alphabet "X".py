#!/usr/bin/env python
# coding: utf-8

# In[57]:


# Program 45 :- Alphabet "X"
for row in range(7):
    for col in range(7):
        if row == col or col == (6-row):
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

