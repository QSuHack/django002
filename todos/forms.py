from .models import Task
from django import forms
class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ("title", "details",'expiry_time', "assigned", "task_status")
    def form_valid(self, form):
        form.save()
