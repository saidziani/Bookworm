import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from app.bookworm.models import Book
from app.bookworm.graphql.input_types import BookInput
from app.bookworm.graphql.types import BookType


# Create mutations for Books
class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    ok = graphene.Boolean()
    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        book_instance = Book(title=input.title)
        book_instance = Book(year=input.year)
        book_instance = Book(isbn=input.isbn)
        book_instance = Book(category=input.category)
        book_instance = Book(writer=input.writer)
        book_instance = Book(house=input.house)
        book_instance.save()
        return CreateBook(ok=ok, book=book_instance)


class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = BookInput(required=True)

    ok = graphene.Boolean()
    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        book_instance = Book.objects.get(pk=id)
        if book_instance:
            ok = True
            book_instance.title = input.title
            book_instance.year = input.year
            book_instance.isbn = input.isbn
            book_instance.category = input.category
            book_instance.writer = input.writer
            book_instance.house = input.house
            book_instance.save()
            return UpdateBook(ok=ok, book=book_instance)
        return UpdateBook(ok=ok, book=None)
