from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Restaurant


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
