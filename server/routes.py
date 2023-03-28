from flask import Blueprint, render_template
from flask_graphql import GraphQLView
from schema.schema import schema

routes = Blueprint("routes", __name__)

# Disable for production
# https://github.com/graphql-python/graphene-django/issues/707
routes.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)


@routes.route('/')
def index():
    return render_template('index.html')
