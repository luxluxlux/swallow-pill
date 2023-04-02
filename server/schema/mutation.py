import graphene
from application import db
from models import User as UserModel, Pill as PillModel
from prototypes import User, CreateUserInput, Pill, CreatePillInput


class CreateUser(graphene.Mutation):
    user = graphene.Field(lambda: User)
    ok = graphene.Boolean()

    class Arguments:
        input = CreateUserInput(required=True)

    @staticmethod
    def mutate(self, info, input):
        user = UserModel(**input)
        db.session.add(user)
        db.session.commit()
        ok = True
        return CreateUser(user=user, ok=ok)


class CreatePill(graphene.Mutation):
    pill = graphene.Field(lambda: Pill)
    ok = graphene.Boolean()

    class Arguments:
        input = CreatePillInput(required=True)

    @staticmethod
    def mutate(self, info, input):
        pill = PillModel(**input)
        db.session.add(pill)
        db.session.commit()
        ok = True
        return CreatePill(pill=pill, ok=ok)


class Mutation(graphene.ObjectType):
    createPill = CreatePill.Field()
    createUser = CreateUser.Field()
