#!/usr/bin/env python
# coding: utf-8

# In[53]:


# Program 41 :- Alphabet "T"
for row in range(7):
    for col in range(7):
        if (row == 0 or col == 3):
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

