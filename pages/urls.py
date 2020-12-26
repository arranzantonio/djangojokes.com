from django.urls import path

from .views import HomeView, AboutUsView

app_name = 'pages'
urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('about_us/', AboutUsView.as_view(),name='about_us'),
]