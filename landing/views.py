from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

class RenderLandingView:
    
    def test(request):
        return HttpResponse('Página landing Page')