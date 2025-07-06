from django.urls import path
from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView,
    RestaurantDeleteView,
)

app_name = 'proj'

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant_list'),
    path('<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('create/', RestaurantCreateView.as_view(), name='restaurant_create'),
    path('<int:pk>/update/', RestaurantUpdateView.as_view(),
         name='restaurant_update'),
    path('<int:pk>/delete/', RestaurantDeleteView.as_view(),
         name='restaurant_delete'),
]
