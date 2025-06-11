import time 
import VSS
import showGraphs
# This file is the src for user input 
# This is where the user will use the program

# Ask the user what company it wants to seek
# company = input("Enter the symbol of company ")
# print(company)

# Define Functions
def VSSFunction():
    #Put call tiingo.py code
    VSS.hello()

def SMH():

     #Put call tiingo.py code
    print("hello2")

    showGraphs.marcus()



    

def VSSFunction():
    #Put call tiingo.py code
    VSS.hello()

def SMH():

    #Put call tiingo.py code
    print("hello2")
    showGraphs.marcus()
# Ask the users name
userName = input("Enter your name? ")

print(f"Hello {userName}, Welcome to the Ultimate Volatility Tracker")
time.sleep(2)
# Ask what the user wants to see
print("Our Features")
time.sleep(1)
print("About Us")
time.sleep(1)
userWantsToSee = input("What do you want to see? ")

# Ask the user what feature they want to use

if userWantsToSee == "Our Features": # Ask the user what feature they want to use

    print("Show multiple graphs (Type SMG)")
    time.sleep(1)
    print("Volatility Scoring System (Type VSS)")
    time.sleep(2)
    desired_feature = input("What do you you want to use? ")

    if desired_feature == "ok":
        print("yaysss")

    
    elif desired_feature == "VSS": #VSS is for debugging 
        
        VSSFunction()

    elif desired_feature == "SMG":
        
        
        SMH()


    








