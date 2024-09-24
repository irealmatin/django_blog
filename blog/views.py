from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm

class PostListView(generic.ListView):
    """
    displaying a list of published blog posts. It retrieves the posts from the database,
    filtering them by their status and ordering them by the date they were last modified.
    """
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        """
        Returns a queryset of Post objects that have a status of 'pub', ordered by datetime_modified in descending order.
        """
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    """
    displays the details of a single blog post. It uses the Post model to fetch the specific post that is being viewed.
    """
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    """
    used to create a new blog post
    """
    form_class = PostForm
    template_name = 'blog/post_create.html'


class PostUpdateView(generic.UpdateView):
    """
    allowing users to modify the details of a post.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'


class PostDeleteView(generic.DeleteView):
    """
    responsible for deleting a blog post. Upon successful deletion, it redirects the user to the list of posts.
    """
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')
