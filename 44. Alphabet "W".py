#!/usr/bin/env python
# coding: utf-8

# In[56]:


# Program 44 :- Alphabet "W"
i = 0
j = 3
for row in range(4):
    for col in range(7):
        if (col == 0 or col == 6) or (row == 1 and col == 4) or (row == 2 and col == 5) :
            print("*", end = "")
        elif row == i and col == j:
            print("*", end = "")
            i += 1
            j -= 1
        else:
            print(end =" ")
    print("\r")

