from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Tag
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

def list_tags(request, page_num=1):
    tags = Tag.objects.all()
    paginator =Paginator(tags, 2)
    paged_tags = paginator.get_page(page_num)
    context = {'page': page_num, 'tags_list': paged_tags}
    return render(request, 'tags/list.html', context)


class TagCreate(CreateView):
    model = Tag
    fields = ['term', 'tags']

    def get_success_url(self):
        return reverse_lazy('tags:root')


class TagUpdate(UpdateView):
    model = Tag
    fields = ['tags']


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('tags:root')
