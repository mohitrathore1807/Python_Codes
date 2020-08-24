#!/usr/bin/env python
# coding: utf-8

# In[58]:


# Program 46 :- Alphabet "Y"
for row in range(7):
    for col in range(7):
        if ((row == col  or col == (6-row)) and row < 4) or (col == 3 and row > 3):
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

