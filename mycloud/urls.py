from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("files/", views.file_list_view, name="file_list"),
    path("files/upload/", views.file_upload_view, name="file_upload"),
    path("files/<int:pk>/delete/", views.file_delete_view, name="file_delete"),
    path("admin/users/", views.admin_user_list_view, name="admin_user_list"),
    path("admin/users/<int:pk>/delete/", views.admin_user_delete_view, name="admin_user_delete"),
]
