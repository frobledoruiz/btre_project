from django.shortcuts import render
from realtors.models import Realtor

from listings.models import Listing


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[0:3]

    context = {
        'listings': listings,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.all().order_by('-hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
