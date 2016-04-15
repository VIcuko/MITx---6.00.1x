'''
The following variables contain values as described below:

	balance - the outstanding balance on the credit card

	annualInterestRate - annual interest rate as a decimal

Monthly interest rate = 
	(Annual interest rate) / 12.0

Monthly payment lower bound = Balance / 12

Monthly payment upper bound = 
	(Balance x (1 + Monthly interest rate)^12) / 12.0

'''

AmountLeft=balance
MonthlyPayment=balance/12

while(AmountLeft>0):
    MonthlyPayment+=0.01
    AmountLeft=balance    
    for month in range(12):
        AmountLeft = (AmountLeft-MonthlyPayment)*(1+(annualInterestRate/12))
    
print "Lowest Payment: " + str(round(MonthlyPayment,2))