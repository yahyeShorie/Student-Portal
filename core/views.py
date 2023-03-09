from django.shortcuts import render, redirect
from item.models import Categories, Item

from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Categories.objects.all()
    context = {'categories':categories, 'items':items}
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'core/signup.html', context)