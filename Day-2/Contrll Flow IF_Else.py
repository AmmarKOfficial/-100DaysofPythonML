## Controll


###If Condiditon
temp = 15
if temp > 30:  #Terminate conditional statement with coln
    print("It's Warm")
elif temp > 20:
    print("It's Nice")
else:
    print("It's Cold")   
print("If Block Ended")

## Clean Practice
age = 17
message = "Eligible" if age >=18 else "Not Eligible"  ##Ternary Operator
print(message)

## Loan Demo

high_income = True
good_credit = False
student = True
if (high_income and good_credit):
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")
    
if (high_income and good_credit) or student:
    print("Eligible for Loan, Only with one condition or Student")
else:
    print("Not Eligible for Loan")
    
if (high_income or not good_credit):
    print("Eligible for Loan, Only with one not applied")
else:
    print("Not Eligible for Loan")
    
## Logical Operators can be short circuits
    
if 18<= age <40:
    print("Age is Good")
else:
    print("Age Error")
