#!/usr/bin/env python
# coding: utf-8

# In[60]:


# Program 48 :- Hollow Diamond
for row in range(7):
    for col in range(7):
        if row + col == 3 or col - row == 3 or row - col == 3 or row + col == 9:
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

