import Goal

days = []
# initialGoals = []

## some hardcode for testing
numDays = 21

# initialGoals.append(Goal.MinGoal("Pushups", "Complete 10 pushups.", "pushups", 10))

# for i in range(0,numDays):
#     days.append(initialGoals)

def getGoal(day, goal):
    return days[day][goal]

def getDay(day):
    return days[day]

def appendGoal(day, goal):
    days[day].append(goal)

def appendDay():
    days.append([])

def setGoal(day, goalIndex, newGoal):
    days[day][goalIndex] = newGoal

def setDay(day, newDay):
    days[day] = newDay

def batchGoalAppend(goal, dayStart, dayEnd):
    for n in range(dayStart, dayEnd):
        days[n].append(goal)

# for n in range(0, numDays):
#     appendDay()

# appendGoal(0, Goal.YesNoGoal("Eat an Apple", "Eat an Apple today."))

# setGoal(0, 0, Goal.MinGoal("Pushups", "Complete 10 pushups.", "pushups", 10))

# print(days)

# print(getGoal(0,0).toString())
# print(len(days))