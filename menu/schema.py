import graphene
from graphene_django import DjangoListField
from .graphql.queries import CategoryTypes, MenuItemTypes
from .graphql.mutations import CreateCategoryMutation, CreateMenuItemMutation, DeleteMenuItemMutation, UpdateMenuItemMutation

from .models import MenuItem

class Query(graphene.ObjectType):
    categories = DjangoListField(CategoryTypes)
    menu_items = DjangoListField(MenuItemTypes)
    menu_item = DjangoListField(MenuItemTypes, id=graphene.ID())


    def resolve_menu_item(self, info, id):
        try:
            return MenuItem.objects.filter(id=id)
        except MenuItem.DoesNotExist:
            return None
        
class Mutation(graphene.ObjectType):
    create_category = CreateCategoryMutation.Field()
    create_menu_item = CreateMenuItemMutation.Field()
    delete_menu_item = DeleteMenuItemMutation.Field()
    update_menu_item = UpdateMenuItemMutation.Field()

    


schema = graphene.Schema(query=Query, mutation=Mutation)