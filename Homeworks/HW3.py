#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Course Grade Application
# Key Points: I used nested dictionary for store student informations got from by user.
# After all infos is got and grade calculation complete,
# name and grade values transfered a list with for loop using of index feature.
# At final we sorted list with reverse=True parameter so highest grade is first index and
# least grade is last index.
# My code is flexible, student count/number can be determine by the user with some little changes,
# and studenttable could be create by for loop.


# In[ ]:


studenttable = {1: {'name': 'name', 'midterm': 'midterm', 'final': 'final','project': 'project','grade': 'grade'},
                2: {'name': 'name', 'midterm': 'midterm', 'final': 'final','project': 'project','grade': 'grade'},
                3: {'name': 'name', 'midterm': 'midterm', 'final': 'final','project': 'project','grade': 'grade'},
                4: {'name': 'name', 'midterm': 'midterm', 'final': 'final','project': 'project','grade': 'grade'},
                5: {'name': 'name', 'midterm': 'midterm', 'final': 'final','project': 'project','grade': 'grade'}}


# In[ ]:


# Notes of exam and homeworks must be in range [0-100],
# that function will verify that.
def getinput(text):
    verified_input=0
    while (verified_input==0):
        user_input=float(input(text))
        if user_input >= 0 and user_input <= 100:
            verified_input=1
            return user_input
        else:
            verified_input=0
            print("Enter a valid value:")


# In[ ]:


count=0
while count<5:
    count=count+1
    student_name=input("Enter name of the the student {}:\n".format(count))
    midterm=getinput("Enter midterm grade the of student {}:\n".format(count))
    project=getinput("Enter project grade the of student {}:\n".format(count))
    final=getinput("Enter final grade of the student {}:\n".format(count))
    passingGrade=(midterm*0.3)+(project*0.3)+(final*0.4)
    studenttable[count]['name']=student_name
    studenttable[count]['midterm']=midterm
    studenttable[count]['final']=final
    studenttable[count]['project']=project
    studenttable[count]['grade']=passingGrade


# In[ ]:


list=[]
count=0
while count < 5 :
    count=count+1
    list.append((studenttable[count]['grade'],studenttable[count]['name']))


# In[ ]:


list.sort(reverse=True)


# In[ ]:


print("List of grades is:")
print(list)
# Some float number precision's so long and that not looks good when printed list for prevent this
# we can use ""%.4g" %" transform during list.append function.
# but I don't used because that tranformation syntax varies between Python versions.
input("Press any key for exit...")
