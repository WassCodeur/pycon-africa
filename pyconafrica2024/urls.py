from django.urls import path
from . import views

app_name = 'pyconafrica2024'

urlpatterns = [
    path('', views.home24, name='home24'),
    path('about/', views.about, name='about'),
    path('team/', views.teams, name='teams'),
    path('travel/', views.travel, name='travel'),
    path('coc/', views.coc, name='coc'),
    path('fin-aid/', views.fin_aid, name='fin_aid'),
    path('health-safety/', views.health_safety_guidelines, name='health_safety_guidelines'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('schedule/', views.schedule24, name='schedule24'),
    path('speakers/', views.speakers, name='speakers'),
    path('our-sponsors/', views.sponsors, name='sponsors'),
    path('sponsor-us/', views.sponsor_us, name='sponsor_us'),
    path('talks/', views.talks, name='talks'),
    path('tickets/', views.tickets, name='tickets'),
]
