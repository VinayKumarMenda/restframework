from django.urls import path
from .views import *
urlpatterns = [
    path('get',get),
    path('add',add),
    path('update/<id>/',update),
    path('delete/<id>/',delete)
]
