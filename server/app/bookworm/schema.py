import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Book, House, Category, Writer
from .graphql.queries.Queries import Query 
from .graphql.mutations.Mutations import Mutation


schema = graphene.Schema(query=Query, mutation=Mutation)
