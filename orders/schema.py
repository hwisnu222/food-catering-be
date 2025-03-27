import graphene
from graphene_django import DjangoListField
from .graphql.mutations import CreateOrderMutation
from .graphql.queries import OrderTypes
class Query(graphene.ObjectType):
    orders = DjangoListField(OrderTypes)

class Mutation(graphene.ObjectType):
    create_order = CreateOrderMutation.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)