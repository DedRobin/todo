import os
import django
from faker import Faker

from django.test.client import Client

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")

    django.setup()

    # Create random user
    from django.contrib.auth.models import User

    fake = Faker()
    username = fake.name()
    password = fake.password()
    user = User(username=username)
    user.set_password(password)
    user.save()
    # End create

    client = Client()

    base_url = "http://localhost:8000"
    response = client.get(base_url)
    assert response.status_code == 200

    client.login(username=username, password=password)

    response = client.post(base_url, data={"title": "test", "text": "test"}, follow=True)
    assert response.status_code == 200

    print("All tests have passed")

    # user.delete()
