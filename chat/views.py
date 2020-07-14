from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Message
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, CreateView, 
)
from .forms import MessageForm

class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        query = Message.objects.filter(recipient=self.request.user) | Message.objects.filter(sender=self.request.user)
        return query.order_by('post_date')



    def post(self, *args, **kwargs):
        form = MessageForm(self.request.POST)
        if form.is_valid():
            form.instance.sender = self.request.user
            form.save()
        return redirect("messages-view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = MessageForm()
        context["form"] = form
        return context
    
        

class MessageCreateView(LoginRequiredMixin,CreateView):
    model = Message
    fields=["recipient", "content"]
