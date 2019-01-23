from django.shortcuts import render
from realtors.models import Realtor


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    realtors = Realtor.objects.all().order_by('-hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
