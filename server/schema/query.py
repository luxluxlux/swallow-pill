import graphene
from graphene import relay
from models import Pill as PillModel
from prototypes import Pill


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    pills_by_author = graphene.List(Pill, id=graphene.Int())

    @staticmethod
    def resolve_pills_by_author(parent, info, **args):
        q = args.get('id')
        query = Pill.get_query(info)
        return query.filter(PillModel.author == q).all()
