from django.db import models

import datetime

from django.utils import timezone






# Create your models here.

class Goal(models.Model): #used to be question
    goal_title = models.CharField(max_length=200)

    goal_description = models.CharField(max_length=300) 

    pub_date = models.DateTimeField('date published')

    due_date = models.DateField('date due')

    def __str__(self):
        return self.goal_title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Progress(models.Model): #used to be choice
    prog_tracker = models.ForeignKey(Goal, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)

    percent_complete = models.IntegerField(default=0)

    def __str__(self):
        return self.prog_tracker