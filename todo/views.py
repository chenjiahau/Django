from django.shortcuts import render, HttpResponse, HttpResponseRedirect, Http404, get_object_or_404
from django.urls import reverse
from .models import User, Todo
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import TodoForm

# Iterable
LEVEL = [
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High')
]

# Create your views here.


class IndexView(ListView):
    model = Todo
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'
    ordering = ['-created_at', '-level']

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query[:3]

        return data


class ItemView(DetailView):
    model = Todo
    template_name = 'todo/item.html'
    context_object_name = 'item'


def item(request, item_id):
    try:
        item = get_object_or_404(Todo, pk=item_id)
    except:
        return HttpResponseRedirect(reverse('todo:index'))

    return render(request, 'todo/item.html', context={"item": item})


class CreateView(CreateView):
    template_name = 'todo/create.html'
    form_class = TodoForm
    model = Todo
    success_url = '/todo'

    def form_valid(self, form):
        try:
            form.save()
        except Exception as err:
            return render(
                self.request, 'todo/create.html',
                context={"form": form}
            )

        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        return render(
            self.request, 'todo/create.html',
            context={"form": form}
        )

# class CreateView(FormView):
#     template_name = 'todo/create.html'
#     form_class = TodoForm
#     model = Todo
#     success_url = '/todo'

#     def form_valid(self, form):
#         try:
#             form.save()
#         except Exception as err:
#             return render(
#                 self.request, 'todo/create.html',
#                 context={"form": form}
#             )

#         return HttpResponseRedirect(self.success_url)

#     def form_invalid(self, form):
#         return render(
#             self.request, 'todo/create.html',
#             context={"form": form}
#         )


def edit(request, item_id):
    try:
        item = Todo.objects.get(pk=item_id)
    except:
        return HttpResponseRedirect(reverse('todo:index'))

    if (request.method == 'POST'):
        form = TodoForm(request.POST)

        if (form.is_valid()):
            user = User.objects.get(pk=request.POST['user'])
            title = request.POST['title']
            description = request.POST['description']
            necessary_time = request.POST.get('necessary_time') == 'on'
            level = int(request.POST['level'])

            try:
                item.user = user
                item.title = title
                item.description = description
                item.necessary_time = necessary_time
                item.level = level
                item.save()
            except Exception as err:
                return render(
                    request, 'todo/create.html',
                    context={"form": form}
                )

            return HttpResponseRedirect(reverse('todo:index'))
        else:
            return render(
                request, 'todo/create.html',
                context={"form": form}
            )

    form = TodoForm(initial={
        "user": item.user.id,
        "title": item.title,
        "description": item.description,
        "level": item.level,
        "necessary_time": item.necessary_time,
        "completed": item.completed,
    })

    return render(
        request,
        'todo/edit.html',
        context={
            "item": item,
            "form": form
        }
    )
