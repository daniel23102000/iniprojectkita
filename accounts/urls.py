from django.urls import path
from.import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.indexView, name='home'),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('register/login.url',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
    path('composers/', views.list_composers, name='composers'),
    path('composer/add', views.add_composer, name='add_composer'),
    path('composer/edit/<int:composer_id>', views.edit_composer, name='edit_composer'),
    path('composer/delete/<int:composer_id>', views.delete_composer, name='delete_composer'),
    path('singers/', views.list_singers, name='singers'),
    path('singer/add', views.add_singer, name='add_singer'),
    path('singer/edit/<int:singer_id>', views.edit_singer, name='edit_singer'),
    path('singer/delete/<int:singer_id>', views.delete_singer, name='delete_singer'),
    path('genres/', views.list_genres, name='genres'),
    path('genre/add', views.add_genre, name='add_genre'),
    path('genre/edit/<int:genre_id>', views.edit_genre, name='edit_genre'),
    path('genre/delete/<int:genre_id>', views.delete_genre, name='delete_genre'),
    path('countrys/', views.list_countrys, name='countrys'),
    path('country/add', views.add_country, name='add_country'),
    path('country/edit/<int:country_id>', views.edit_country, name='edit_country'),
    path('country/delete/<int:country_id>', views.delete_country, name='delete_country'),
    path('citys/', views.list_citys, name='citys'),
    path('city/add', views.add_city, name='add_city'),
    path('city/edit/<int:country_id>', views.edit_city, name='edit_city'),
    path('city/delete/<int:city_id>', views.delete_city, name='delete_city'),
    path('dashboard/', views.list_musictitles, name='musictitles'),
    path('dashboard/add/', views.add_musictitle, name='add_musictitle'),
    path('dashboard/edit/<int:musictitle_id>', views.edit_musictitle, name='edit_musictitle'),
    path('dashboard/delete/<int:musictitle_id>', views.delete_musictitle, name='delete_musictitle'),

]