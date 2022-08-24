import pytest

from django.test.client import Client
from faker import Faker

from notes.factories import UserFactory, NoteFactory


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()

    def test_index(self):
        self.client.force_login(self.user)

        response = self.client.get("/")
        assert response.status_code == 200

    def test_register(self):
        data = {"username": self.fake.user_name(),
                "first_name": self.fake.first_name(),
                "last_name": self.fake.last_name(),
                "email": self.fake.email(),
                "password": self.fake.md5()}
        response = self.client.post("/register/", data=data)
        assert response.status_code == 302
        assert response.url == "/"

    def test_login(self):
        data = {"username": self.fake.user_name(),
                "first_name": self.fake.first_name(),
                "last_name": self.fake.last_name(),
                "email": self.fake.email(),
                "password": self.fake.md5()}
        response = self.client.post("/register/", data=data)
        assert response.status_code == 302
        assert response.url == "/"

        # data = {"username": self.user.username,
        #         "password": self.user.password}
        data_login = {"username": data["username"],
                      "password": data["password"]
                      }

        response = self.client.post("/login/", data=data_login)
        assert response.status_code == 302
        assert response.url == "/"

    def test_add_notes(self):
        self.client.force_login(self.user)
        NoteFactory.create_batch(10)

        response = self.client.get("/")
        assert response.status_code == 200
        # assert len(response.data) == 10

