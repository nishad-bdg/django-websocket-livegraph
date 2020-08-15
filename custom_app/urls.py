from django.urls import path

from custom_app import views
urlpatterns = [
    path('',views.home,name="home"),
]