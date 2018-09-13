from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('logout-then-login/', logout_then_login, name='logout_then_login'),
    # path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/confirm/', PasswordResetConfirmView.as_view(), 'password_reset_confirm'),
    # path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]