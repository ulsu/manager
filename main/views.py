from models import *
from django.contrib.auth.decorators import login_required
from django.template import loader, RequestContext
from django.http import HttpResponse

@login_required
def index(request):
    task_list = Task.objects.filter(parent=None)

    t = loader.get_template('index.html')
    c = RequestContext(request, {
            'tasks': task_list,
        })

    return HttpResponse(t.render(c))

@login_required
def detail(request, task_id):
    task = Task.objects.filter(pk=task_id)

    t = loader.get_template('task.html')
    c = RequestContext(request, {
            'task': task,
        })

    return HttpResponse(t.render(c))