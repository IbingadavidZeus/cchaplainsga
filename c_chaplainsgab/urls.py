from django.urls import path
from .views import *  # Import de la vue

urlpatterns = [
    path('', home, name='home'),  # Route pour la page d'accueil
    path('activites', about, name='about'),  # Route pour la page "À propos" (ajoutez cette ligne si vous avez une vue pour cela)
    path('be_volunteer', be_volunteer, name='be_volunteer'),  # Route pour la page "Devenir bénévole"
    path('contact', contact, name='contact'),  # Route pour la page de contact
    path('a_propos', a_propos, name='a_propos'),  # Route pour la page "À propos"
    path('donate', donate, name='donate'),  # Route pour la page de don
]
