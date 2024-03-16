from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


from .models import Article

class ArticleListView(LoginRequiredMixin, ListView):
    """article list view"""
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(LoginRequiredMixin, DetailView):
    """Article Detail View"""

    model = Article
    template_name = "article_detail.html"

class ArticleCreateView(LoginRequiredMixin, CreateView):
    """Article Create View"""

    model = Article
    template_name = "article_new.html"
    fields=(
        "title",
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Article Update View"""

    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

    def test_func(self):
        obj = self.get.object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Article Delete View"""

    model = Article 
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    
    def test_func(self):
        obj = self.get.object()
        return obj.author == self.request.user