from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Review, Cottage
from .forms import ReviewForm


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_create.html'

    def form_valid(self, form):

        form.instance.user = self.request.user
        form.instance.cottage = get_object_or_404(Cottage, pk=self.kwargs['cottage_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('cottage_detail', kwargs={'pk': self.kwargs['cottage_id']})



class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_update.html'

    def get_success_url(self):
        return reverse_lazy('cottage_detail', kwargs={'pk': self.object.cottage.id})

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user



class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_delete.html'

    def get_success_url(self):
        return reverse_lazy('cottage_detail', kwargs={'pk': self.object.cottage.id})

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user