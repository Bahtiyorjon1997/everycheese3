from django.urls import path
from . import views
from .views import CheeseListView, CheeseDetailView

app_name = "cheeses"
 
urlpatterns = [
    path(
        route = "", 
        view = views.CheeseListView.as_view(),
        name='list'
    ),
    path(
        route = "<slug:slug>/",
        view = views.CheeseDetailView.as_view(),
        name = "detail",
    ),
]
 