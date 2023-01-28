from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Demmy
from .forms import DemmyForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class Tasklistview(ListView):
    model = Demmy
    template_name = 'home.html'
    context_object_name = 'demmy'


class Taskdetailview(DetailView):
    model = Demmy
    template_name = 'detail.html'
    context_object_name = 'i'


class TaskUpdateView(UpdateView):
    model = Demmy
    template_name = 'update.html'
    context_object_name = 'demmy'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Demmy
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def add(request):
    demmy = Demmy.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Demmy(name=name, priority=priority, date=date)
        task.save()

    return render(request, 'home.html', {'demmy': demmy})


def delete(request, taskid):
    demmy = Demmy.objects.get(id=taskid)
    if request.method == 'POST':
        demmy.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    demmy = Demmy.objects.get(id=id)
    form = DemmyForm(request.POST or None, instance=demmy)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'demmy': demmy})
