from . import parser, models
from django import forms

# class ParserForm(forms.Form):
#     MEDIA_CHOICES = (
#         ('ANIME', 'ANIME'),
#     )
#     media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
#
#     class Meta:
#         fields = [
#             'media_type',
#         ]
#
#     def parse_data(self):
#         if self.data['media_type'] == 'ANIME':
#             anime_parser = parser.parser()
#             for i in anime_parser:
#                 models.Film.objects.create(**i)

#
# from django import forms
# from parser_app import parser, models


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('FILM', 'FILM'),
    )
    media_choice = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_choice',
        ]

    def parser_data(self):
        if self.data['media_choice'] == 'FILM':
            films_data = parser.films_parser()
            for i in films_data:
                models.Film.objects.create(**i)
