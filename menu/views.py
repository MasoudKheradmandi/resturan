from django.shortcuts import render
from .models import Food
from django.core.paginator import Paginator

# Create your views here.
def MenuView(request):
    Food_list =Food.objects.all()
    paginator = Paginator(Food_list, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        'posts':posts,
    }
    return render(request,'menu.html',context)


