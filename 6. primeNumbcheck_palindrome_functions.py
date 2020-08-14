# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:35:50 2020

@author: sidhartha kumar
"""
####################Excercise 1###################################################
# def stat(a):
#     print(f'The list is {a}')
#     print(f'The maximum value is {max(a)}')
#     print(f'The miminum value is {min(a)}')
#     print(f'The total sum is {sum(a)}')
#     print(f'The length is {len(a)}')
#     print(f'The mean value is {"%.2f"%(sum(a)/len(a))}')
#     print()
    
# stat([10,14,25,9,11,7])

# stat([26,22,44,9,10,1])
######Excercise 2 (takes a list of numbers and outputs only even numbers########
def even_element(b):
    even_list=[]
    for i in b:
        if i%2==0:
            even_list.append(i)
    print(even_list)
even_list=even_element([10,14,25,9,11,7,18,55,98])
even_list=even_element([3,4,5,6,7,11,12,13,14])

##########################Excercise 3############################################
def list_benifits():
    list =["More organised code","More readable code","Easier code re-use","Allowing programmers to share and connect code together"]
    return list
result = list_benifits()
print(result)

def build_sentence(str1,str2=" is a benefit of functions!"):
    full_sentence = str1 + str2
    return full_sentence
sentence_1=build_sentence("Avoiding Duplication")
print(sentence_1)

def name_the_benefits_of_functions():
    list_of_benifits = list_benifits()
    for benifit in list_of_benifits:
        print(build_sentence(benifit))
name_the_benefits_of_functions()
#############################Excercise 4 (prime number Check)#########################################
def prime_check(number):
    if number > 1:
        for i in range(2, number): # numbers are taken from 2 to the inputed number -1
            if (number % i) == 0: # Each number divided by i
                print(number, "is not a prime number_1")
                return
        else:
            print(number, "is a prime number")
    
    # if the entered number is less than or equal to 1
    # then it is not prime number
    else:
        print(number, "is not a prime number")
prime_check(5)
#########Excercise 5 (Plaindrome check)########################################
word = str(input('Please enter a word: ')).lower().replace(" ","")
def check_pal(new_word):
    if new_word=="":
        return
    for i in range(len(new_word)):
        if new_word[i] != new_word[(-1-i)]: # every index of the word is checked to last index
            print(word, 'is NOT Palindrome!')
            return
    print(word,'is Palindrome')
check_pal(word)
######################################################################
def func1(n):
    total=0
    total = n*n-1
    print(total)
    # for i in n:
    #     total=n*n-1
        # print(total)
func1(4)  