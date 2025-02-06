from django.urls import path
from . import views

RenderAppFood = views.RenderAppView()

app_name = 'app'
urlpatterns = [
    path('', RenderAppFood.test, name='principal'),
    path('<slug:foods>/<int:id>/', RenderAppFood.filter_, name='preview'),
    path('category/<str:cat>/', RenderAppFood.filter_category, name='category-food')
]
