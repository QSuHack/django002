from django.shortcuts import render
from django.views.generic import DetailView , ListView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
# Create your views here.
from .models import Task
from .forms import TaskForm
class TaskDetailView():
    model = Task
class TaskListView(ListView):
    model = Task
def edit_task(request, *args, **kwargs):
    id = request.headers.get("ID")
    status = request.headers.get("NewStatus")
    status = int(status)

    if status in [0,1,2,3]:
        obj = Task.objects.filter(id=id).first()
        obj.task_status = status
        obj.save()
    return HttpResponse(request.headers.get("ID"))

class TaskArchiveListView(ListView):
    model = Task
    template_name = "todos/task_archive.html"
    def get_queryset(self, *args, **kwargs):
        return Task.objects.filter(task_status=3)
    
class TaskCreateView(LoginRequiredMixin, FormView):
    template_name = "todos/task_form.html"
    form_class = TaskForm
    success_url = 'list'
    def form_valid(self, form):
        TaskForm.form_valid(TaskForm, form)
        return super().form_valid(form)