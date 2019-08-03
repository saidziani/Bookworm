import graphene
import app.bookworm.schema
import app.bookworm.graphql.queries.Queries
import app.bookworm.graphql.mutations.Mutations


class Query(app.bookworm.graphql.queries.Queries.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(app.bookworm.graphql.mutations.Mutations.Mutation, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

