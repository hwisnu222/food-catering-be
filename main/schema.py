import graphene
import graphql_jwt

import menu.schema as MenuSchema
import orders.schema as OrderSchema

class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Query(MenuSchema.Query, OrderSchema.Query, graphene.ObjectType):
    pass

class Mutation(MenuSchema.Mutation, OrderSchema.Mutation, AuthMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)