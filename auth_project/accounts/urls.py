from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import online_users_view


urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register_view, name='register'),
    path('', views.landing_page, name='landing'),
    path('logout/', LogoutView.as_view(next_page='landing'), name='logout'),
]

urlpatterns += [
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/new/', views.blog_create, name='blog_create'),
    path('asignar-permiso/', views.asignar_permiso, name='asignar_permiso'),
    path('online-users/', online_users_view, name='online-users'),
]