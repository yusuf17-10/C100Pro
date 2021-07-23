class ATM(object):
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceenqiury(self):
        print("Your Balance Is :$50")
    
    def cashwithdrawal(self,amount):
        new_amount = 100-amount
        print("You Withdrawed: "+str(amount) + "Your remaing balance is :"+str(new_amount))

def main():
    name = input("Hello what's Your name : ")
    print("Hello, "+name)
    cardnumber = input("Input your card number: ")
    pin = input("Insert Your Card Number Please: ")
    new_user = ATM(cardnumber,pin)

    print("Choose your activity")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawal")
    activity = int(input("Enter Activity choice : "))

    if (activity ==1):
        new_user.balanceenqiury()
    elif (activity ==2):
        amount = int(input("Enter The Amount:"))
        new_user.cashwithdrawal(amount)
    else:
        print("Enter a valif number")


if __name__ == "__main__":
    main()