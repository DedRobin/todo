from django.shortcuts import render, redirect

from notes.forms import AddNoteForm
from notes.models import Note


def index(request):
    notes = Note.objects.order_by("-created_at")
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            print(form)
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

        # WTF?!
        print(form)

        note_id = int(request.POST.get("id"))
        note_title = form.cleaned_data["title"]
        note_text = form.cleaned_data["text"]
        if form.is_valid():
            note = Note.objects.filter(id=note_id)
            note.update(title=note_title, text=note_text)
        return redirect("index")

    else:
        note_id = int(request.GET.get("id"))
        note = Note.objects.get(id=note_id)
        form = AddNoteForm({'title': note.title, 'text': note.text})
        return render(request, "edit_note.html", {"form": form, "note": note})
