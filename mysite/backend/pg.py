import Goal
goals = []
days = []
numDays = 0

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
    numDays = inputNumber("How many days would you like the challenge to run for? ") #number of days the challenge runs for
    while(True):
        #this segment is where the title and description of the goal are set
        print("Goal number " + str(numGoals) + ".")
        title = input("Title your goal: ")
        description = input("Type in a description of goal: ")
        print("What type of goal is it?")

        #this segment contains all the constructors for the types of goals depend on what you want to create
        typeGoal = input("Enter max if it is a restriction, Enter min if it is a minimum goal, enter anything else for it to be yes/no type of goal. ")
        if (typeGoal.casefold() == 'max'):
            metric = input("Set a metric you are trying to measure. ")
            max = inputNumber("Input a maximum number. This is the limit of the goal you want to set ")
            goals.append(Goal.MaxGoal(title, description, metric, max))
        elif (typeGoal.casefold() == 'min'):
            metric = input("Set a metric you are trying to measure. ")
            min = input("Input a minimum number. This is the minimum to acheive your goal" )
            goals.append(Goal.MinGoal(title, description, metric, min))
        else: #if its a yes/no goal
            print("This goal will have a simple yes or no completion requirement")
            goals.append(Goal.YesNoGoal(title, description))
        askAgain = input("Would you like to set another goal? enter Yes to make another: ")
        if (askAgain.casefold() != 'yes'):
            break
        numGoals += 1
    print("done")

#this is just a premade test case
def testcase1():
    numDays = 20
    goals.append(Goal.MinGoal("Sleep", "Get enough sleep", "hours", 8))
    goals.append(Goal.MaxGoal("TV Time", "Dont watch too much tv", "hours", 3))
    goals.append(Goal.MinGoal("Read", "Read a number of pages every day", "pages", 50))
    goals.append(Goal.YesNoGoal("Dishes", "Do dishes"))

#to initialize the number of days
def initializeDays():
    for i in range(0,numDays):
        days.append(goals)

def daysChart():
#    for i in range(0,numDays):
#        for j in goals:

        
#testOut()
#testcase1()
initializeDays()


for n in goals:
    print(n.toString())
