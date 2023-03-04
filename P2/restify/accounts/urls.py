from django.urls import path
from . import views

app_name="accounts"
urlpatterns = [ 
    path('<str:acc_type>/all/', views.all_users, name='all'),
    path('<str:username>/', views.user, name='user'),
    path('avatar/<str:username>/', views.user_avatar, name='user_avatar'),
    path('create/', views.CreateAccount.as_view(), name="create"),
    path('<str:username>/update/', views.UpdateUser.as_view(), name='update_user'),
    path('login', views.login, name="user_login"),
    path('logout', views.logout, name="user_logout")
]
