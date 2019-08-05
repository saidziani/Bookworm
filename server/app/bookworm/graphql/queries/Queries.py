import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from app.bookworm.models import Book, House, Category, Writer, User
from app.bookworm.graphql.types import BookType, HouseType, CategoryType, WriterType, UserType

# Create a Query type
class Query(ObjectType):
    # Books
    book = graphene.Field(BookType, id=graphene.Int())
    books = graphene.List(BookType)

    def resolve_book(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Book.objects.get(pk=id)
        return None

    def resolve_books(self, info, **kwargs):
        return Book.objects.all()

    # Categories
    category = graphene.Field(CategoryType, id=graphene.Int())
    categories = graphene.List(CategoryType)

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Category.objects.get(pk=id)
        return None

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    # Houses
    house = graphene.Field(HouseType, id=graphene.Int())
    houses = graphene.List(HouseType)

    def resolve_house(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return House.objects.get(pk=id)
        return None

    def resolve_houses(self, info, **kwargs):
        return House.objects.all()

    # Writers
    writer = graphene.Field(WriterType, id=graphene.Int())
    writers = graphene.List(WriterType)

    def resolve_writer(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Writer.objects.get(pk=id)
        return None

    def resolve_writers(self, info, **kwargs):
        return Writer.objects.all()

    # Users
    user = graphene.Field(UserType, id=graphene.Int())
    users = graphene.List(UserType)

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return User.objects.get(pk=id)
        return None

    def resolve_users(self, info, **kwargs):
        return User.objects.all()
