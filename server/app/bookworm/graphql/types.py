import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from app.bookworm.models import Book, House, Category, Writer, User

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

# Create a GraphQL type for the User model
class UserType(DjangoObjectType):
    class Meta:
        model = User
