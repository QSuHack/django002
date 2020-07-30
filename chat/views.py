from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.db.models import QuerySet
from .models import Message
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, CreateView, 
)
from .forms import MessageForm, MessageFormSpecific
from django.views.decorators.clickjacking import xframe_options_exempt 


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        query = (Message.objects.filter(recipient=self.request.user) 
         | Message.objects.filter(sender=self.request.user) 
        
         )

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


class MessageSeparetedListView(LoginRequiredMixin, ListView):
    model = Message
    def get_queryset(self, *args, **kwargs):
        second_user = User.objects.get(id=self.kwargs["pk"])
        query = (
                Message.objects.filter(recipient=self.request.user, sender=second_user) 
                | Message.objects.filter(sender=self.request.user, recipient=second_user )
                | Message.group.get_queryset(member=self.request.user)
                )
        return query.order_by('post_date')
    def post(self, *args, **kwargs):
        form = MessageFormSpecific(self.request.POST)
        if form.is_valid():
            form.instance.sender = self.request.user
            form.instance.recipient =get_object_or_404(User, id=self.kwargs['pk'])
            form.save()
        return redirect("messages-sep",self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = MessageFormSpecific
        context["form"] = form
        return context
    


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name="chat/user_list.html"
    def get_queryset(self):
        subquery = Message.objects.filter(recipient=self.request.user).distinct().values('sender')
        subquery3= Message.objects.filter(sender=self.request.user).distinct().values('recipient')
        l = list()
        for x in subquery3:
            l.append(x.get('recipient'))
        for x in subquery:
            l.append(x.get('sender'))
        l = list(set(l))
        subquery = User.objects.filter(id__in = l )
        return subquery 
