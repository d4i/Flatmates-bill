from flat import Bill, Flatmate
from report import PdfReport

bill_amount = float(input("Enter the total bill amount: "))
period = input("Enter the period (eg. August 2024): ")

name1 = input("Enter your name: ")
name2 = input("Enter flatmate's name: ")

days_1 = int(input(f"Enter the number of days {name1} was in the flat: "))
days_2 = int(input(f"Enter the number of days {name2} was in the flat: "))

the_bill = Bill(bill_amount, period)
flatmate1 = Flatmate(name1, days_1)
flatmate2 = Flatmate(name2, days_2)

print(f'{flatmate1.name} has to pay: ', flatmate1.pays(the_bill, flatmate2))
print(f'{flatmate2.name} has to pay: ', flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generates(flatmate1, flatmate2, the_bill)

