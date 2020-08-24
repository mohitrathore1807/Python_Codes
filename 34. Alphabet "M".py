#!/usr/bin/env python
# coding: utf-8

# In[46]:


# Program 34 :- Alphabet "M"
for row in range(7):
    for col in range(7):
        if (col == 0  or col == 6) or (row == col and row < 4) or (col == (6 - row ) and row < 4):
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

