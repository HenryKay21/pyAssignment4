# Procedure:
    #1 Pitch ideas on how to accomplish the task
    #2 Divide the roles between ourselves as to who will work on what
    #3 Implement the ideas agreed upon by individualy coding and pushing the code to the shared github repo.

# Defining the function
def pythonMobileMoney():
    launch = str(input("Please launch the Python Mobile Money with USSD code: "))
    customerPIN = int(input("Enter PIN: "))

    # Conditions
    if (launch == str(input("*000#"))):
        # print("1. Send Money 2. Withdraw Money")
        print("Succeeded") # For testing to see if code executes
    else:
        #print("Invalid PIN. Please enter the correct PIN number!")
        print("Connection failed")




pythonMobileMoney()
