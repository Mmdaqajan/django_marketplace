# todo learn how to say mig insteadof 'python manage.py makemigrations'

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import SignUpForm, LoginFrom
from core.models import Item, Category


# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, 'core/index.html', context)


def contact(request):
    context = {}
    return render(request, 'core/contact.html', context)


def detail(request, pk):
    # item = Item.objects.get_object_or_404(id=pk)
    item = get_object_or_404(Item, id=pk)
    related_item = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)
    context = {
        'item': item,
        'related_item': related_item,
    }
    return render(request, 'core/detail.html', context)


def signup(request):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            return redirect(reverse('login_page'))
    else:
        sign_up_form = SignUpForm()

    context = {
        'sign_up_form': sign_up_form,
    }
    return render(request, 'core/signup.html', context)


# todo learn how to logout via django internal function
