# Parent Class
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
        return "=== YesNoGoal ===\n" + str(super(YesNoGoal, self).toString()) + "\n"

# MinGoal Class
class MinGoal(Goal):
    def __init__(self, title, desc):
        super(MinGoal, self).__init__(title, desc)

    def toString(self):
        return "=== MinGoal ===\n" + str(super(MinGoal, self).toString()) + "\n"

# MaxGoal Class
class MaxGoal(Goal):
    def __init__(self, title, desc):
        super(MaxGoal, self).__init__(title, desc)

    def toString(self):
        return "=== MaxGoal ===\n" + str(super(MaxGoal, self).toString()) + "\n"



# g = Goal("bruh", "be bruhed")
# print(g.toString())

yn = YesNoGoal("this is a goal", "achieve this goal!")
print(yn.toString())