from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from . import models, forms
from django.views import generic

class ShowsListView(generic.ListView):
    template_name = "shows_list.html"
    queryset = models.TVShow.objects.all()

    def get_queryset(self):
        return models.TVShow.objects.filter().order_by("-id")



# def shows_all(request):
#     shows = models.TVShow.objects.all()
#     return render(request, 'shows_list.html', {'shows': shows})

class ShowsDetailView(generic.DetailView):
    template_name = "shows_detail.html"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.TVShow, id=shows_id)




# def shows_detail(request, id):
#     show = get_object_or_404(models.TVShow, id=id)
#     return render(request, 'shows_detail.html', {'show': show})

class ShowsCreateView(generic.CreateView):
    template_name = 'add_shows.html'
    form_class = forms.ShowForm
    queryset = models.TVShow.objects.all()
    success_url = "/shows/"

    def form_valid(self, form):
        print(form.cleaned_date)
        return super(ShowsCreateView, self).form_valid(form=form)


# def add_show(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.ShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Show created')
#     else:
#         form = forms.ShowForm()
#     return render(request, 'add_shows.html', {'form': form})


class ShowsUpdateView(generic.UpdateView):
    template_name = "show_update.html"
    form_class = forms.ShowForm
    success_url = "/shows/"

    def get_object(self, *kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.TVShow, id=shows_id)

    def form_valid(self, form):
        return super(ShowsUpdateView, self).form_valid(form=form)



# def show_update(request, id):
#     show_object = get_object_or_404(models.TVShow, id=id)
#     if request.method == 'POST':
#         form = forms.ShowForm(instance=show_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             # return HttpResponse('Show Updated Successfully')
#             return redirect(reverse("shows:shows_all"))
#     else:
#         form = forms.ShowForm(instance=show_object)
#     return render(request, 'show_update.html', {'form': form, 'object': show_object})


class ShowsDeleteView(generic.DeleteView):
    template_name = "confirm_delete_show.html"
    success_url = '/shows/'

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.TVShow, id=shows_id)



# def show_delete(request, id):
#     show_object = get_object_or_404(models.TVShow, id=id)
#     show_object.delete()
#     return HttpResponse('Show Deleted')


