from django.urls import path
from . import views
#что такое точка?

urlpatterns = [
    path("", views.index, name="index")
    #главная страница - вью "индекс"
]