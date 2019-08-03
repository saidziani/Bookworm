import graphene

class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class HouseInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    country = graphene.String()


class WriterInput(graphene.InputObjectType):
    id = graphene.ID()
    fname = graphene.String()
    lname = graphene.String()
    email = graphene.String()
    nationality = graphene.String()
    birthday = graphene.String()


class BookInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    year = graphene.Int()
    isbn = graphene.String()
    category = graphene.Field(CategoryInput)
    writer = graphene.Field(WriterInput)
    house = graphene.Field(HouseInput)
