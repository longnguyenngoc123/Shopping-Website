from django.urls import path
from .import views
from monan import views as monan
urlpatterns = [
    path('', views.index),
    path('monan/', monan.PostListView.as_view(), name='monan'),
]
