from django.urls import path
from . import views

urlpatterns=[
    path("", views.index),
    path("login", views.login),
    path("register", views.register),
    path("main", views.main),
    path("dinning", views.dinning),
    path("add_resteraunt", views.add_resteraunt),
    path("resteraunt_review", views.resteraunt_review)
]