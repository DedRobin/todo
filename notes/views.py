from django.shortcuts import render, redirect

from notes.forms import AddNoteForm
from notes.models import Note


def index(request):
    notes = Note.objects.all()
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                author=request.user, title=form.cleaned_data["title"], text=form.cleaned_data["text"]
            )
            return redirect("index")
    else:
        form = AddNoteForm()
    return render(request, "index.html", {"notes": notes, "form": form})


def delete_note(request):
    if request.method == "POST":
        note_id = int(request.POST.get("delete"))
        Note.objects.get(id=note_id).delete()
        return redirect("index")
    else:
        return redirect("index")


def edit_note(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.filter(id=note_id).update(title=form.cleaned_data["title"],
                                                   text=form.cleaned_data["text"])
            return redirect("index")
    else:
        note_id = int(request.GET.get("id"))
        note = Note.objects.get(id=note_id)
        form = AddNoteForm({'title': note.title, 'text': note.text})
        return render(request, "edit_note.html", {"form": form})
