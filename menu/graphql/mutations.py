import graphene
from .queries import CategoryTypes, MenuItemTypes
from ..models import Category, MenuItem

# class type input
class CategoryInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    is_active = graphene.Boolean()


class MenuItemInput(graphene.InputObjectType):
    category = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    base_price = graphene.Decimal()
    dietary_type = graphene.String()
    preparation_time = graphene.Int()
    is_available = graphene.Boolean()
    image = graphene.String()

class CreateCategoryMutation(graphene.Mutation):
    class Arguments:
        data = CategoryInput(required=True)


    category = graphene.Field(CategoryTypes)

    @classmethod
    def mutate(cls, root, info, data):
        category = Category(**data)
        category.save()

        return CreateCategoryMutation(category=category)

class CreateMenuItemMutation(graphene.Mutation):
    class Arguments:
        data = MenuItemInput(required=True)


    category = graphene.Field(MenuItemTypes)

    @classmethod
    def mutate(cls, root, info, data):
        menu_item = MenuItem(**data)
        menu_item.save()

        return CreateMenuItemMutation(menu_item=menu_item)

        