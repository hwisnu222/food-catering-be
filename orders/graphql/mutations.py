import graphene
from .queries import OrderTypes
from ..models import Order
from menu.models import MenuItem
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

class OrderInput(graphene.InputObjectType):
    name=graphene.String()
    menu_item_id = graphene.ID()
    phone_number = graphene.String()
    delivery_date = graphene.DateTime()
    delivery_address = graphene.String()
    special_notes = graphene.String()

class CreateOrderMutation(graphene.Mutation):
    class Arguments:
        data = OrderInput()
    
    order = graphene.Field(OrderTypes)

    @classmethod
    def mutate(cls, root, info, data):
        try:
            menu_item_instance = MenuItem.objects.get(id=data.menu_item_id)
        except ObjectDoesNotExist:
            raise Exception("menu is not exist")

        try:
            data.menu_item = menu_item_instance
            order = Order(**data)

            return CreateOrderMutation(order=order)
        except Order.DoesNotExist:
            return Order(order=None)