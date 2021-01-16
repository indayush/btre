from django.urls import path
from . import views as views

urlpatterns = [
     path('',views.index, name='listings'),                                                 # For /listings/ page
     path('<int:listing_id>',views.listing, name='listing'),                                # For listings/4 page
     path('search',views.search, name='search'),                                            # For search handling on page
     
]
