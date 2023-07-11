from django.shortcuts import render
from cart import models
from django.db.models import Q

# Create your views here.

def search_view(request):
    res = []
    q = None
    if request.method == 'POST':
        q = request.POST.get('q')
        orders = models.Order.objects.filter(Q(phone__icontains=q))
        for i in orders:
            res.append((i.phone, i.get_search_url))
    context = {'results': res, 'q': q}
    context['search_results'] = []
    return render(
        request, 
        template_name='search/search_results.html', 
        context=context)