from django.urls import path
from . import views
urlpatterns = [
    path('',views.index_vista, name='index.html ')
]
