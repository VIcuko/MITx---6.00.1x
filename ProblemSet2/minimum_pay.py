'''
Write a program to calculate the credit card balance after 
one year if a person only pays the minimum monthly payment 
required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal


Monthly interest rate= (Annual interest rate) / 12.0

Minimum monthly payment = 
	(Minimum monthly payment rate) x (Previous balance)

Monthly unpaid balance = 
	(Previous balance) - (Minimum monthly payment)

Updated balance each month = 
(Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

'''


CurrentBalance=balance
Total=0
for month in range(1,13):
    MonthlyPayment = CurrentBalance*monthlyPaymentRate
    Total+=MonthlyPayment
    RemainingBalance = (CurrentBalance-MonthlyPayment)*(1+(annualInterestRate/12))
    CurrentBalance=RemainingBalance
    print "Month: " + str(month)
    print "Minimum monthly payment: " + str(round(MonthlyPayment,2))
    print "Remaining balance: "+ str(round(RemainingBalance,2))
print "Total paid: "+str(round(Total,2))
print "Remaining balance: "+str(round(RemainingBalance,2))
