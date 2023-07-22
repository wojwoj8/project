from django.views.generic.list import ListView

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category, summary_per_yearmonth


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            from_date =  form.cleaned_data.get("from_date")
            to_date = form.cleaned_data.get('to_date')
            categories = form.cleaned_data.get('categories')
            sort_by = form.cleaned_data.get('sort_by')

            

            # print(f'From: {from_date}, To: {to_date}')
            # print(f'Categories: {categories}')
            # print(f'{sort_by}')

            if name:
                queryset = queryset.filter(name__icontains=name)
            if from_date and to_date:
                queryset = queryset.filter(date__range=(from_date, to_date))
            elif from_date:
                queryset = queryset.filter(date__gte=from_date)
            elif to_date:
                queryset = queryset.filter(date__lte=to_date)
            if categories:
                queryset = queryset.filter(category__in=categories)
            if sort_by:
                queryset = queryset.order_by(sort_by)
            
            # calculate total amount for queryset
            total_amount = 0
            summary_data = summary_per_category(queryset)
            for value in summary_data.values():
                total_amount += value    

            print(total_amount)

        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            total_amount=total_amount,
            summary_per_yearmonth=summary_per_yearmonth(queryset),
            **kwargs)

class CategoryListView(ListView):
    model = Category
    paginate_by = 5

