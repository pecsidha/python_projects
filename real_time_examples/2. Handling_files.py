# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:06:05 2020

@author: sidhartha kumar
"""

'''
# exercise 1 - Solution
# Since I want to write and not override on the file i choose to open it with mode "a"
f = open('exercise1.txt','a')

# since we have a defined numner of iterations we use for 
for i in range(3):
  user_input = input('Please enter you text:')
  f.write(user_input + "\n")

f.close()
'''
'''
# exercise 2 - Solution

#Since I want to only read the file I can open it with mode "r"
my_file = open("My_File.txt", "r")

count_lines = 0
count_char = 0

while True: 
  # take the content of each line without the "\n"
  content = my_file.readline().strip()

  # ALWAYS check if it is the end of the file before doing anything else!!
  if content == "":
    break
  # count the lines of the file
  count_lines += 1
  # count number 4
  if content == '4':
    count_char += 1
 
my_file.close()
# now you have read the file and calculate what it is needed therefore you can print them
print("Number of lines: ", count_lines)
print("Times that I counted number 4: ", count_char)
'''
'''
#Exercise 3 - Solution

file1 = open("File1.txt","r")
file2 = open("File2.txt","r")

while True:
  # take the content of the line and remove "\n"
  content1 = file1.readline().strip()
  content2 = file2.readline().strip()
  # ALWAYS check if it is the end of the file before doing anything else!!
  #(at this point the optimal solution is to check the length of the two files if it is the same:len(file1.readlines()) == len(file2.readlines()))
  if content1 == "" and content2 == "":
    break

  # end = " " removes the new line on print function, so all are printed in one line
  print(content1 + " " + content2, end =" ")

file1.close()
file2.close()
'''


# Exercise 4 - Solution

products = []
count = 0
cheapest_price = 100
cheapest_product = ""

most_expensive_price = 0
most_expensive_product = ""

total_num_items = 0
total_cost = 0

csvfile = open('Shopping_list.csv', 'r')

while True:
  content = csvfile.readline().strip()
  
  # ALWAYS check if it is the end of the file before doing anything else!
  if content == "":
    break
  # elements are seperated with "," since we have a csv file. THerefore, we have to remove comma and take each element seperately
  element = content.split(',')
  count +=1
  # the first line should be omitted
  if count == 1:
    continue
  # element[0] -> products
  products.append(element[0])
  items = int(element[1])
  total_num_items += items
  price = float(element[2])
  total_cost += price
  # I want to find the cheapest product and the most expensive one
  # find the price of each product
  price_per_item = price / items

  if price_per_item < cheapest_price:
    # I found a cheaper price, store the price and the responding product
    cheapest_price = price_per_item
    cheapest_product = element[0]

  if price_per_item > most_expensive_price:
    # I found a more expensive price, store the price and the responding product
    most_expensive_price = price_per_item
    most_expensive_product = element[0]

csvfile.close()

# print all products
print("Products bought: ", products)

# print total amount of money
print("Money spent: ",  total_cost)

# total amount of items
print("Items bought in total: ", total_num_items)


# the most expensive product
print("The most expensive product is: ", most_expensive_product, "and its price is: ", most_expensive_price)

# the cheapest product
print("The cheapest product is: ", cheapest_product, "and its price is: ", cheapest_price)

'''