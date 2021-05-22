
from django.urls import path
from . import view

urlpatterns = [
    path('', view.homepage, name='home'),
    path('counttheword/', view.count, name='count'),
    path('AboutPage/', view.about, name='about'),
]
