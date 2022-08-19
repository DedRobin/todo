import logging

from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

from notes.forms import AddNoteForm, LoginForm, RegisterForm
from notes.models import Note

logger = logging.getLogger(__name__)


def index(request):
    if not request.user.is_authenticated:
        return redirect("login")

    else:
        first_name = request.user.first_name
        last_name = request.user.last_name
        notes = Note.objects.filter(author_id=request.user.id).order_by("-created_at")

        if request.GET.get("q"):
            param = request.GET.get("q")
            notes = notes.filter(Q(title__contains=param) | Q(text__contains=param))
        form = AddNoteForm()
        variables = {"notes": notes, "form": form, "first_name": first_name, "last_name": last_name}
        return render(request, "index.html", variables)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request, **form.cleaned_data)
            if user is None:
                error = "User is not found!"
                return render(request, "login.html", {"form": form, "error": error})
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("index")
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})


def add_note(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                author=request.user, title=form.cleaned_data["title"], text=form.cleaned_data["text"]
            )
            return redirect("index")


def delete_note(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        note_id = int(request.POST.get("delete"))
        Note.objects.get(id=note_id).delete()
        return redirect("index")
    else:
        return redirect("index")


def edit_note(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        form = AddNoteForm(request.POST)
        note_id = int(request.POST.get("id"))

        if form.is_valid():
            note = Note.objects.filter(id=note_id, author_id=request.user.id)
            note.update(title=form.cleaned_data["title"], text=form.cleaned_data["text"])
        return redirect("index")

    else:
        note_id = int(request.GET.get("id"))
        is_note_existed = Note.objects.filter(id=note_id, author_id=request.user.id).exists()

        if is_note_existed:
            note = Note.objects.get(id=note_id)
            form = AddNoteForm({'title': note.title, 'text': note.text})
            return render(request, "edit_note.html", {"form": form, "note": note})
        else:
            return HttpResponseNotFound()
