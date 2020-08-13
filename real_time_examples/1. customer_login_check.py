# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:29:23 2020

@author: sidhartha kumar
"""
a = {'ahmed':'apple','yong':'cat','sudhir':'dog','julie':'mouse'}
block_user=[]
correct = True
while correct:
  user_name = str(input('Enter your name:')).lower()
  if user_name in a:
    print('Welcome')
    for i in range(3,0,-1):
      password=input('Enter your password:').lower()
      if password==a[user_name]:
        print('You are authorised',user_name.upper())
        print('Thank you !!!')
        break
      else:
        print('INVALID password!!')
      if i==1:
        print('Maximum Attempts reached,ACCESS DENIED!! and BLOCKED!!')
        block_user.append(user_name)
        print(block_user)
    #else:
    #  break

  else:
    print('Sorry, Your Name not found')
    new_regist=str(input('Do you want to register? y/n:')).lower()
    if new_regist=="y":
      new_customer=str(input('Choose your name:')).lower()
      #for i in range (2,0,-1):
      new_pass = str(input('Choose your password:')).lower()
      new_pass1 = str(input('Re-Enter your password:')).lower()
      if new_pass==new_pass1:
        print('Password saved')
        a[new_customer]=new_pass
        print('Thank you !!You are now added to database')
        #break
      else:
        print('Password do not match - EXITING')
    else:
      print('Thank you bye')  