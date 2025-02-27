"""django002 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from weather.views import search_view, CityDetailView
from chat.views import MessageListView, MessageCreateView, MessageSeparetedListView, UserListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/',search_view,name="weather-search"),
    path('city/<int:pk>',CityDetailView.as_view(),name="weather-city_detail" ),
 #   path('messages/', MessageListView.as_view(), name="messages-view"),
    path('messages/', UserListView.as_view(), name="messages-view"),
    path('EU/', include('qualified_majority_app.urls')),
    path('messages/<int:pk>', MessageSeparetedListView.as_view(), name='messages-sep'),
    path('task/', include('todos.urls')),
]
