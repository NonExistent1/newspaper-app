from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse, reverse_lazy


from .models import Article
from .forms import CommentForm

class ArticleListView(LoginRequiredMixin, ListView):
    """article list view"""
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(LoginRequiredMixin, View):
    """Article Detail View"""

    def get(self, request, *args, **kwargs):
        """Doing GET request"""
        view = CommentGetView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Doing POST request"""
        view = CommentPostView.as_view()
        return view(request, *args, **kwargs)

class CommentGetView(DetailView):
    """Comment Get View"""

    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        """Get the context data for the template"""
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
class CommentPostView(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        # Get the Article object associated with the pk in the URL
        self.object = self.get_object()
        # Do work parent would have
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        """Create new comment when form is valid"""
        # Get the comment instance by saving the form, but set commit to False
        # as we don't want the form to fully save the model to the database yet
        comment = form.save(commit=False)
        # attach article to the new comment
        comment.article = self.object
        # attach author to new comment
        comment.author = self.request.user
        # save comment to database
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        """Get the success URL"""
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk" : article.pk})

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
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Article Delete View"""

    model = Article 
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user