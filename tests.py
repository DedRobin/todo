import os
import django

from django.test.client import Client

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")
    django.setup()

    client = Client()

    base_url = "http://localhost:8000"
    response = client.get(base_url)
    assert response.status_code == 200

    client.login(username="manti", password="Dalt0nik")

    response = client.post(base_url, data={"title": "test", "text": "test"}, follow=True)
    assert response.status_code == 200

    print("All tests have passed")
