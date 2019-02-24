from django import forms
from .models import Day, Plans
class DayForm(forms.Form):
    Date = forms.DateField()

class DayModelForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ('day_made',)

class PlanForm(forms.Form):
    day = forms.ModelChoiceField(queryset = Day.objects.all())
    time_start = forms.TimeField()
    time_end = forms.TimeField()
    plan_title = forms.CharField(max_length= 20)
    plan_desc = forms.CharField(widget = forms.Textarea)

class PlanModelForm(forms.ModelForm):

    class Meta:
        model = Plans
        fields = ('plan_title','time_start', 'time_end', 'plan_description','plan_tag')
