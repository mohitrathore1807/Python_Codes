#!/usr/bin/env python
# coding: utf-8

# In[39]:


# Program 27 :- Alphabet "F"
for row in range(7):
    for col in range(5):
        if (col == 0 or row == 0 or row == 3):
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

