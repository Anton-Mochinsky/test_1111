# from django.urls import path
# from .views import RegisterView, FileListCreateView, FileDeleteView, AdminUserListView, AdminUserDeleteView

# urlpatterns = [
#     # Регистрация
#     path("register/", RegisterView.as_view(), name="register"),

#     # Файлы пользователя
#     path("files/", FileListCreateView.as_view(), name="file-list-create"),
#     path("files/<int:pk>/", FileDeleteView.as_view(), name="file-delete"),

#     # Админ-функции
#     path("admin/users/", AdminUserListView.as_view(), name="admin-user-list"),
#     path("admin/users/<int:pk>/", AdminUserDeleteView.as_view(), name="admin-user-delete"),
# ]
from django.urls import path
from .views import (
    RegisterView,
    FileListCreateView,
    FileDeleteView,
    AdminUserListView,
    AdminUserDeleteView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("files/", FileListCreateView.as_view(), name="file-list-create"),
    path("files/<int:pk>/", FileDeleteView.as_view(), name="file-delete"),
    path("admin/users/", AdminUserListView.as_view(), name="admin-user-list"),
    path("admin/users/<int:pk>/", AdminUserDeleteView.as_view(), name="admin-user-delete"),
]
