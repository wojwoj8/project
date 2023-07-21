from django import forms
from .models import Expense, Category

# - means not (for views)
sort_choices = (
    ('date', 'Date (Ascending)'),
    ('-date', 'Date (Descending)'),
    ('category', 'Category (Ascending)'),
    ('-category', 'Category (Descending)'),
)

class ExpenseSearchForm(forms.ModelForm):
    from_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    to_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False, widget=forms.CheckboxSelectMultiple, to_field_name='name')
    sort_by = forms.ChoiceField(choices= sort_choices, required=False)
    
    class Meta:
        model = Expense
        fields = ('name', 'from_date', 'to_date', 'categories', 'sort_by' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['from_date'].required = False
        self.fields['from_date'].widget = forms.DateInput(attrs={'type': 'date', 'name': 'From'})
        self.fields['to_date'].required = False
        self.fields['to_date'].widget = forms.DateInput(attrs={'type': 'date', 'name': 'To'})
        # self.fields['sort_by']
        self.fields['categories'].required = False

