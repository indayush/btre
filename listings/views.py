from django.shortcuts import render
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
    return render (request,'listings/listings.html')

def search(request):
    return render (request,'listings/search.html')

