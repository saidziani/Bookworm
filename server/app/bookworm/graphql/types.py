import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from app.bookworm.models import Book, House, Category, Writer

# Create a GraphQL type for the Book model
class BookType(DjangoObjectType):
    class Meta:
        model = Book

# Create a GraphQL type for the Category model
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

# Create a GraphQL type for the House model
class HouseType(DjangoObjectType):
    class Meta:
        model = House

# Create a GraphQL type for the Writer model
class WriterType(DjangoObjectType):
    class Meta:
        model = Writer
