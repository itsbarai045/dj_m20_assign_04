from django import forms
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name']


class FilterCategoryForm(forms.Form):
    username = forms.ModelChoiceField(
        queryset=models.Category.objects.all(),
        widget=forms.TextInput(attrs={"placeholder": "Category",'class':'border rounded border-solid border-slate-300'})
        )


class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ['name', 'date', 'location', 'duration', 'desc','limit', 'category']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder': 'Name'}),
            'date':forms.DateInput(attrs={'placeholder': 'Date'}),
            'location':forms.TextInput(attrs={'placeholder': 'location'}),
            'duration':forms.NumberInput(attrs={'placeholder': 'duration'}),
            'desc':forms.Textarea(attrs={'placeholder': 'Detail','rows': 3}),
            'limit':forms.NumberInput(attrs={'placeholder': 'Set a Limit'}),
            'category':forms.Select(attrs={'placeholder': 'category'}),
        }