Title: Flatmates bill
Description: An app that gets as the input amount of bill for a particular period and the days
that each of the flatmates stayed in the house for that period and
returns how much each flatmate has to pay. It also generates a pdf report stating the
names of the flatmates, the period, and how much each of them had to pay.
Objects:

Bill:
    amount
    period
Flatmates
    name
    number_of_days_in_house
    pays(bill)
PdfReport:
    Filename
    generates(flatmate1, flatmate2, bill)
