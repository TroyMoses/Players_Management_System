from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('player/<int:pk>', views.player_record, name='player'),
    path('delete_player/<int:pk>', views.delete_player, name='delete_player'),
    path('add_player/', views.add_player, name='add_player'),
    path('update_player/<int:pk>', views.update_player, name='update_player'),
]

