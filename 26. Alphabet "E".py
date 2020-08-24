#!/usr/bin/env python
# coding: utf-8

# In[38]:


# Program 26 :- Alphabet "E"
for row in range(7):
    for col in range(5):
        if (col == 0 or row == 0 or row == 3 or row == 6):
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

