#!/usr/bin/env python
# coding: utf-8

# In[18]:


# 1. Login application with strings
username="eric"
password="cartman"
temp_username=input("Enter your username to login system: \n")
if temp_username==username:
    print("User founded.\n")
    temp_password=input("Enter your password: \n")
    if password == temp_password:
        print("Succesfully logged in the system.\n")
    else: 
        print("Password not matched with the user!")
else:
        print("User not found!")


# In[ ]:


# 2. login application with dictionary


# In[19]:


database={'eric': 'cartman', 'stan': 'marsh', 'kyle': 'colorado'}
temp_username=input("Enter your username to login system: \n")
if  temp_username in database:
    print("User founded in database.\n")
    password=database.get(temp_username)
    temp_password=input("Enter your password: \n")
    if password == temp_password:
        print("Succesfully logged in the system.\n")
    else: 
        print("Password not matched with user!")
else:
    print("User not found!")

input("Press any key for exit...")