from django.urls import path
from .import views as sviews

urlpatterns = [
            path('',sviews.shopindex,name='shopindex'),
            path('about/',sviews.about,name='about'),
            path('contact/',sviews.contact,name='contact'),
            path('tracker/',sviews.tracker,name='tracker'),
            path('search/',sviews.search,name='search'),
            path('productview/',sviews.productview,name='productview'),
            path('checkout/',sviews.checkout,name='checkout'),
]