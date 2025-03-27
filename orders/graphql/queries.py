from graphene_django import DjangoObjectType
from ..models import Order

class OrderTypes(DjangoObjectType):
    class Meta:
        model = Order
        fields = "__all__"