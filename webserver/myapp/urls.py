from django.urls import path
from .views import name_view, hobby_view, dream_view

urlpatterns = [
    path('name/', name_view, name='name'),
    path('hobby/', hobby_view, name='hobby'),
    path('dream/', dream_view, name='dream'),
]