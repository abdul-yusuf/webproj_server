from django.urls import path
from .views import GallaryView, HomeView, CarearView

app_name = 'core'

urlpatterns = [
    path('', HomeView, name='home-view'),
    path('carear', CarearView, name='carear-view'),
    path('gallary', GallaryView, name='gallary-view')
]
