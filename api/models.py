from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    storage_path = models.CharField(max_length=255, default="")

    # Переопределяем поля groups и user_permissions
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Уникальное имя для обратной связи
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Уникальное имя для обратной связи
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return self.name