from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseForbidden
from vacancy.models import Vacancy
from vacancy.forms import VacancyForm
from django.views.generic.edit import FormView


vacancy_form = VacancyForm()


class VacancyView(View):
    def get(self, request):
        vacancies = Vacancy.objects.filter()
        context = {"vacancies": vacancies}
        return render(request, "vacancy/vacancies.html", context=context)


class VacancyFormView(FormView):
    form_class = VacancyForm
    template_name = "vacancy/vacancy_new.html"
    success_url = "/vacancies"
    extra_context = {"vacancy_form": VacancyForm()}

    def post(self, request, *args, **kwargs):
        global vacancy_form
        vacancy_form = VacancyForm(request.POST)

        if not request.user.is_staff:
            return HttpResponseForbidden()

        if vacancy_form.is_valid():
            data = vacancy_form.cleaned_data
            Vacancy.objects.create(author=request.user, description=data["description"])
            return redirect('/vacancies')
        elif 'description' not in vacancy_form.cleaned_data:
            return HttpResponseForbidden()
