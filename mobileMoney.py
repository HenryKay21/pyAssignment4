# Procedure:
    #1 Pitch ideas on how to accomplish the task
    #2 Divide the roles between ourselves as to who will work on what
    #3 Implement the ideas agreed upon by individualy coding and pushing the code to the shared github repo.

# Defining the function
# Defining the function
def pythonMobileMoney():
    launch = input("Please launch the Python Mobile Money with USSD code e.g *185'#' or *165'#': ")

    balance = 500000
    sending_fee = 1000
    withdraw_tax= 2000
    pin = 0000
    
    if (launch == ('*185#' or '*165#')):
         menu = int(input("Select 1 to Send Money or 7 to Withdraw Money: "))
         if (menu == 1):
             reciever = int(input("Enter the number of the receiver: "))
             amout_to_send = int(input("Enter the amount to be sent: "))
             if(amout_to_send + sending_fee < balance):
                reason = input(" Reason: ")
                print("Send UGX ",str(amout_to_send) + " to ",str(reciever) +" Reason: ",str(reason) + " at a fee of UGX ",str(sending_fee))
                customer_confirmation = int(input("Enter your pin to confirm :"))
                if (customer_confirmation == pin):
                    print("You have Sent UGX ",str(amout_to_send) + " to ",str(reciever) +" Reason: ",str(reason) + " at a fee of UGX ",str(sending_fee))
                else:
                    print("Wrong Pin!")
                
             else:
                 print("You have insuuficient balance to complete this transaction.Please visit the nearest agent to deposit!")
                              
         elif (menu == 7):
             amout_to_withdraw = int(input("Enter the amount to withdraw: "))
             if(amout_to_withdraw + withdraw_tax < balance):
                print(" Enter your pin to withdraw")
                customer_confirmation = int(input("Enter your pin to confirm :"))
                if (customer_confirmation == pin):
                    print("You have Successfulkly withdrawn")
                else:
                    print("Wrong Pin!")
                
             else:
                 print("You have insuuficient balance to complete this transaction.Please visit the nearest agent to deposit!")
                       
             
         else:
             print("Invalid option. Please enter 1 to Send Money or 7 to Withdraw Money:!")


    else:
        print("Invalid option. Please enter *185# or *165# to initiate Mobile Money:!")
pythonMobileMoney()
