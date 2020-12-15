from django.urls import path
from .views import *


urlpatterns = [
    path('',homePage , name = 'homePage'),
    path('signup/',signup , name = 'signup'),
    path('signin/',signin , name = 'signin'),
    path('logoutView/',logoutView , name = 'logoutView'),

    path('search/',search , name = 'search'),

    path('myCart/',myCart , name = 'myCart'),
    path('product/<int:id>/',productPage,name='productPage'),

    path('addToCart/<int:id>/',addToCart,name="addToCart"),
    # path('myCart/addToCart/<int:id>/',addToCart,name="addToCart"),
    path('myCart/removeFromCart/<int:id>/',removeFromCart,name="removeFromCart"),
    path('product/<int:id>/addToMyOrder/',addToMyOrder,name="addToMyOrder"),

    path('myOdrers/',myOrdersPage,name='myOrdersPage'),
    path('myOdrers/addRatingandReview/<int:id>',addRatingandReview,name='addRatingandReview'),

]