from django.urls import path
from user import views

urlpatterns = [
    path(
        'register_user/',
        views.UserCreateView.as_view(),
        name='user_register_api'
    ),
    path(
        'list_users/',
        views.UserListView.as_view(),
        name='user_list_api'
    ),
    path(
        'resize_user_image/<int:user_id>/',
        views.GetUserResizedImage.as_view(),
        name='get_user_resize_image_api'
    ),
]
