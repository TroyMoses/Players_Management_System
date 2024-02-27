from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('male_player/<int:pk>', views.male_player_record, name='male_player'),
    path('delete_player/<int:pk>', views.delete_player, name='delete_player'),
    path('add_male_player/', views.add_male_player, name='add_male_player'),
    path('update_male_player/<int:pk>', views.update_male_player, name='update_male_player'),
]

