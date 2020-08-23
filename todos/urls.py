from django.urls import path

from .views import TaskListView, edit_task, TaskArchiveListView, TaskCreateView

urlpatterns = [
    path("list", TaskListView.as_view(), name="task-list"),
    path("edit", edit_task),
    path('archive',TaskArchiveListView.as_view() ,name="archive-task"),
    path('new', TaskCreateView.as_view(),name="create-task")
]