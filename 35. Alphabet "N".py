#!/usr/bin/env python
# coding: utf-8

# In[47]:


# Program 35 :- Alphabet "N"
for row in range(7):
    for col in range(7):
        if col == 0  or col == 6 or row == col:
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

