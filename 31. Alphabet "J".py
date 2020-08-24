#!/usr/bin/env python
# coding: utf-8

# In[43]:


# Program 31 :- Alphabet "J"
for row in range(7):
    for col in range(5):
        if col == 2 or (col == 0 and row > 4 )or (row == 0 or (row == 6 and col < 3) ):
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

