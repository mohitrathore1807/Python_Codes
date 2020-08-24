#!/usr/bin/env python
# coding: utf-8

# In[51]:


# Program 39 :- Alphabet "R"
for row in range(7):
    for col in range(7):
        if col == 0  or (col == 6 and row != 0 and row != 3 and row < 4) or ((row == 0 or row == 3) and col < 6) or row == col and row > 3:
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

