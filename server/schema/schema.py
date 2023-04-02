import graphene
from schema.query import Query
from schema.mutation import Mutation
from prototypes import User, Pill

schema = graphene.Schema(query=Query, mutation=Mutation, types=[User, Pill])