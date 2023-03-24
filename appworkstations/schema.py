import graphene

import pcs.schema


class Query(pcs.schema.Query, graphene.ObjectType):
    pass

class Mutation(pcs.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)