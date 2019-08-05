import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from app.bookworm.models import House
from app.bookworm.graphql.input_types import HouseInput
from app.bookworm.graphql.types import HouseType


# Create mutations for Houses
class CreateHouse(graphene.Mutation):
    class Arguments:
        input = HouseInput(required=True)

    ok = graphene.Boolean()
    house = graphene.Field(HouseType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        house_instance = House(name=input.name, country=input.country)
        house_instance.save()
        return CreateHouse(ok=ok, house=house_instance)


class UpdateHouse(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = HouseInput(required=True)

    ok = graphene.Boolean()
    house = graphene.Field(HouseType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        house_instance = House.objects.get(pk=id)
        if house_instance:
            ok = True
            house_instance.name = input.name
            house_instance.country = input.country
            house_instance.save()
            return UpdateHouse(ok=ok, house=house_instance)
        return UpdateHouse(ok=ok, house=None)
