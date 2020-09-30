#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Program 5 :- Mirrored Right Triangle Star Pattern
n = int(input("PLEASE ENTER THE NUMBERS OF ROWS YOU WANT : "))
for i in range(1, n+1):
    for j in range(n):
        if j >= (n-i) :
            print("* ", end = "")
        else:
            print("PLEASE ENTER ANY DIGITS")
            print("", end = "  ")
    print("\r")
print('Thank you')

