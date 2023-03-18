from django_filters import rest_framework as filters
from .models import ToDo


class ToDoFilter(filters.FilterSet):
    created = filters.DateFromToRangeFilter()

    class Meta:
        model = ToDo
        fields = ['proj', 'created']
