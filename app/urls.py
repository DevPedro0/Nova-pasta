from django.urls import path
from . import views



urlpatterns = [
    path('', views.RenderAppView.test, name='page_principal')
]
