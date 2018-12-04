from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from telegram import views

urlpatterns = [
    url('message/', views.MessageList.as_view()),
    url('message/<int:pk>/', views.MessageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
