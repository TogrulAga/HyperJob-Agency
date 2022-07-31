from django.shortcuts import render
from django.views import View
from resume.models import Resume
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from resume.forms import ResumeForm
from django.views.generic.edit import FormView


resume_form = ResumeForm()


class ResumeView(View):
    def get(self, request):
        resumes = Resume.objects.filter()
        context = {"resumes": resumes}
        for resume in resumes:
            print(type(resume.description))

        return render(request, "resume/resumes.html", context=context)


class ResumeFormView(FormView):
    form_class = ResumeForm
    template_name = "resume/resume_new.html"
    success_url = "/resumes"
    extra_context = {"resume_form": ResumeForm()}

    def post(self, request, *args, **kwargs):
        global resume_form

        resume_form = ResumeForm(request.POST)
        if resume_form.is_valid():
            data = resume_form.cleaned_data
            Resume.objects.create(author=request.user, description=data["description"])
            return redirect('/resumes')
        elif 'description' not in resume_form.cleaned_data:
            print("Description is not valid")
            return HttpResponseForbidden()