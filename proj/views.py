from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Restaurant, Customer, MenuItem, Order, OrderItem
from rest_framework import viewsets, permissions
from .serializers import (
    RestaurantSerializer,
    CustomerSerializer,
    MenuItemSerializer,
    OrderSerializer,
    OrderItemSerializer
)


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    model = Restaurant
    fields = ['name', 'address', 'cuisine']
    success_url = reverse_lazy('proj:restaurant_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Restaurant created!")
        return super().form_valid(form)


class RestaurantListView(LoginRequiredMixin, ListView):
    model = Restaurant
    context_object_name = 'restaurants'


class RestaurantDetailView(LoginRequiredMixin, DetailView):
    model = Restaurant
    success_url = reverse_lazy('proj:restaurant_list')


class RestaurantUpdateView(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
    model = Restaurant
    fields = ['name', 'address', 'cuisine']
    success_url = reverse_lazy('proj:restaurant_list')

    def form_valid(self, form):
        messages.success(self.request, "Restaurant updated!")
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class RestaurantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Restaurant
    success_url = reverse_lazy('proj:restaurant_list')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows YourModel objects to be viewed or edited.
    Provides list, create, retrieve, update, partial_update, destroy actions.
    """
    queryset = Restaurant.objects.all().order_by('-id')  # Or appropriate ordering
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by('-id')
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-order_date')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all().order_by('-id')
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
