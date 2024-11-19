from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_experiment", views.add_experiment, name="add_experiment"),
    path("view_experiments", views.view_experiments, name="view_experiments"),
    path("view_experiment/<int:experiment_id>", views.view_experiment, name="view_experiment"),
    path("add_reagent", views.add_reagent, name="add_reagent"),
    path("view_reagents", views.view_reagents, name="view_reagents"),
    # path("reagents_search", views.reagents_search, name="reagents_search"),
    path("delete_reagent/<int:reagent_id>", views.delete_reagent, name="delete_reagent"),
    path("add_cell", views.add_cell, name="add_cell"),
    path("view_cells", views.view_cells, name="view_cells"),
    path("delete_cell/<int:cell_id>", views.delete_cell, name="delete_cell"),
    # path("cells_search", views.cells_search, name="cells_search"),
    path("view_protocols", views.view_protocols, name="view_protocols"),
    path("view_protocol/<str:entry>", views.view_protocol, name="protocol"),
    path("upload_protocol", views.upload_protocol, name="upload_protocol"),
    path("delete_protocol/<int:protocol_id>", views.delete_protocol, name="delete_protocol"),

]