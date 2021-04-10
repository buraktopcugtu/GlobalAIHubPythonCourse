#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Knowledge Competition Application
# Methodology and Structure of Program: 
# Questions and it's answers stored in nested dictionary,
# response options shown to the user stored in nested list.
# User must be type his answer with paying attention to lower/upper letters and spaces.
# I wrote functions for asking question, checking anwer, get input from user and calculate total point and true answers.
# This way the code is becomes very simple and effective,
# if we wouldn't use functions need to use and repeat print/get input/check answer operations with if/else statements.


# In[ ]:


question_table= {1: {'question': 'Who is the leading actor in the "The Last Castle" movie?', 'answer': 'Robert Redford'},
                 2: {'question': 'Who is the director of the Alien movie?', 'answer': 'Ridley Scott'},
                 3: {'question': 'Which of the following films has Uma Thurman not starred in?', 'answer': 'Training Day'},
                 4: {'question': 'What is the role of Tom Cruise in "A Few Good Men" movie?','answer': 'Lawyer'},
                 5: {'question': 'Which of the following films has Jessica Alba starred in?', 'answer': 'The Eye'},
                 6: {'question': 'Which of the following films has Kurt Russell starred in?', 'answer': 'The Thing'},
                 7: {'question': 'Which of the following films directed by John Carpenter?', 'answer': 'Ghosts of Mars'},
                 8: {'question': 'Which of the following films directed by Kathryn Bigelow?', 'answer': 'Blue Steel'},
                 9: {'question': 'What is the star of "The Hunt for Red October" film?', 'answer': 'Sean Connery'},
                10: {'question': 'Which of the following films has Keanu Reeves starred in?', 'answer': 'Point Break'}}


# In[ ]:


choices_list=[['- Robert Redford','- Denzel Washington'],['- Tony Scott','- Ridley Scott']
             ,['- Gattaca','- Training Day'],['- Lawyer','- Pilot'],['- Jurassic Park','- The Eye']
             ,['- Jaws','- The Thing'] ,['- Ghosts of Mars','- Armageddon'] ,['- Dark Blue','- Blue Steel']
              ,['- Sean Connery','- Pierce Brosnan'] ,['- From Paris with Love','- Point Break']]


# In[ ]:


def ask_question(number):
    question=question_table[number]['question']
    choices=choices_list[number-1]
    print("{}. {}\n{} \n".format(number,question, " ".join(choices)))
def check_answer(answer,number):
    true_answer=question_table[number]['answer']
    if user_answer==true_answer:
        return 1
    else:
        return 0
def getinput():
    user_input=str(input("Enter your answer:"))
    return user_input
def result(count):
    total_point=count*10
    if count>5:
        print("You have succeeded by answering {} questions correctly.".format(count))
        print("Your total point is:",total_point)
    else:
        print("You have failed by answering only {} questions correctly.".format(count))
        print("Your total point is: {}".format(total_point))


# In[ ]:


true_count, num=0,0
while(num<10):
    num=num+1
    ask_question(num)
    user_answer=getinput()
    true_count=check_answer(user_answer,num)+true_count
result(true_count)
input("Press any key for exit...")
