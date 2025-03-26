import graphene
from graphene_django import DjangoListField
from .graphql.queries import CategoryTypes, MenuItemTypes
from .graphql.mutations import CreateCategoryMutation, CreateMenuItemMutation

class Query(graphene.ObjectType):
    categories = DjangoListField(CategoryTypes)
    menu_items = DjangoListField(MenuItemTypes)

class Mutation(graphene.ObjectType):
    create_category = CreateCategoryMutation.Field()
    create_menu_item = CreateMenuItemMutation.Field()

    


schema = graphene.Schema(query=Query, mutation=Mutation)