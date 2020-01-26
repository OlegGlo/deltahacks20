# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from .models import Progress,Goal

from django.http import Http404

from django.shortcuts import get_object_or_404, render

from django.urls import reverse

#from django.template import loader


def index(request):
    latest_goal_list = Goal.objects.order_by('-pub_date')[:5]
    context = {
        'latest_goal_list': latest_goal_list}
    return render(request, 'planner/index.html', context)

def detail(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    return render(request, 'planner/detail.html', {'goal': goal})


def results(request, goal_id):
    response = "You're looking at the results of goal %s."
    return HttpResponse(response % goal_id)

def results(request, goal_id):
    question = get_object_or_404(Goal, pk=goal_id)
    return render(request, 'planner/results.html', {'goal': goal})

def vote(request, goal_id):
    return HttpResponse("You're voting on goal %s." % goal_id) #change this to whatever it is supposed to be

def vote(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    try:
        selected_progress = goal.progress_set.get(pk=request.POST['progress'])
    except (KeyError, Progress.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'planner/detail.html', {
            'goal': goal,
            'error_message': "You didn't select a progress.",
        })
    else:
        selected_progress.activity += 1 #votes = activity
        selected_progress.save() 
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('planner:results', args=(goal.id,)))