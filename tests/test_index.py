import pytest

from django.test.client import Client
from faker import Faker

from notes.factories import UserFactory


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
        data = {"username": self.user.username,
                "password": self.user.password}
        response = self.client.post("/login/", data=data)
        assert response.status_code == 200

    # @pytest.mark.skip
    # def test_register_login_logout(self):
    #     response = self.client.get("/register")
    #     assert response.status_code == 200
    #
    #     self.client.post('/register/', {
    #         "username": "test_user",
    #         "email": "test_email",
    #         "first_name": "test_first_name",
    #         "last_name": "test_first_name",
    #         "password": "test_password123!"
    #     })
    #     is_user_existed = User.objects.filter(username='test_user').exists()
    #     assert is_user_existed == True
