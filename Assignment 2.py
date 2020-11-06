# Simple ATM
data_base={123456:
               {"name":"Rajmeet kaur",
                "age":20,
                "email":"rajmeetkaur@gmail.com",
                "address":"73/B maitri vihar kohka bhilai ",
                "account balance": 20000,
                "mobile no.": 9876543210,
                "password":"raj123"},
           654321:
               {"name":"Sanjana nath",
                "age":21,
                "email":"sanjananath@gmail.com",
                "address":"street avanu 7 sector 7 bhilai ",
                "account balance":50000,
                "mobile no.":8765432190,
                "password":"sanju123"}}
account=int(input("please enter your user no.  :  "))
password1= str(input("please enter your password  :  "))
count=1
while count<=3:
    if password1 == data_base[account]["password"]:
        print("welcome")
        break
    count+=1
else:
    print("You have entered wrong password ")
    print("your account is blocked")
    print("try after 24 hours")
print("")
print("")
print("")
if password1 != data_base[account]["password"]:
    exit()
balance=10000
print("    ATM    ")
print("""
1)        Balance 
2)        Cash withdrawal
3)        Deposit
4)        Quit


""")
Option=int(input("Enter Option: "))

if Option==1:
    print("Balance  ₹  ",balance)


if Option==2:
    print("Balance   ₹ ",balance)
    Withdraw=float(input("Enter amount ₹ "))
    if Withdraw>0:
        remainingbalance=(balance-Withdraw)
        print("remaining Balance ₹ ",remainingbalance)
        print("Please collect the cash....")
    elif Withdraw>balance:
        print("No fund in account")
    else:
        print("None withdraw made")

if Option==3:
    print("Balance  ₹ ",balance)
    Deposit=float(input("Enter deposit amount ₹ "))
    if Deposit>0:
        ramainingbalance=(balance+Deposit)
        print("remaining balance  ₹ ",ramainingbalance)
    else:
        print("None deposit made")


if Option==4:
    exit()
