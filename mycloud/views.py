from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect

from api.models import CustomUser
from api.models import File
from api.forms import FileForm

# Регистрация
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("file_list")
    else:
        form = UserCreationForm()
    return render(request, "api/register.html", {"form": form})

# Вход
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("file_list")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

# Список файлов пользователя
@login_required
def file_list_view(request):
    files = File.objects.filter(owner=request.user)
    return render(request, "file_list.html", {"files": files})

# Загрузка файла
@login_required
def file_upload_view(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.owner = request.user
            file.save()
            return redirect("file_list")
    else:
        form = FileForm()
    return render(request, "file_upload.html", {"form": form})

# Удаление файла
@login_required
def file_delete_view(request, pk):
    file = File.objects.get(pk=pk, owner=request.user)
    if request.method == "POST":
        file.delete()
        return redirect("file_list")
    return render(request, "file_confirm_delete.html", {"file": file})

# Админ-функция: Список пользователей
@user_passes_test(lambda u: u.is_staff)
def admin_user_list_view(request):
    users = CustomUser.objects.all()
    return render(request, "admin_user_list.html", {"users": users})

# Админ-функция: Удаление пользователя
@user_passes_test(lambda u: u.is_staff)
def admin_user_delete_view(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect("admin_user_list")
    return render(request, "admin_user_confirm_delete.html", {"user": user})
