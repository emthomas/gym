from tastypie.resources import ModelResource
from api.models import Budget, Expense
from tastypie.authorization import Authorization
from tastypie import fields


class BudgetResource(ModelResource):
    class Meta:
        queryset = Budget.objects.all()
        resource_name = 'budget'
        authorization = Authorization()


class ExpenseResource(ModelResource):
    budget = fields.ForeignKey(BudgetResource, 'budget')

    class Meta:
        queryset = Expense.objects.all()
        resource_name = 'expense'
        authorization = Authorization()
