from django.urls import path, re_path

from main.api.views import (
    ChatListView,
    ChatDetailView,
    ChatCreateView,
    ChatDestroyView,
    ChatUpdateView
)

app_name = 'chat'

urlpatterns = [
    path('', ChatListView.as_view()),
    path('create/', ChatCreateView.as_view()),
    path('<int:pk>', ChatDetailView.as_view()),
    path('<int:pk>/update', ChatUpdateView.as_view()),
    path('<int:pk>/delete', ChatDestroyView.as_view()),
]