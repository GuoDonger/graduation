from user.views import user_login, user_register, user_logout, user_active, user_forget
from django.urls import path


app_name = 'user'
urlpatterns = [
    path('user_register/', user_register, name='user_register'),
    path('user_login/', user_login, name='user_login'),
    path('user_logout/', user_logout, name='user_logout'),
    path('user_forget/', user_forget, name='user_forget'),
    path('active/<str:code>/', user_active, name='user_active'),
]
