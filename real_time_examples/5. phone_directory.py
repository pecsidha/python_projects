# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:58:36 2020

@author: ReDI
"""

###########################################################################
##
##                            Phone List
##
###########################################################################

## Create a program to manage a list of phone-numbers.
## These numbers should be valid and stored in a dictionary

phone_numbers = {'Peter': '+49 1234567', 'Eva': '+49 9863456'}
possible_countries = {
    "germany": "+49",
    "france": "+33",
    "spain": "+34",
    "greece": "+30",
    "pakistan": "+92"
}

# Task 1: Ask the user to input:
# 1. Name
# 2. Phone prefix
# 3. Phone number




def valid_prefix(prefix):
    valid = False
    #print(valid)
    # TODO: check if prefix
    # 1. Starts with "+"
    # 2. Has two characters following the "+" sign (you only need to chek if the string has in total 3 characters)
    if len(prefix) == 3 and prefix[0] == '+':
        valid = True
            
    return valid


def valid_number(number):
    valid = True
    # TODO: check if number has 7 digits (you should check if all characters are valid numbers 0-9)
    valid_numbers = ['0','1','2','3','4','5','6','7','8','9']
    if len(number) == 7 :
        for i in number:
            if i not in valid_numbers:
                valid = False
                break
    else: 
        valid = False
        
    return valid

def check_country(country):
    
    if country in possible_countries:
        a = possible_countries[country] 
    else:
        print('Country not recognized')  
        a = 'error'
    return a


# Task 2: Check if the input prefix and number are valid, by using the functions above
# Hint: don't forget to call the functions



# Task 3: Add the COMPLETE number in phone_numbers and print phone_numbers
# The complete number should include the prefix, an empty space after it and the number
# Example: +49 9863456


# main code
user_name = ''
while True:
    user_name = input('Please enter your name: ').title()
    if user_name =='Stop':
        break

    #prefix = input('Enter the country code: ')
    #while valid_prefix(prefix)==False:
        #prefix = input('Enter the country code again(e.g +23): ')
    country = input('Enter country: ').lower() 
    prefix = check_country(country)
    if prefix == 'error':
        continue
        
    phone_number = input('Your phone number: ')     
    while valid_number(phone_number) == False:
        phone_number = input('Enter a valid 7 digit number: ') 

    
    complete_number = prefix +' '+ phone_number
    phone_numbers[user_name] = complete_number

    print(phone_numbers)



# Task 4: Store the current value of phone_numbers into a file called numbers.txt
# Hints:
#   1. don't forget to open the file using the rigth mode
#   2. To write phone_numbers as a string, you can use str(phone_numbers) and write the string in the file


number_file = open("numbers.txt",'w')
content = str(phone_numbers)
number_file.write(content)
number_file.close()


# Task 5: Change the program to run untill the input name is "STOP"
# The content of the file should be written after this





# Task 6: Change you code, and instead of asking the user to input the phone prefix difrectly, ask for the country
# Check if the country is available in possible_countries
# If it is, use the phone prefix provided (you can remove the step to validate prefix)
# If it is not, print an error message and start from the begining
