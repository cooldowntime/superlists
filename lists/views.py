from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    _list = List.objects.get(pk=list_id)
    return render(request, 'list.html', {'list': _list})


def new_list(request):
    _list = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=_list)
    try:
        item.full_clean()
    except ValidationError:
        _list.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(f'/lists/{_list.id}')


def add_item(request, list_id):
    _list = List.objects.get(pk=list_id)
    Item.objects.create(text=request.POST['item_text'], list=_list)
    return redirect(f'/lists/{_list.id}/')
