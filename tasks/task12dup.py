#countdown calculator
from datetime import  datetime
from dateutil import relativedelta



date1 = input("Enter the date 1 in DD/MM/YYYY format:\n")
date2 = input("Enter the date 2 in DD/MM/YYYY format:\n")

try:
    date1_split = datetime.strptime(date1,"%d/%m/%Y").date()
    date2_split = datetime.strptime(date2,"%d/%m/%Y").date()
    diff_date = relativedelta.relativedelta(date1_split,date2_split)
    print(f"{diff_date.days} days, {diff_date.months} months, {diff_date.years} years")
except Exception as e:
    print("Invalid date format\n")







