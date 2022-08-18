import factory

from factory.django import DjangoModelFactory

from notes.models import Note


class NoteFactory(DjangoModelFactory):
    class Meta:
        model = Note

    title = factory.Faker('some_title')
    text = factory.Faker('some_text')
