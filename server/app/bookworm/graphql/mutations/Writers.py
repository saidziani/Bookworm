import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from app.bookworm.models import Writer
from app.bookworm.graphql.input_types import WriterInput
from app.bookworm.graphql.types import WriterType


# Create mutations for Writers
class CreateWriter(graphene.Mutation):
    class Arguments:
        input = WriterInput(required=True)

    ok = graphene.Boolean()
    writer = graphene.Field(WriterType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        writer_instance = Writer(fname=input.fname)
        writer_instance = Writer(lname=input.lname)
        writer_instance = Writer(email=input.email)
        writer_instance = Writer(nationality=input.nationality)
        writer_instance = Writer(birthday=input.birthday)
        writer_instance.save()
        return CreateWriter(ok=ok, writer=writer_instance)


class UpdateWriter(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = WriterInput(required=True)

    ok = graphene.Boolean()
    writer = graphene.Field(WriterType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        writer_instance = Writer.objects.get(pk=id)
        if writer_instance:
            ok = True
            writer_instance.fname = input.fname
            writer_instance.lname = input.lname
            writer_instance.email = input.email
            writer_instance.nationality = input.nationality
            writer_instance.birthday = input.birthday
            writer_instance.save()
            return UpdateWriter(ok=ok, writer=writer_instance)
        return UpdateWriter(ok=ok, writer=None)
