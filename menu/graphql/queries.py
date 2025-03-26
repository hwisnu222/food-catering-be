from ..models import Category, MenuItem
from graphene_django import DjangoObjectType

class CategoryTypes(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'


class MenuItemTypes(DjangoObjectType):
    class Meta:
        model = MenuItem
        fields = '__all__' 

