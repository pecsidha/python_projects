# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 23:15:17 2020

@author: sidhartha kumar
"""
import matplotlib.pylab as plt
import csv
with open('retail_data.csv','r') as f:
    reader = csv.DictReader(f)
    retail_data = list(reader)
    
print()
total_lines = len(retail_data) # To check the total lines in the data
print('General Check : The total no of Entries in this data is',total_lines)

without_custmoerID_entries = 0
total_invoice = 0
user_input = input('To check list of Unique Items based on Invoice number , Please enter the invoice number?:')
for i in retail_data:
    if i["InvoiceNo"] == user_input: # Gerneral Check : To count the no. of invoices for user query
        total_invoice = total_invoice+1
    if i["CustomerID"] == '':
        without_custmoerID_entries += 1 # General Check : To count the no. of blank spaces in customer ID column
print()    
print('General Check : The total number of Unique Items for', user_input, 'is', total_invoice)
# print()
print('General Check : There are',without_custmoerID_entries,'invoices WITHOUT customer IDs')

transaction_details = []
wooden_products=[]
total_wooden_products_purchased = 0
total_quantity = 0
total_cost = 0
total_money_spent = 0
product_purchased = []
unique_products_purchased = {}
transaction_query = input('Please enter the customer ID for transaction you need?:')

for i in retail_data:
    if i["CustomerID"] == transaction_query: # To query which cusomer ID to see details
        total_quantity += int(i["Quantity"]) # To count the total quantity purchased to the cusomer ID
        total_money_spent += int(i["Quantity"])* float(i["UnitPrice"]) # To count the total quantity purchased to the cusomer ID
        product_purchased.append(i["StockCode"]) # To save in list all the products purchased by stockcode what customer purchased
        
        if 'WOODEN' in i["Description"]: # Check for WOODEN description in the description coulumn
            wooden_products.append(i["Description"])
            total_wooden_products_purchased += 1 # count the total number of WOODEN products purchased
            total_cost += int(i["Quantity"])* float(i["UnitPrice"]) # to find total money spent on WOODEN products
            
for i in product_purchased:
    # Make a key value pair for the products purchased ie. keys will be stock code and value is no of occurances
    if i not in unique_products_purchased.keys(): 
        unique_products_purchased[i] = 1
    else:
        unique_products_purchased[i] = unique_products_purchased[i]+1

print('The total quanity of products purchased by customer ID',transaction_query,'is:' ,total_quantity)
print()
print('The total money spent by customer ID',transaction_query,'is:' ,'%.2f'%total_money_spent)
print()
print('The list of product purchased by customer ID',transaction_query,' is: ',unique_products_purchased)
print()

print('The total WOODEN products purchased by customer ID',transaction_query,' is: ',total_wooden_products_purchased)

print()

print('The total money spent on WOODEN products by customer ID',transaction_query,' is: ','%.2f'%total_cost)
        
print()

'''
# Plotting the key value pair of unique product purchased. 'keys' will be stock code and 'value' is no of occurances
lists = sorted(unique_products_purchased.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples

plt.plot(x, y)
plt.show()

'''
########Additional#######################################################
######To check the Customer vs frequency (number of purchases)###########
'''
all_customer = []
no_customer_invoice = []
no_custmoerID_entries = 0
most_purchase = {}
for i in retail_data:
  if i["CustomerID"] == '':
    no_customer_invoice.append(i["CustomerID"])
    no_custmoerID_entries += 1
  else:
    all_customer.append(i["CustomerID"])
    
for i in all_customer:
    if i not in most_purchase.keys():
        most_purchase[i] = 1
    else:
        most_purchase[i] = most_purchase[i]+1
        
print()
# print('The customer general purchase volume:',most_purchase)
print()

lists = sorted(most_purchase.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples

plt.plot(x, y)
plt.show()
#################################Additional#############################
'''