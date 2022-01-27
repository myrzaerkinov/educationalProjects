# import requests
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import parser, models, forms

# class ParserFormView(FormView):
#     template_name = "parser.html"
#     form_class = forms.ParserForm
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.parse_data()
#             return HttpResponse('Parser Success')
#             # return redirect(reverse("parse:list_objects"))
#         else:
#             return super(ParserFormView, self).post(request, *args, **kwargs)
#

class FilmView(ListView):
    model = models.Film
    template_name = 'parser_list.html'

    def get_queryset(self):
        return models.Film.objects.all()

class ParserFilmView(FormView):
    template_name = 'parser.html'
    form_class = forms.ParserForm


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Parser Success')
        else:
            return super(ParserFilmView, self).post(request, *args, **kwargs)

