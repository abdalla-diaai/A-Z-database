from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_reagent", views.add_reagent, name="add_reagent"),
    path("add_cell", views.add_cell, name="add_cell"),
    path("view_reagents", views.view_reagents, name="view_reagents"),
    path("view_cells", views.view_cells, name="view_cells"),
    path("delete_reagent/<int:reagent_id>", views.delete_reagent, name="delete_reagent"),
    path("delete_cell/<int:cell_id>", views.delete_cell, name="delete_cell"),
]