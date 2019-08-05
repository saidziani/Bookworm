import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .Books import CreateBook, UpdateBook
from .Categories import CreateCategory, UpdateCategory
from .Writers import CreateWriter, UpdateWriter
from .Houses import CreateHouse, UpdateHouse


# Create a Mutation type
class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()

    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()

    create_writer = CreateWriter.Field()
    update_writer = UpdateWriter.Field()

    create_house = CreateHouse.Field()
    update_house = UpdateHouse.Field()

