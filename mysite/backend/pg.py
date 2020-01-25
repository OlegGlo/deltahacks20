
goals = []

def inputNumber(message): #yeah, I basically stole this code online where it just takes an integer input
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 

#this function simply lets the user create a set of goals
def testOut():
    
    numGoals = 1 #int i counts how many goals you are 
    challengeLength = inputNumber("How many days would you like the challenge to run for? ") #number of days the challenge runs for
    while(True):
        #this segment is where the title and description of the goal are set
        print("Goal number " + str(numGoals) + ".")
        title = input("Title your goal: ")
        description = input("Type in a description of goal: ")
        print("What type of goal is it?")

        #this segment contains all the constructors for the types of goals depend on what you want to create
        typeGoal = input("Enter max if it is a restriction, Enter min if it is a minimum goal, enter anything else for it to be yes/no type of goal. ")
        if (typeGoal.casefold() == 'max'):
            max = input("Input a maximum number. This is the limit of the goal you want to set" )
            #insert constructor here
        elif (typeGoal.casefold() == 'min'):
            min = input("Input a minimum number. This is the minimum to acheive your goal" )
            #insert constructor here
        else: #if its a yes/no goal
            print("This goal will have a simple yes or no completion requirement")
            #goals.append(YesNoGoal(title, desc))
        askAgain = input("Would you like to set another goal? enter Yes to make another: ")
        if (askAgain.casefold() != 'yes'):
            break
        numGoals += 1
    print("done")
    
testOut()
