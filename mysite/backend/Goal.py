# Parent Class - not instantiated
class Goal(object):

    def __init__(self, title, desc):
        self.title = title
        self.completed = False
        self.failed = False
        self.desc = desc

    def toString(self):
        return "Title: " + self.title + "\nDesc: " + self.desc + "\nCompleted: " + ("Yes" if self.completed else "No") + "\nFailed: " + ("Yes" if self.failed else "No")

# YesNoGoal Class
class YesNoGoal(Goal):

    def __init__(self, title, desc):
        super(YesNoGoal, self).__init__(title, desc)

    def setState(self, state):
        self.completed = state

    def toString(self):
        return "=== YesNoGoal ===\n" + super(YesNoGoal, self).toString() + "\n"

# QuantitativeGoal Class - not instantiated
class QuantitativeGoal(Goal):

    def __init__(self, title, desc, metric, goalQuantity):
        super(QuantitativeGoal, self).__init__(title, desc)
        self.metric = metric
        self.goalQuantity = goalQuantity
        self.currentQuantity = 0

    def toString(self):
        return super(QuantitativeGoal, self).toString()

# MinGoal Class
class MinGoal(QuantitativeGoal):

    def __init__(self, title, desc, metric, goalQuantity):
        super(MinGoal, self).__init__(title, desc, metric, goalQuantity)

    def setState(self, state):
        self.currentQuantity = state
        if self.currentQuantity >= self.goalQuantity:
            self.completed = True
            print("Goal completed!\n") ##temp

    def toString(self):
        return "=== MinGoal ===\n" + super(MinGoal, self).toString() + "\nMin " + self.metric + ": " + str(self.goalQuantity) +  "\nCurrent # of " + self.metric + ": " + str(self.currentQuantity) + "\n"

# MaxGoal Class
class MaxGoal(QuantitativeGoal):

    def __init__(self, title, desc, metric, goalQuantity):
        super(MaxGoal, self).__init__(title, desc, metric, goalQuantity)

    def setState(self, state):
        self.currentQuantity = state
        if self.currentQuantity > self.goalQuantity:
            self.failed = True
            print("Goal completed!\n") ##temp

    def toString(self):
        return "=== MaxGoal ===\n" + super(MaxGoal, self).toString() + "\nMax " + self.metric + ": " + str(self.goalQuantity) +  "\nCurrent # of " + self.metric + ": " + str(self.currentQuantity) + "\n"

# mg = MinGoal("this is a goal", "achieve this goal!", "pushups", 10)
# print(mg.toString())

# mg.setState(50)

# print(mg.toString())