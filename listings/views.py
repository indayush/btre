from django.shortcuts import render
from django.shortcuts import get_object_or_404
from listings.choices import price_choices, bedroom_choices, state_choices

from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # order_by('-list_date') = views the listings according to the date they were published. Last In First Out
    # filter(is_published=True) = Filter data according to the is_published value in the DB

    
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render (request,'listings/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context= {
        'listing' : listing
    }
    
    return render (request,'listings/listing.html',context)

def search(request):

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
        
    }
    return render (request,'listings/search.html',context)

