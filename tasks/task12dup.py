#countdown calculator
from datetime import  datetime

date1 = input("Enter the date 1 in DD/MM/YYYY format:\n")
date2 = input("Enter the date 2 in DD/MM/YYYY format:\n")


date1_split = datetime.strptime(date1,"%d/%m/%Y").date()
date2_split = datetime.strptime(date2,"%d/%m/%Y").date()

diff_date = abs(date1_split - date2_split).days



print(f"{diff_date} days")
