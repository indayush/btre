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

    queryset_List = Listing.objects.order_by('-list_date')
    
    # Different sections acc to searchable items. Refer HTML for more understranding
    
    # For Keywords - String/text field
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_List = queryset_List.filter(description__icontains=keywords)

    # For City - String/text field
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_List = queryset_List.filter(city__iexact=city)

    # For State - String/text field
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_List = queryset_List.filter(state__iexact=state)

    # For Bedrooms - Number
    # lte = Less than or Equal To
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_List = queryset_List.filter(bedrooms__lte=bedrooms)

    # For Price - Number
    # lte = Less than or Equal To
    if 'price' in request.GET:
        price = request.GET['price']
        # print(price) Logging is visible on Server Logs
        if price:
            queryset_List = queryset_List.filter(price__lte=price)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': queryset_List,
        'values': request.GET        
    }
    
    return render (request,'listings/search.html',context)

