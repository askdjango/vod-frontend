from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render, resolve_url
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework.renderers import JSONRenderer
from .forms import CommentForm
from .models import Post, Comment
from .serializers import PostSerializer


class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_template_names(self):
        if self.request.is_ajax():
            return ['blog/_post_list.html']
        return ['blog/index.html']

index = PostListView.as_view()

post_new = CreateView.as_view(model=Post, fields='__all__')


class PostDetailView(DetailView):
    model = Post

    def render_to_response(self, context):
        if self.request.is_ajax():
            return JsonResponse({
                'title': self.object.title,
                'summary': truncatewords(self.object.content, 100),
            })
        # 템플릿 렌더링
        return super().render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

post_detail = PostDetailView.as_view()


post_edit = UpdateView.as_view(model=Post, fields='__all__')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')

post_delete = PostDeleteView.as_view()


class CommentListView(ListView):
    model = Comment

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(post__id=self.kwargs['post_pk'])
        return qs


comment_list = CommentListView.as_view()

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        response = super().form_valid(form)

        if self.request.is_ajax(): # render_to_response가 호출되지 않습니다.
            return render(self.request, 'blog/_comment.html', {
                'comment': comment,
            })

        return response


    def get_success_url(self):
        return resolve_url(self.object.post)

    def get_template_names(self):
        if self.request.is_ajax():
            return ['blog/_comment_form.html']
        return ['blog/comment_form.html']

comment_new = CommentCreateView.as_view()


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.request.is_ajax(): # render_to_response가 호출되지 않습니다.
            return render(self.request, 'blog/_comment.html', {
                'comment': self.object,
            })

        return response

    def get_success_url(self):
        return resolve_url(self.object.post)

    def get_template_names(self):
        if self.request.is_ajax():
            return ['blog/_comment_form.html']
        return ['blog/comment_form.html']

comment_edit = CommentUpdateView.as_view()


class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        return resolve_url(self.object.post)

comment_delete = CommentDeleteView.as_view()


def post_list_json(request):
    qs = Post.objects.all()

    serializer = PostSerializer(qs, many=True)
    json_utf8_string = JSONRenderer().render(serializer.data)

    return HttpResponse(json_utf8_string, content_type='application/json; charset=utf-8') # 커스텀 지정

