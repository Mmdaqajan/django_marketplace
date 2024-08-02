# todo learn how to say mig insteadof 'python manage.py makemigrations'
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import SignUpForm, LoginFrom, NewItemForm, EditItemForm
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


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            # this commit=False makes change not to save in database cause the created by field is empty
            # we should fill it then save item into database
            item.created_by = request.user
            item.save()
            return redirect('detail_page', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'core/new_item.html', {
        'form': form,
        'title': 'New Item'
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index_page')


def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

        return redirect('detail_page', pk=item.id)

    else:
        form = EditItemForm(instance=item)

    return render(request, 'core/new_item.html', {
        'form': form,
        'title': 'Edit Item'
    })


def browse(request):
    items = Item.objects.filter(is_sold=False)

    return render(request, 'core/brows.html', {
        'items': items,
    })

# todo learn how to logout via django internal function
