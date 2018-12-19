# -user can log in or continue as guest
# -screen populates with one required line for loan amount, optional interest rate
#and monthly payment amount
# -two optional lines with same information, button to add more lines
# -loans default to names by number, user can rename
# -user presses calculate button
# -sort loans from smallest to biggest
# -subtract monthly payment from all loans.
# -when smallest loan is gone, append number of months (loops) to month tracking
#list, roll over any surplus of the monthly payment to next smallest loan.
# -remove smallest loan from loan list
# -repeat until all loans are repaid.
# -add all integers in month tracking list
# -report to user how long it will take to pay off all loans under current payment
# -store original amounts in a sheet that user may access at anytime by logging in
#to track progress and maintain pace

## Debt Repayment App MVP will report back to user the input values and estimation
## of debt repayment completion.
## Ideal project reports the sheet and is pretty
## Dream project offers more strategies than just the snowball repayment method.

import math

##Defines everything required to accurately predict repayment time
class Loans:
    def __init__(self, name, amount, interest, monthly):
        self.name = loan
        self.amount = 0
        self.interest = 0
        self.monthly = 0

    def calculate(self):
        i = 0
        while int(amount) > 0:
            i +=1
            amount = (amount - monthly)
            amount = (amount * interest) + amount

        return i

userLoans = {}

## get user instance of Loans
userDone = False
while userDone == False:
    loanValues = []
    userName = input('Loan Name')
    loanValues.append(input('Amount of loan'))
    loanValues.append(input('Interest rate'))
    loanValues.append(input('Monthly payment'))
    userLoans[userName] = loanValues

## do math with the values in the dictionary--find out how this works, need to sort
##min-max and then do mathy math
    
    

