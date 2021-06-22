#!/usr/bin/env python3
#Time Value of Money by KBowen

import locale
def getChoice():
    #use boolean for loop control
    goodVal = False;
    while not goodVal:
        try:
            c = int(input("Select oporation: 1=PV, 2=FV, 3=FV-Annuity, 0=Quit: "))
            if c <0 or c > 3:
                #oob
                print("Illegal value, please enter 1, 2, 3, or 0.")
                goodVal = False
            else:
                #correct choice
                goodVal = True
        except ValueError:
            print("Illegal value, please enter 1, 2, 3, or 0.")
            goodVal = False
    return c

def getValue(prompt):
#G2G
    try:
        v = float(input(prompt))
        if v <=0:
            print("Illegal value.  Positive numbers only please.")
        else:
            return v
    except ValueError:
        print("Illegal value.  Positive numbers only please.")
        getValue(prompt)

        
def getTerm(prompt):
    #G2G
    #xt cdt - merge v and t (use get value to return float or int)
    #goodVal = False;
    #while not goodVal:
        try:
            t = int(input(prompt))
            if t <=0:
                print("Term must be a positive number.")
                getTerm(prompt)
            else:
                return t
        except ValueError:
            print("Illegal value.  Positive numbers only please")
            getTerm(prompt)

def doFVA():
    deposit = getValue("Monthly Deposit: ")
    #rate must be >0 but <= 25%
    rate = getValue("Annual interest rate (6.5% = 6.5: ")
    while rate > 25.0:
        print("Rate is astronomical.  Try again.")
        rate = getValue("Annual interest rate (6.5% = 6.5: ")
    term=getTerm("Enter term (in months): ")
    fva = 0.0
    morate = rate/12.0/100.0
    for i in range(0,term):
        intearn = (fva + deposit) * morate
        fva += deposit + intearn
    
    print("A monthly deposit of %s " % locale.currency(deposit,grouping=True)
          + "earning "
          + "{:.3%}".format(rate/100.0) + " annually after "
          + str(term) + " months will have a final value of: "
          + locale.currency(fva,grouping=True))
    print("That includes interest earned of %s "
          % locale.currency( (fva - (deposit*term) ),grouping=True))
                        
def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL,'en_US')
        
    print("Welcome to the finincial calculator")

    choice = getChoice()
    while choice !=0:
        #get data and do calc
        print("Your choice was: " + str(choice))
        if choice ==1:
            #PV logic
            print("Present Value")
            print("Amount to be received: ")
            deposit = getValue
        elif choice ==2:
            #FV logic
            print("Future Value")
        elif choice ==3:
            #FV annuity logic
            print("Future Value with an annuity")
            doFVA()
            #print("Your deposit was %s " % locale.currency(deposit,grouping=True))
            
        else:
            print("Unknown operation.")
        
        #ask for next op or quit
        choice = getChoice()
        print()
        
    print("Thank you for using the calculator")

#launch program based on env pariable name
if __name__ == "__main__":
    main()
