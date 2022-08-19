import pytest

from django.test.client import Client


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get("/")
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
