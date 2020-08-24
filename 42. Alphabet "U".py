#!/usr/bin/env python
# coding: utf-8

# In[54]:


# Program 42 :- Alphabet "U"
for row in range(7):
    for col in range(7):
        if (col == 0 or col == 6) and (row != 0 and row != 6) or ((row == 6) and (col > 0 and col < 6)):
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

