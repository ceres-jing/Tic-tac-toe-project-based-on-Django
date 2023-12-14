from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, re_path

from .views import home, new_invitation, accept_invitation, SignUpView

urlpatterns = [
    path(r'home', home, name="player_home"),

    path(r'login', LoginView.as_view(template_name='player/login_form.html'),
         name='player_login'),
    path(r'logout', LogoutView.as_view(), name='player_logout'),

    path(r'new_invitation', new_invitation, name='player_new_invitation'),

    re_path(r'accept_invitation/(?P<id>\d+)', accept_invitation, name="player_accept_invitation"),

    path(r'signup', SignUpView.as_view(), name='player_signup'),

]
