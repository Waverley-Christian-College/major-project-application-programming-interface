import time 
# This file is the src for user input 
# This is where the user will use the program

# Ask the user what company it wants to seek
# company = input("Enter the symbol of company ")
# print(company)

# Define Functions

def showMultipleGraphsFeature():

    #Put call tiingo.py code
    print("hello2")
    

def VSS():
    #Put call tiingo.py code
    print("hello")

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

    print("Show multiple graphs")
    time.sleep(1)
    print("Volatility Scoring System")
    time.sleep(2)
    desired_feature = input("What feature do you want to use? ")

    if desired_feature == "Show multiple graphs" or "SMM": #SMM is for debugging

        showMultipleGraphsFeature()
    elif desired_feature == "Volatility Scoring System" or "VSS": #VSS is for debugging 

        VSS()
    else:
        print("That is not a feature")








