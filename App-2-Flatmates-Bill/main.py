from flat import Bill, Flatmate
from report import PdfReport, FileSharer

amount = float(input("Hey user, enter the bill amount: "))
period = input("Enter the period of bill ? E.g March 2024:")

name1 = input("Enter the first person's name: ")
days_in_house1 = int(input("How many did {name1} stay in the house ?: "))
name2 = input("Enter the second person's name: ")
days_in_house2 = int(input("How many did {name2} stay in the house ?: "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1} pays:", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2} pays:", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename="{the_bill.period}.pdf")
pdf_report.generate(flatmate1,flatmate2,the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())