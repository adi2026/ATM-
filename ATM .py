#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

print("Please insert your card:")
time.sleep(2)
password=123
pin=int(input("inter your atm pin:"))

balance=1000
transactions = [] 

if pin==password:
    while True:
        
        print("""
              1 == balance
              2 == withdraw amount
              3 == deposit balance
              4 == mini Satement
              5 == exit
              """)
        try:
            option=int(input("please enter your choise:"))
        except:
              print("Plese enter vaild option")

        if option ==1:
              print(f"your current balance is {balance}")

        if option ==2:
              withdraw_amount=int(input("Please enter withdraw amount"))
              balance = balance-withdraw_amount
            
              print(f"{withdraw_amount} is debited from your account")
                
              print(f"your updated Balance is {balance}")
            
        if option ==3:
            
            deposit_amount=int(input("Please enter deposit_amount"))
            balance = balance + deposit_amount
                
            print(f"{deposit_amount} is credit to your account")
            print(f"your updated Balance is {balance}")
                
        if option==4:
            print("Mini Statement:")
            for t in transactions:      
                print("-",t)
            print(f"Current balance: {balance}")
             
                 
        if option ==5:
            
            print("Thank you for useing the ATM")
            break

else:
    print("wrong pin please try again")


# # 

# In[ ]:




