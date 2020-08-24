#!/usr/bin/env python
# coding: utf-8

# In[40]:


# Program 28 :- Alphabet "G"
for row in range(7):
    for col in range(5):
        if (col == 0 or (col == 4 and (row != 1 and row != 2)) or row == 0 or row == 6) or (row == 3 and col > 2):
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

