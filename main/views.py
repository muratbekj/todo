from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Todo
from .forms import TodoForm
from django.urls import reverse_lazy
import logbook

logger = logbook.Logger('__name__')

# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
            )
        if category:
            queryset = queryset.filter(category__name__iexact=category)
            
        return queryset.order_by('-created_date')
        

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/todo_detail.html'
    context_object_name = 'todo'
    def get(self, request, *args, **kwargs):
        todo = self.get_object()
        template_name = 'todo/todo_detail.html'
        context = {
            'todo': todo
        }
        return render(request, template_name, context)
    
class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo/todo_create.html'
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo/todo_update.html'
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/todo_delete.html'
    success_url = reverse_lazy('todo_list')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)
    