#!/usr/bin/env python
# coding: utf-8

# In[50]:


# Program 38 :- Alphabet "Q"
for row in range(7):
    for col in range(7):
        if (col == 0 or col == 6) and (row != 0 and row != 5 and row != 6) or ((row == 0 or row == 5) and (col > 0 and (col < 6) or row == 6 and col == 5) or (row == 6 and col == 5) or (row == 4 and col == 2)):
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

