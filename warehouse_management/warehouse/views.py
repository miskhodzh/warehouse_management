from django.shortcuts import render


def add(request):
    template = 'warehouse/add.html'
    return render(request, template)

def product_list(request):
    template = 'warehouse/list.html'
    return render(request, template)

