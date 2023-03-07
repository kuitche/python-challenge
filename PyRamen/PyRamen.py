# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')
metrics_filepath = Path('sales_metrics.txt') # for writing output file

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath,'r') as menufile:
    menureader = csv.reader(menufile,delimiter=',')
    menu_header = next(menureader)
    for row in menureader:
        menu.append(row)
menufile.close()
# print(menu)



# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as salesfile:
    salesreader = csv.reader(salesfile, delimiter=",")
    sales_header = next(salesreader)
    for s in salesreader:
        sales.append(s)
salesfile.close()
#print(sales)



# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for sale_row in sales:



    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    line_item_id = sale_row[0]
    date = sale_row[1]
    credit_card_number = sale_row[2]
    quantity = int(sale_row[3])
    sale_item = sale_row[4]
    valid_sale_item = False # Flag to check if the sale item is in the menu. Initially assume false


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if sale_item not in report:
        report[sale_item] = {"01-count": 0, "02-revenue": 0,"03-cogs": 0, "04-profit": 0}


    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for menu_record in menu:


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        menu_item = menu_record[0]
        category = menu_record[1]
        description = menu_record[2]
        price = float(menu_record[3])
        cost = float(menu_record[4])


        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if menu_item == sale_item:
            valid_sale_item = True # set the valid flag to True 
            menu_profit = quantity * profit


            # @TODO: Print out matching menu data
            # print(report[sale_item])


            # @TODO: Cumulatively add up the metrics for each item key
            report[sale_item]["01-count"] += quantity
            report[sale_item]["02-revenue"] += quantity * price
            report[sale_item]["03-cogs"] += quantity * cost
            report[menu_item]["04-profit"] += menu_profit

        # @TODO: Else, the sales item does not equal any of the item in the menu data, therefore no match
  
    # @TODO: Increment the row counter by 1
    if valid_sale_item == False:
        print(f"{sale_item} does not equal {menu_item}! NO MATCH!")


# @TODO: Print total number of records in sales data
print(f"total number of records in sales data: {len(report)}")
print()

# @TODO: Write out report to a text file (won't appear on the command line output)
metrics_filepath.touch()
with open(metrics_filepath, 'a') as reportfile:
    for key in report:
        reportfile.write(f"{key} {report[key]}")
reportfile.close()
    