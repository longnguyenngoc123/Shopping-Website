from django.urls import path
from . import views
from giohang import views as giohang
urlpatterns = [
    path('', views.PostListView.as_view(), name='blog'),
    path('delete/<int:id>', views.destroy),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),
    path('giohang/<int:id>', giohang.update_cart, name='update_cart'),
    path('emp', views.emp),
    path('product/<int:id>', views.productdetail, name='pdetail'),
    
]
