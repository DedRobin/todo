import pytest

from django.test.client import Client

from notes.factories import NoteFactory


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get("/api/notes/")
        assert response.status_code == 200

    def test_create_notes(self):
        NoteFactory.create_batch(5)
        response = self.client.get("/api/notes/")
        assert response.status_code == 200
        assert len(response.data) == 5

    def test_create_one_note(self):
        data = {"title": "test_title", "text": "test_text"}
        response = self.client.post("/api/notes/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/notes/")
        assert response.status_code == 200
        assert len(response.data) == 1
