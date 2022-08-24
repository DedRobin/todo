import factory
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory

from notes.models import Note


class NoteFactory(DjangoModelFactory):
    class Meta:
        model = Note

    title = factory.Faker('word')
    text = factory.Faker('text')


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('word')
    email = factory.Faker('word')
