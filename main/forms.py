from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','category', 'priority', 'description', 'due_date', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter todo title'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select category'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select priority'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description',
                'rows': 3
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }