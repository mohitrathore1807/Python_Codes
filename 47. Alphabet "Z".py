#!/usr/bin/env python
# coding: utf-8

# In[59]:


# Program 47 :- Alphabet "Z"
for row in range(7):
    for col in range(7):
        if row == 0 or row == 6 or col == (6-row):
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

