import graphene

import menu.schema as MenuSchema
import orders.schema as OrderSchema


class Query(MenuSchema.Query, OrderSchema.Query, graphene.ObjectType):
    pass

class Mutation(MenuSchema.Mutation, OrderSchema.Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)