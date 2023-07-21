from django import forms
from .models import Expense, Category


class ExpenseSearchForm(forms.ModelForm):
    from_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    to_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False, widget=forms.CheckboxSelectMultiple, to_field_name='name')

    
    class Meta:
        model = Expense
        fields = ('name', 'from_date', 'to_date', 'categories' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['from_date'].required = False
        self.fields['from_date'].widget = forms.DateInput(attrs={'type': 'date', 'name': 'From'})
        self.fields['to_date'].required = False
        self.fields['to_date'].widget = forms.DateInput(attrs={'type': 'date', 'name': 'To'})
       
        self.fields['categories'].required = False

