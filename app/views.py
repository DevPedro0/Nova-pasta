from django.shortcuts import render
from . import models

class RenderAppView:
    
    
    
    
    def test(request):
        context = {
           'template_food': models.ModelFood.objects.all()
        }
        
        return render(
            request, 
            'pages/index.html',
            context= {'app_food': context }
        )