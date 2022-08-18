from django.urls import include, path
from rest_framework import routers
from api.notes.views import NoteViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"notes", NoteViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include(
        "rest_framework.urls",
        namespace="rest_framework"
    )),
]
