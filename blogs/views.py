from django.views import generic
from django.urls import reverse_lazy
from .models import Post

# Create your views here.

class IndexVire(generic.ListView):
    model = Post
    paginate_by = 5
    ordering = ['-updated_at']
    template_name = 'blogs/index.html'

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/detail.html'

class CreateView(generic.edit.CreateView):
    model = Post
    fields = '__all__'
    template_name = 'blogs/create.html'

class UpdateView(generic.edit.UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'blogs/update.html'

class DeleteView(generic.edit.DeleteView):
    model = Post
    success_url = reverse_lazy('blogs:index')
    template_name = 'blogs/delete.html'
