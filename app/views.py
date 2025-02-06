from django.shortcuts import render, get_list_or_404


from . import models

class RenderAppView:
    
    context = {
        'app_food': models.ModelFood.objects.all(),
        'app_user': models.Author.objects.all(),
        'app_test': 'Pedro'
    }
    
    
    def test(self, request):
        return render(
            request, 
            'pages/index.html',
            context= {'context_app_food': self.context}
        )
        
    @staticmethod
    def filter_(request, foods, id):
        
        food = get_list_or_404(models.ModelFood, slug = foods, pk = id)
        
        return render(
            request,
            'pages/list_filter.html',
            context= {'context_app_food': food}
        )
        
    @staticmethod
    def filter_category(request, cat):
        
        food_filter = get_list_or_404(
            models.ModelFood.objects.filter(
            category_food__category = cat, 
        ).order_by('-id')
        
        )
        
        
        return render(
            request, 
            'pages/filter_category.html',
            context= {
                'context_app_food': food_filter            
            }           
        )