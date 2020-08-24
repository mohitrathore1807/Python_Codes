#!/usr/bin/env python
# coding: utf-8

# In[41]:


# Program 29 :- Alphabet "H"
for row in range(7):
    for col in range(5):
        if (col == 0 or col == 4 or row == 3):
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

