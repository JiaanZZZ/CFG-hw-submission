class ATM:
    correct_answer='aaaa'
    account_balance=100
    
    def __init__(self,correct_answer,account_balance):
        self.correct_answer=correct_answer
        self.account_balance=account_balance


    
    def pin_code(self):
        count=0
        while True and count<3:
            answer=input("please enter a pin code: ")
            if answer==self.correct_answer:
                break
            count+=1

   
    def withdrawal(self):
        def util():
            withdrawal_amount= input("how much money you would like to withdraw? ")

            remain=self.account_balance-float(withdrawal_amount)
            if remain <0:
                raise Exception("You are overdrawing money. Action not completed.")
            else: 
                print("You have successfully withdrawn your money.")


        try:
            util()
            
        except:
            print("You are overdrawing money. Action not completed. Please try again")

        finally:
            print("Thank you for using our services")


atm = ATM('aaaa',200)
atm.pin_code()
atm.withdrawal()