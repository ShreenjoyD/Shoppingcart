from django.urls import path
from .import views

app_name='maincart'

urlpatterns=[
    path('', views.index, name='index'),
    path('presults/', views.presults, name='presults'),
    #path('addtocart/id(\d+)/', views.addtocart, name='addtocart'),
    path('<int:id>', views.purchase, name='purchase'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('streamcsv/', views.streamcsv, name='streamcsv')
]
