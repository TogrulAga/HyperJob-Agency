from django.forms import ModelForm
from vacancy.models import Vacancy


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['description']
