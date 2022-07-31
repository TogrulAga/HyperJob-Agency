from django.forms import ModelForm
from resume.models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['description']
