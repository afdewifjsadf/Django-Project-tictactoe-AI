from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import  login_required
from . import  views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name='myapp'
urlpatterns = [
    # path('', views.index, name="index"),
    # path('', include('django.contrib.auth.urls')),
    path('', views.index , name="index"),
    path('login/',views.loginPage, name="login"),
    path('register/',views.registerPage, name="register"),
    path('logout/',views.logoutUser, name="logout"),
    path('profile/', views.profile, name='profile'),
    path('crate_game/', views.createGame, name='createGame'),
    path('account/', views.accountPage, name="account"),
    path('learn/', views.learn, name='learn'),
    path('learn_ttt/', views.learn_ttt, name='learn_ttt'),
    path('learn_profile/', views.learn_profile, name='learn_profile'),
    path('leaderboard/', views.leaderboardPage, name="leaderboard" ),
    
    # reset_password
    #     path('reset_password/',
    #  auth_views.PasswordResetView.as_view(),
    #  name="reset_password"),


    path('password_reset/', 
    auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        success_url=reverse_lazy('myapp:password_reset_done')
    ), 
    name='password_reset'),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_sent.html'
        ), 
        name="password_reset_done"),

    path('password_reset_<uidb64>_<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_form.html",
            success_url=reverse_lazy('myapp:password_reset_complete')
     ), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_done.html"
        ), 
        name="password_reset_complete"),

]
