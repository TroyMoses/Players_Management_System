from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('male_player_record/<int:pk>', views.male_player_record, name='male_player_record'),
    path('female_player_record/<int:pk>', views.female_player_record, name='female_player_record'),
    path('delete_male_player/<int:pk>', views.delete_male_player, name='delete_male_player'),
    path('delete_female_player/<int:pk>', views.delete_female_player, name='delete_female_player'),
    path('add_male_player/', views.add_male_player, name='add_male_player'),
    path('add_female_player/', views.add_female_player, name='add_female_player'),
    path('update_female_player/<int:pk>', views.update_female_player, name='update_female_player'),
]

