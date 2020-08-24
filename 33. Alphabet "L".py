#!/usr/bin/env python
# coding: utf-8

# In[45]:


# Program 33 :- Alphabet "L"
for row in range(7):
    for col in range(5):
        if col == 0  or row == 6:
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

