from django.shortcuts import render

def cars_view(request):
    return render(request ,template_name='cars.html')