import graphene
from .queries import CategoryTypes, MenuItemTypes
from ..models import Category, MenuItem
from django.core.exceptions import ObjectDoesNotExist

# class type input
class CategoryInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    is_active = graphene.Boolean()


class MenuItemInput(graphene.InputObjectType):
    category_id = graphene.ID()
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
    
class DeleteCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    category =graphene.Field(CategoryTypes)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(pk=id)
        category.save()
        return DeleteCategoryMutation(category=category)

class CreateMenuItemMutation(graphene.Mutation):
    class Arguments:
        data = MenuItemInput(required=True)


    menuItem = graphene.Field(MenuItemTypes)

    @classmethod
    def mutate(cls, root, info, data):
        try:
            category_instance = Category.objects.get(id=data.category_id)
        except ObjectDoesNotExist:
            raise Exception("category does not exist")
        
        data.category = category_instance
        
        menuItem = MenuItem(**data)
        menuItem.save()

        return CreateMenuItemMutation(menuItem=menuItem)
    
class DeleteMenuItemMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    # define type on delete
    menuItem = graphene.Field(MenuItemTypes)

    @classmethod
    def mutate(cls, root, info, id):
        try:
            menuItem = MenuItem.objects.get(pk=id)
            delete_menu = menuItem
            menuItem.delete()

            return DeleteMenuItemMutation(menuItem=delete_menu)
        except MenuItem.DoesNotExist:
            return DeleteMenuItemMutation(menuItem=None)


class UpdateMenuItemMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        data = MenuItemInput()

    menuItem = graphene.Field(MenuItemTypes)
    
    @classmethod
    def mutate(cls, root, info, id, data):
        try:
            MenuItem.objects.filter(pk=id).update(**data)
            menuItem = MenuItem.objects.get(pk=id)

            return UpdateMenuItemMutation(menuItem=menuItem)
        except MenuItem.DoesNotExist:
            return UpdateMenuItemMutation(menuItem=None)
        

        