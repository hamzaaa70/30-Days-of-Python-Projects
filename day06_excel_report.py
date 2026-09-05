from openpyxl import Workbook
from openpyxl.styles import Font

print("Company Sales Report Generator")

workbook = Workbook() #T create a new excel workbook

sheet = workbook.active #to get a active sheet
sheet.title = "Sales Report"


#Columns headings
sheet ["A1"] = "Emolyee"
sheet ["B1"] = "Product"
sheet ["C1"] = "Unites Sold"
sheet ["D1"] = "Price"
sheet ["E1"] = "Total Sales"

#makes heading bold
for cell in sheet[1]:
    cell.font = Font(bold=True)

#company sales data
sales_data = [
    ["UMER", "Laptop", 3,150000],
    ["wWISAL","IPHONE", 7,200000],
    ["DAWOOD","PISTOL",10,200093],
    ["HAMZA","BMW",5,210000020],
]

#add data to excel
row_number = 2
for sale in sales_data:

    employee = sale[0]
    product = sale[1]
    units = sale[2]
    price = sale[3]

    total = units * price

sheet.cell(row=row_number, column = 1 , value = employee)

# Add data to Excel
row_number = 2

for sale in sales_data:

    employee = sale[0]
    product = sale[1]
    units = sale[2]
    price = sale[3]

    total = units * price

    sheet.cell(row=row_number, column=1, value=employee)
    sheet.cell(row=row_number, column=2, value=product)
    sheet.cell(row=row_number, column=3, value=units)
    sheet.cell(row=row_number, column=4, value=price)
    sheet.cell(row=row_number, column=5, value=total)

    row_number = row_number + 1


# Save the Excel file
workbook.save("sales_report.xlsx")

print("Sales report created successfully!")