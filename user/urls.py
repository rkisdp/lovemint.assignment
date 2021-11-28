from django.urls import path
from user import views

urlpatterns = [
    path(
        'register_user/',
        views.UserCreateView.as_view(),
        name='user_register_api'
    ),
]
