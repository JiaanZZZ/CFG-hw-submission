from logging import exception


correct_anwser='aaaa'
count=0

while True and count<3:
    answer=input("please enter a pin code: ")
    if answer==correct_anwser:
        break
    count+=1

account_balance=100
withdrawal_amount= input("how much money you would like to withdraw? ")

def withdrawal(account_balance, withdrawal_amount):
    remain=account_balance-float(withdrawal_amount)
    if remain <0:
        raise Exception("You are overdrawing money. Action not completed.")
    else: 
        print("You have successfully withdrawn your money.")

        

try:
    withdrawal(account_balance,withdrawal_amount)
    
except:
    print("You are overdrawing money. Action not completed.Please try again")

finally:
    print("Thank you for using our services")