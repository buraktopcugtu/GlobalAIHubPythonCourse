#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Method 1: Swapping two half of list with manual
dwarf_planets=([ "Pluto", "Eris", "Haumea", "Makemake", "Gonggong", "Quaoar", "Sedna","Orcus"])
print("Original list is:\n",dwarf_planets)
temp_list1=dwarf_planets[0:4]  # we assigned firt half of array to that list
temp_list2=dwarf_planets[4:8]  # we assigned second half of array to that list
dwarf_planets=temp_list2+temp_list1 # new list is second half+ firt half
print("Swapped list is:\n",dwarf_planets)


# In[ ]:


# Method 2: We can also write a simple function for that
def swap_array(list):
    n=len(list)
    if( n%2 == 0 ): # checking lenght of list is odd or even
        n1=int(n/2)
        temp_list2=list[0:(n1)]
        temp_list1=list[(n1):n]
        list=temp_list1+temp_list2
        print("Swapped list is:")   
        print(list)                   # will print swapped list
                                       # if we need to assign swapped list to a new list 
                                       # can change "print(list)" to "return (list)" 
    else:
        print ("Lenght of list non-suitable for swapping")


# In[104]:


# Function Test
dwarf_planets=([ "Pluto", "Eris", "Haumea", "Makemake", "Gonggong", "Quaoar", "Sedna","Orcus"])
print("Original list is:\n",dwarf_planets)
swap_array(dwarf_planets)
raw_input("Press any key for exit...")
