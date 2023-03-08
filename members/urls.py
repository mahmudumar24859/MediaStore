from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register_member', views.register, name='register'),
    path('login_member', views.custom_login, name='login'),
    path('logout_member', views.custom_logout, name='logout'),
    path('password_change', views.password_change, name='password_change'),
    path('password_reset', views.password_reset_request, name='password_reset'),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm,
         name='password_reset_confirm'),
    path('subscribe', views.subscribe, name='subscribe'),
]
