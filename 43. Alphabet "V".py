#!/usr/bin/env python
# coding: utf-8

# In[55]:


# Program 43 :- Alphabet "V"
for row in range(4):
    for col in range(8):
        if row == col or col == (6 - row):
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

