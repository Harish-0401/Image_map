from django.shortcuts import render

def img_view(request):
    return render(request, 'img.html')

def bodi(request):
    return render(request,'bodi.html')

def vira(request):
    return render(request, 'virapandi.html') 

def boothi(request):
    return render (request, 'boothi.html')


def meena(request):
    return render (request, 'meenachipuram.html')

