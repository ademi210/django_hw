from django .urls import path
from . import views


urlpatterns = [
    path('about_me/', views.about_me),
    path('favorite_animal/', views.favorite_animal),
    path('system_time/', views.system_time),
    ]
