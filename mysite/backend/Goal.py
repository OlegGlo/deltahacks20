# Parent Class - not instantiated
class Goal(object):

    def __init__(self, title, desc):
        self.title = title
        self.completed = False
        self.desc = desc

    def toString(self):
        return "Title: " + self.title + "\nDesc: " + self.desc + "\nCompleted: " + ("Yes" if self.completed else "No")

# YesNoGoal Class
class YesNoGoal(Goal):

    def __init__(self, title, desc):
        super(YesNoGoal, self).__init__(title, desc)

    def toString(self):
        return "=== YesNoGoal ===\n" + super(YesNoGoal, self).toString() + "\n"

# QuantitativeGoal Class - not instantiated
class QuantitativeGoal(Goal):

    def __init__(self, title, desc, metric, goalQuantity):
        super(QuantitativeGoal, self).__init__(title, desc)
        self.metric = metric
        self.goalQuantity = goalQuantity

    def toString(self):
        return super(QuantitativeGoal, self).toString()

# MinGoal Class
class MinGoal(QuantitativeGoal):
    def __init__(self, title, desc, metric, goalQuantity):
        super(MinGoal, self).__init__(title, desc, metric, goalQuantity)

    def toString(self):
        return "=== MinGoal ===\n" + super(MinGoal, self).toString() + "\n"

# MaxGoal Class
class MaxGoal(QuantitativeGoal):
    def __init__(self, title, desc, metric, goalQuantity):
        super(MaxGoal, self).__init__(title, desc, metric, goalQuantity)

    def toString(self):
        return "=== MaxGoal ===\n" + super(MaxGoal, self).toString() + "\n"

###

# g = Goal("bruh", "be bruhed")
# print(g.toString())

# yn = YesNoGoal("this is a goal", "achieve this goal!")
# print(yn.toString())

yn = MaxGoal("this is a goal", "achieve this goal!", "pushups", 10)
print(yn.toString())