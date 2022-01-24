from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from . import models, forms
from django.views import generic
from . import models


class BookListView(generic.ListView):
    template_name = 'book_list.html'
    queryset = models.Genre.objects.all()

    def get_queryset(self):
        return models.Genre.objects.all()


# def book_all(request):
#     books = models.Genre.objects.all()
#     return render(request, 'book_list.html', {'books': books})


class BookDetailView(generic.DetailView):
    template_name = "book_detail.html"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Genre, id=books_id)


# def book_detail(request, id):
#     book = get_object_or_404(models.Genre, id=id)
#     return render(request, 'book_detail.html', {'book': book})


class BookCreateView(generic.CreateView):
    template_name = "add_book.html"
    form_class = forms.BookForm
    queryset = models.Genre.objects.all()
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)


# def add_book(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Book created')
#     else:
#         form = forms.BookForm()
#     return render(request, 'add_book.html', {'form': form})


class BookUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, *kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Genre, id=books_id)

    def form_valid(self, form):
        return super(BookUpdateView, self).form_valid(form=form)


# def book_update(request, id):
#     book_object = get_object_or_404(models.Genre, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(instance=book_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Book Updated Successfully')
#             # return redirect(reverse("books:book_all"))
#     else:
#         form = forms.BookForm(instance=book_object)
#     return render(request, 'book_update.html', {'form': form, 'object': book_object})


class BookDeleteView(generic.DeleteView):
    template_name = "delete_book.html"
    success_url = '/books/'

    def get_object(self, *kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Genre, id=books_id)


# def book_delete(request, id):
#     book_delete = get_object_or_404(models.Genre, id=id)
#     book_delete.delete()
#     return HttpResponse('Book Deleted')





class ExpertRecomendation(generic.ListView):
    template_name = "book_detail.html"
    queryset = models.Genre.objects.all()

    def get_queryset(self):
        return models.Genre.objects.all()

