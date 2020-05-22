import graphene

import covid19.schema


class Query(covid19.schema.Query, graphene.ObjectType):
    pass


class Mutation(covid19.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
