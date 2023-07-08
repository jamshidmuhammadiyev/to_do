from django.urls import path
from .views import (ListTodoView,CreateTodoView,DetailTodoView, DeleteTodoView,
                    UpdateTodoView,StatusUpdateView,GetTodoStatusView)


urlpatterns=[
    path('',ListTodoView.as_view()),
    path('create/',CreateTodoView.as_view()),
    path('<int:todo_id>/',DetailTodoView.as_view()),
    path('delete/<int:todo_id>/',DeleteTodoView.as_view()),
    path('update/<int:todo_id>/',UpdateTodoView.as_view()),
    path('status_update/<int:todo_id>/',StatusUpdateView.as_view()),
    path('status/<str:status>',GetTodoStatusView.as_view()),

]