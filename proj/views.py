from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Restaurant
from django.contrib import messages


class RestaurantCreateView(CreateView):
    model = Restaurant
    fields = ['name', 'address', 'cuisine']
    success_url = reverse_lazy('proj:restaurant_list')

    def form_valid(self, form):
        messages.success(self.request, "Restaurant created!")
        return super().form_valid(form)


class RestaurantListView(ListView):
    model = Restaurant
    context_object_name = 'restaurants'


class RestaurantDetailView(DetailView):
    model = Restaurant
    success_url = reverse_lazy('proj:restaurant_list')


class RestaurantUpdateView(UpdateView):
    model = Restaurant
    fields = ['name', 'address', 'cuisine']
    success_url = reverse_lazy('proj:restaurant_list')

    def form_valid(self, form):
        messages.success(self.request, "Restaurant updated!")
        return super().form_valid(form)


class RestaurantDeleteView(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('proj:restaurant_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Restaurant deleted!")
        return super().delete(request, *args, **kwargs)
