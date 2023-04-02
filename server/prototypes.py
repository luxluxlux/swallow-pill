# Don't convert enums from the models with Graphene! This causes problem:
# https://github.com/graphql-python/graphene/issues/273
# https://github.com/graphql-python/graphene/issues/1384

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import User as UserModel, Pill as PillModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node, )


class UserAttributes:
    id = graphene.Int()
    email = graphene.NonNull(graphene.String)
    password = graphene.NonNull(graphene.String)
    language = graphene.String()


class CreateUserInput(graphene.InputObjectType, UserAttributes):
    pass


class Pill(SQLAlchemyObjectType):
    class Meta:
        model = PillModel
        interfaces = (graphene.relay.Node, )


class PillAttributes:
    id = graphene.Int()
    author = graphene.NonNull(graphene.Int)
    name = graphene.NonNull(graphene.String)
    unit = graphene.String()
    dosage = graphene.Int()
    intake = graphene.String()
    startdate = graphene.NonNull(graphene.Date)
    enddate = graphene.NonNull(graphene.Date)
    days = graphene.List(graphene.Int)
    times = graphene.List(graphene.NonNull(graphene.Time))


class CreatePillInput(graphene.InputObjectType, PillAttributes):
    pass
