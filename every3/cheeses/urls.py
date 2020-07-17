from django.urls import path
from . import views
from .views import CheeseListView

app_name = "cheeses"
 
urlpatterns = [
    path(
        route = "", 
        view = views.CheeseListView.as_view(),
        name='list'
    ),
]
 