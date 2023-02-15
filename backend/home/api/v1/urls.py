from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AuthViewSet,ItemViewSet,UserViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register('item', ItemViewSet )
router.register('user', UserViewSet )
router.register('auth', AuthViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
