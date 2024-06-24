# example/urls.py
from django.urls import include, path
from rest_framework import routers
from example.views import index, UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)

urlpatterns = [
    path("", index),
    path("api/v1/", include(router.urls)),
]
