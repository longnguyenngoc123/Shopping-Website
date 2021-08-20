
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile
from django.urls import path
from . import views as home
from monan import views as monan
from send import views as send
from giohang import views as giohang
from rent import views as rent
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views as user_views
from django.urls import reverse_lazy
urlpatterns = [
    path('',home.index),
    path('register/', home.register, name='register'),
    path('login/', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('monan/', monan.PostListView.as_view(), name='monan'),
    path('giohang/', giohang.index, name='giohang'),
    path('rent/', rent.show, name='rent'),
    path('rent/emp/', rent.emp, name='rentad'),
    path('profile/', user_views.profile, name= 'profile'),
    path('updatep/', user_views.profileupdate, name = 'updatep'),
    path('change_password/', PasswordChangeView.as_view(template_name='pages/change.html',success_url=reverse_lazy('password_change_done')), name = 'password'),
    path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='pages/success.html'), name='password_change_done'),
    path('send/', send.index, name='send'),
    path('user/', home.UserListViews.as_view(), name='userlist'),
    path('user/delete/<int:id>', home.destroy),
    path('user/emp/', home.add, name='emp'),
  
]
