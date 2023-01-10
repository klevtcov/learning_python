from django.urls import path

from users.views import login, logout, UserRegistrationView, UserProfileView
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    # path('registration/', registration, name='registration'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    # path('profile/', profile, name='profile'),
    path('profile/<int:pk>', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', logout, name='logout'),
]

