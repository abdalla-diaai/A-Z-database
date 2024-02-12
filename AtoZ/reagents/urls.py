from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add", views.add_reagent, name="add"),
    path("view", views.view, name="view"),
    path("delete/<int:reagent_id>", views.delete, name="delete"),
]