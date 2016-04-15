'''
Now write a program that calculates the minimum fixed monthly 
payment needed in order pay off a credit card balance within 
12 months. By a fixed monthly payment, we mean a single number 
which does not change each month, but instead is a constant 
amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly 
payment rate.

The following variables contain values as described below:

	balance - the outstanding balance on the credit card

	annualInterestRate - annual interest rate as a decimal

Monthly interest rate = 
	(Annual interest rate) / 12.0

Monthly unpaid balance = 
	(Previous balance) - (Minimum fixed monthly payment)

Updated balance each month = 
	(Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

'''

AmountLeft=balance
MonthlyPayment=-10
while(AmountLeft>0):
    MonthlyPayment+=10
    AmountLeft=balance    
    for month in range(12):
        AmountLeft = (AmountLeft-MonthlyPayment)*(1+(annualInterestRate/12))
print "Lowest Payment: " + str(MonthlyPayment)
