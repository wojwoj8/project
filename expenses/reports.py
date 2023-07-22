from collections import OrderedDict

from django.db.models import Sum, Value, Count
from django.db.models.functions import Coalesce, TruncMonth
from .models import Expense, Category


def summary_per_category(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))


def summary_per_yearmonth(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(month=TruncMonth('date'))
        .order_by()
        .values('month')
        .annotate(s=Sum('amount'))
        .values_list('month', 's')
    ))

def expenses_per_category(queryset):
    return (sorted(
        queryset
        .annotate(expense_count=Coalesce(Count('expense'), 0))
        .values_list('name', 'expense_count', 'id')
    ))
    