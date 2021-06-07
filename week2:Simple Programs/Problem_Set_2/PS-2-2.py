''' Problem 2 - Paying Debt Off in a Year
15.0/15.0 points (graded)

Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180

Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

'''

balance = 320000
annualInterestRate = 0.2
#calcuates annual interest rate
monthlyIntRate = annualInterestRate/12
initBalance = balance

#Minimum fixed monthly payment
monthPay = 106
while balance > 0:
    for month in range(12):
        #cacluates monthly unpaid balance
        balance = balance - monthPay
        #calcuates updated balance each month
        balance = balance + (monthlyIntRate*balance)
    if balance > 0:
        monthPay += 10
        #reset balance
        balance = initBalance
    elif balance <= 0:
        break


print(monthPay)