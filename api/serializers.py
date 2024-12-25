# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import File

# # Сериализатор для регистрации пользователя
# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ["id", "username", "email", "password"]

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data["username"],
#             email=validated_data["email"],
#             password=validated_data["password"]
#         )
#         return user

# # Сериализатор для файлов
# class FileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = File
#         fields = ["id", "name", "file", "uploaded_at", "owner"]
#         read_only_fields = ["owner"]
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import File

# Получаем кастомную модель пользователя
CustomUser = get_user_model()

# Сериализатор для регистрации пользователя
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_admin = serializers.BooleanField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password", "is_admin", "storage_path"]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user

# Сериализатор для файлов
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["id", "name", "file", "uploaded_at", "owner"]
        read_only_fields = ["owner"]
