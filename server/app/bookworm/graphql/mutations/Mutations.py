import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .Books import CreateBook, UpdateBook, DeleteBook
from .Categories import CreateCategory, UpdateCategory, DeleteCategory
from .Writers import CreateWriter, UpdateWriter, DeleteWriter
from .Houses import CreateHouse, UpdateHouse, DeleteHouse


# Create a Mutation type
class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()

    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()

    create_writer = CreateWriter.Field()
    update_writer = UpdateWriter.Field()
    delete_writer = DeleteWriter.Field()

    create_house = CreateHouse.Field()
    update_house = UpdateHouse.Field()
    delete_house = DeleteHouse.Field()

