import graphene
from graphene_django import DjangoListField
from .graphql.mutations import CreateOrderMutation
from .graphql.queries import OrderTypes
from .models import Order
class Query(graphene.ObjectType):
    orders = DjangoListField(OrderTypes)
    order = DjangoListField(OrderTypes, id=graphene.ID())

    def resolve_order(cls, info, id):
        try:
            return Order.objects.filter(id=id)
        except Order.DoesNotExist:
            return None

class Mutation(graphene.ObjectType):
    create_order = CreateOrderMutation.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)